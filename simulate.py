import numpy as np
from simulation import *

"""
1. Convert State vector into MPS

2. Apply Gate

3. SVD to approximate state

4. Convert MPS into state vector
"""

# qubits in "bit" structure
bit_sequence = [0,0,0,0]
# X gate
X = [[0,1], [1,0]]

mps = bit_sequence_to_qubit_mps(bit_sequence)

print(mps)

mps[1] = perform_one_qubit_gate(mps[1], X)

print(mps)

