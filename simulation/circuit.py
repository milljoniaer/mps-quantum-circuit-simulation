import sys
from .operations import *

class Circuit:

    gates = []    

    def __init__(self, bit_sequence):
        self.n = len(bit_sequence)
        self.mps = bit_sequence_to_qubit_mps(bit_sequence)

    def add_gate(self, gate, i, j=-1):
        if np.shape(gate) == (2,2):
            self.gates.append({ "gate": gate, "type": "one", "i": i})
        elif np.shape(gate) == (4,4):
            if (i + 1 != j):
                print("Two qubit gates can only be applied to adjacent tensors")
                sys.exit(1)
            self.gates.append({ "gate": gate, "type": "two", "i": i, "j": j})
        else:
            print("ERROR: Unsupported gate type! Only one and two qubit gates are valid!")
        

    def run(self):
        for gate in self.gates:
            if gate["type"] == "one":
                print(f'One qubit gate at {gate["i"]}')
                self.mps[gate["i"]] = perform_one_qubit_gate(self.mps[gate["i"]], gate["gate"])
            elif gate["type"] == "two":
                i, j = gate["i"], gate["j"]
                print(f'Two qubit gate at : ({i},{j}) -> shapes: {np.shape(self.mps[i])}; {np.shape(self.mps[j])}')
                self.mps[i], self.mps[j] = perform_two_qubit_gate(self.mps[i], self.mps[j], gate["gate"])
            else:
                print("ERROR: Invalid gate detected! Only one and two qubit gates are valid!")
                sys.exit(1)

            # log_mps_structure(self.mps)

        self.gates = []

    def state_vector(self):
        return mps_to_state_vector(self.mps)
