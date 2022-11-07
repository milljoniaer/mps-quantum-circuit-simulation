import sys
from .operations import *

class Circuit:

    gates = []

    def __init__(self, bit_sequence, chi=64, verbose=False, truncate=True):
        """
        Inits the circuit with a given state as bit_sequence.

        chi represents the maximal bond dimension for the truncation.
        """
        self.n = len(bit_sequence)
        self.mps = bit_sequence_to_qubit_mps(bit_sequence)
        self.chi = chi
        self.verbose = verbose
        self.truncate = truncate

    def add_gate(self, gate, i, j=-1):
        """
        appends a new gate (2x2 or 4x4 matrix) on the qubits i and j (only i if one-qubit gate).

        i and j have to be adjacent
        """
        if np.shape(gate) == (2,2):
            self.gates.append({ "gate": gate, "type": "one", "i": i})
        elif np.shape(gate) == (4,4):
            if i + 1 != j:
                print("Two qubit gates can only be applied to adjacent tensors")
                sys.exit(1)
            self.gates.append({ "gate": gate, "type": "two", "i": i, "j": j})
        else:
            print("ERROR: Unsupported gate type! Only one and two qubit gates are valid!")

    def run(self):
        """
        Applies the circuit.
        The Gates are applied on their qubits in the order they are in the array
        """
        for gate in self.gates:
            if gate["type"] == "one":
                if self.verbose:
                    print(f'One qubit gate at {gate["i"]}')
                self.mps[gate["i"]] = perform_one_qubit_gate(self.mps[gate["i"]], gate["gate"])
            elif gate["type"] == "two":
                i, j = gate["i"], gate["j"]
                if self.verbose:
                    print(f'Two qubit gate at : ({i},{j}) -> shapes: {np.shape(self.mps[i])}; {np.shape(self.mps[j])}')
                self.mps[i], self.mps[j] = perform_two_qubit_gate(self.mps[i], self.mps[j], gate["gate"], self.chi, self.truncate)
            else:
                print("ERROR: Invalid gate detected! Only one and two qubit gates are valid!")
                sys.exit(1)

        self.gates = []

    def state_vector(self):
        """
        returns the current state of the network as state vector
        """
        return mps_to_state_vector(self.mps)
