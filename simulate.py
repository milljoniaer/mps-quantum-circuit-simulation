import numpy as np
from simulation import *

# Generation of Greenberger-Horne-Zeilinger state (GHZ)
# see: https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_states

N = 3
# qubits in "bit" structure
bit_sequence = N * [0]

mps = bit_sequence_to_qubit_mps(bit_sequence)
mps[0] = perform_one_qubit_gate(mps[0], GATES.h)

mps[0], mps[1] = perform_two_qubit_gate(mps[0], mps[1], GATES.cx)
mps[1], mps[2] = perform_two_qubit_gate(mps[1], mps[2], GATES.cx)

sv = mps_to_state_vector(mps)
print(sv)
