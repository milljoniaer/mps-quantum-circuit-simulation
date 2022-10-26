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

def perform_two_qubit_gate(M1, M2, U):
    """
    Performing a two qubit gate U on the given tensors, those two have to be neightbours
    The algorithm is based on the paper.

    Currently there is no approximation and hence no orthonomalization
    """
    # TODO Add orthonomalisation to decrease error rate
    print(f'IN: M1: {np.shape(M1)}; M2: {np.shape(M2)}')
    T = np.einsum("hij, kjl -> hkil", M1, M2)
    print(f'nach (8): T: {T.shape}')
    U = np.reshape(U, [2,2,2,2])
    T_tick = np.einsum("hijk, jklm -> hilm", U, T)
    print(f'T\': {T_tick.shape}')

    n = T_tick.shape[2]
    m = T_tick.shape[3]
    T_tick = np.reshape(T_tick, [2 * n, 2 * m])
    print(f'reshaped T\': {T_tick.shape}')

    # TODO approximate
    X, S, Y = np.linalg.svd(T_tick)

    print(S)
    print(f'X: {X.shape}; S: {S.shape}; Y: {Y.shape}')
    X = X[:, :len(S)] * S
    
    M1 = np.reshape(X, [2, n, X.shape[1]])
    M2 = np.reshape(Y, [2, Y.shape[1], m])

    print(f'OUT: M1: {M1.shape}; M2: {M2.shape}')
    return M1, M2

