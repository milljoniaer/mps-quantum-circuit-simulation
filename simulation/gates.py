import numpy as np

class GATES:
    """
    static class too easily import gates
    reference: https://en.wikipedia.org/wiki/Quantum_logic_gate
    """

    # one qubit gates
    x = [[0,1], [1,0]]
    z = [[1,0], [0,-1]]
    h = [[1,1], [1,-1]] / np.sqrt(2)

    # two qubit gates
    cx = [[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]
    cz = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,-1]]
    swap = [[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]]