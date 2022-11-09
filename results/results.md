# Results 

This folder contains some results that have been computed by the algorithm. The scrit-files that have been used for this results are located in the projects root folder.

## Increasing maximum number of bond dimensions

As expected, the 2-qubit fidelity becomes more exact, once we increase the max-bond-dimension size. If we increase it exponentially large, the fidelity will become 1.

![Increasing chi](increasing-chi.png)

## Increase number of qubits N and depth D

If we increase both the number of qubits and the depth of the circuit, the fidelity decreases. 

It is stated in the paper, that the fidelity converges at a static value. With my results, I can not underline those assumptions.
But the reason for this could be that there is no orthonomalization at each 2-qubit gate. This would lower the error rate.

![Increase N and D](increasing-depth-n.png)