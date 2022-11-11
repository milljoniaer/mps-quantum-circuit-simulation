# MPS Quantum Computing Simulation
This Repository contains quantum circuit simutlation using a Matrix-Product-State representation of the quantum state. It is an approximation algorithm to scale linear with the number of qubits and the depth of the circuit. It has been written for the Quantum Computing Seminar at the Technical University of Munich. The simulator is based on a paper about the ["Limits of the simulation of quantum computers on classical computers"](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.10.041038).

## Installation
To use this simulation package you need to install some dependencies.

Run the following code to install them:

```
pip3 install numpy # needed for the tensor operations
pip3 install tqdm  # displays a progress bar during running the circuit

# optional for recalculating the results (plotting)
# pip3 install matplotlib 
```

## Examples

### Greenberger-Horne-Zeilinger state
Run `python3 ghz-simulation.py` to generate the [GHZ state](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state) with 3 particles, using the MPS simulation. The ouput should be a statevector in the GHZ format.

Generation:

![image](https://user-images.githubusercontent.com/78978542/199467893-180f278b-0d92-4491-9185-fcc6dec5b029.png)

Result: GHZ state:

![image](https://user-images.githubusercontent.com/78978542/199470730-b682284b-5fd2-4148-b5da-b389b81fc748.png)


### Complicated Circuit
This a circuit to test how efficient this simulation is. Adjust N (number of qubits) and D (number of 2 particle gates on each qubit), to see the performance of the simulation. This circuit is the one they use in the paper for their research. It is used in the paper to proof that classical computers can still rival quantum computers like googles [sydacore processore](https://ai.googleblog.com/2019/10/quantum-supremacy-using-programmable.html).

The time for applying the circuit is measured and printed. Run `python3 complicated-circuit.py` to do so.

Format of the circuit:

![image](https://user-images.githubusercontent.com/78978542/199468414-7fb34d24-8340-40b8-93d9-3d2d4bfdcb33.png)

1-qubit gate: h-gate; 2-qubit gate: control-not gate

## Results

Have a look at the `/results` subfolder to view some analytics. The scripts to generate these plots are located in the root folder. 

To run these scripts you need to install [Matploblib](https://matplotlib.org/stable/index.html).
