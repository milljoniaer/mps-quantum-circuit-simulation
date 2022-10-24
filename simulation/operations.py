import numpy as np

def bit_sequence_to_qubit_mps(bit_sequence):
    """
    Convert a Sequence of bits (qubits with 100% probability for 1 or 0) int a mps
    """
    return [[[[1-qubit]], [[qubit]]] for qubit in bit_sequence]


def perform_one_qubit_gate(qubit, gate):
    """
    Performe one qubit gate on given tensor. 
    -> Multiply statevector with gate matrix
    """
    sv = np.matmul(gate, [qubit[0][0][0], qubit[1][0][0]])
    qubit[0][0][0] = sv[0]
    qubit[1][0][0] = sv[1]
    return qubit
