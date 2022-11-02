# MPS Quantum Computing Simulation
This Repository contains a MPS based quantum circuit simutlation. It has been written for the Quantum Computing Seminar at the Technical University of Munich. The simulator is based on a paper about the ["Limits of the simulation of quantum computers on classical computers"](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.10.041038).

## Installation
To install the dependencys of this project run `pip3 install numpy`. This project relies on the algebraic operations of numpy.

## Examples

### Greenberger-Horne-Zeilinger state
Run `python3 ghz.py` to generate the [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state) with 3 particles, using the MPS simulation. The ouput should be a statevector in the GHZ format.

![image](https://user-images.githubusercontent.com/78978542/199467893-180f278b-0d92-4491-9185-fcc6dec5b029.png)

### Complicated Circuit
This a circuit to test how efficient this simulation is. Adjust N (number of qubits) and D (number of 2 particle gates on each qubit), to see the performance of the simulation. The time for applying the circuit is measured and printed.

Format of the circuit:

![image](https://user-images.githubusercontent.com/78978542/199468414-7fb34d24-8340-40b8-93d9-3d2d4bfdcb33.png)

1-qubit gate: h-gate; 2-qubit gate: control-not gate
