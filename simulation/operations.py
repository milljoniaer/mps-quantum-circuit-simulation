import numpy as np
import math

def bit_sequence_to_qubit_mps(bit_sequence):
    """
    Convert a Sequence of bits int a mps
    """
    return [[[[1-qubit]], [[qubit]]] for qubit in bit_sequence]


def perform_one_qubit_gate(M, U):
    """
    Performe one qubit gate on given tensor.
    """
    M = np.einsum("hi, ijk -> hjk", U, M)
    return M

def perform_two_qubit_gate(M1, M2, U, chi, truncate, fidelities):
    """
    Performing a two qubit gate U on the given tensors, those two have to be neightbours
    The algorithm is based on the paper.

    Currently there is no orthonomalization to decrease the error rate

    chi is the number of the maximal bond dimension,
    truncate controls if the MPS should be truncated.
    """
    # TODO Add orthonomalisation to decrease error rate
    T = np.einsum("hij, kjl -> hkil", M1, M2)
    U = np.reshape(U, [2,2,2,2])
    T_tick = np.einsum("hijk, jklm -> hilm", U, T)

    n = T_tick.shape[2]
    m = T_tick.shape[3]
    T_tick = np.reshape(T_tick, [2 * n, 2 * m])

    X, S, Y = np.linalg.svd(T_tick)
    calculate_fidelity(fidelities, S, chi)
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

def calculate_fidelity(fidelities, S, chi):
    """
    calculate fidelity of a 2-qubit gate by the given Singular Values S.
    the fidelity is added to the given array of fidelities.
    """
    
    approx_sum = 0
    perfect_sum = 0

    for i in range(len(S)):
        square = np.square(S[i])
        if i < chi:
            approx_sum += square
        perfect_sum += square

    fidelity = np.sqrt(approx_sum) / np.sqrt(perfect_sum)
    if math.isnan(fidelity):
        # happens if the difference is to small, therefore we approximate with 1
        fidelities.append(1)
    else:
        fidelities.append(fidelity)

