from simulation import Circuit, GATES

# Generation of Greenberger-Horne-Zeilinger state (GHZ)
# see: https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_states

N = 3
# qubits in "bit" structure
bit_sequence = N * [0]

circuit = Circuit(bit_sequence)
circuit.add_gate(GATES.h, 0)
circuit.add_gate(GATES.cx, 0, 1)
circuit.add_gate(GATES.cx, 1, 2)

circuit.run()

sv = circuit.state_vector()
print(sv)
