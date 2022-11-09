from time import time
from simulation import Circuit, GATES

def run(N, D, chi):
    """
    Run an example circuit with given Number of qubits N, Depth D and maximum bond dimension chi.

    Returns duration of the running circuit and the average fidelity.
    """

    # setting up the circuit with first state
    print(f'Setting up circuit with N: {N}; D: {D}; chi: {chi}')
    bit_sequence = N * [0]
    circuit = Circuit(bit_sequence, chi)

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

    endTime = time()
    duration = '{:5.3f}s'.format(endTime-startTime)
    print(f'Done in {duration}!')

    # print(circuit.fidelities)
    f_av = sum(circuit.fidelities) / len(circuit.fidelities)
    print(f_av)
    duration_int = endTime - startTime
    return f_av, duration_int
