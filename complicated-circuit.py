from time import time
from simulation import Circuit, GATES

# Implements the simulation of the circuit used in the paper to explain the algorithm.
#
# N = Number of qubits; D = Number of 2-qubit gates on each qubit


N = 20
D = 200


# setting up the circuit with first state
print("Setting up circuit...")
bit_sequence = N * [0]
circuit = Circuit(bit_sequence)

print("Adding Gates...")
for d in range(D):
    # adding one qubit gates first
    for n in range(N):
        circuit.add_gate(GATES.h, n)

    # adding two qubit gates
    n = d % 2
    while n < N-1:
        circuit.add_gate(GATES.cx, n, n+1)
        n = n + 2

print("Start running the circuit...")
startTime = time()

circuit.run()
sv = circuit.state_vector()

endTime = time()
duration = '{:5.3f}s'.format(endTime-startTime)
print(f'Done in {duration}!')

# print(sv)
