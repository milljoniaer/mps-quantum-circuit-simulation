import numpy as np

def bit_sequence_to_qubit_mps(bit_sequence):
    """
    Convert a Sequence of bits (qubits with 100% probability for 1 or 0) int a mps
    """
    return [[[[1-qubit]], [[qubit]]] for qubit in bit_sequence]


def perform_one_qubit_gate(M, U):
    """
    Performe one qubit gate on given tensor. 
    """
    sv = np.matmul(U, [M[0][0][0], M[1][0][0]])
    M[0][0][0] = sv[0]
    M[1][0][0] = sv[1]
    return M

def perform_two_qubit_gate(M1, M2, U, chi, truncate):
    """
    Performing a two qubit gate U on the given tensors, those two have to be neightbours
    The algorithm is based on the paper.

    Currently there is no orthonomalization to decrease the error rate

    chi is the number of the maximal bond dimension
    """
    # TODO Add orthonomalisation to decrease error rate
    T = np.einsum("hij, kjl -> hkil", M1, M2)
    U = np.reshape(U, [2,2,2,2])
    T_tick = np.einsum("hijk, jklm -> hilm", U, T)
    

    n = T_tick.shape[2]
    m = T_tick.shape[3]
    T_tick = np.reshape(T_tick, [2 * n, 2 * m])
    #print(f'shape: T\': {np.shape(T_tick)}')

    X, S, Y = np.linalg.svd(T_tick)
    if truncate:
        # doing the magic: truncation
        S = S[:chi]
    X = X[:, :len(S)] * S
    Y = Y[:, :len(S)]
    
    M1 = np.reshape(X, [2, n, X.shape[1]])
    M2 = np.reshape(Y, [2, Y.shape[1], m])

    return M1, M2

def mps_to_state_vector(mps):
    """
    converts a given matrix product state into a state-vector
    """
    sv = mps[0]
    for i in range(1, len(mps)):
        M = np.einsum("hij, kjl -> hkil", sv, mps[i])
        M = np.reshape(M, (M.shape[0] * M.shape[1], M.shape[2], M.shape[3]))
        sv = M

    return np.reshape(sv, (sv.shape[0]))

def log_mps_structure(mps):
    """
    logs the shape of each tensor of a given matrix product state
    """
    print(list(map(lambda node: np.shape(node), mps)))