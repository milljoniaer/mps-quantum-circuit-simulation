import matplotlib.pyplot as plt
from run_example_circuit import run

chi = 20
step_size = 50

plot_filename = "increasing-depth-n.png"

depths = []
fidelities_n_5 = []
fidelities_n_10 = []
fidelities_n_15 = []

N = 5
for d in range(100, 1000, step_size):
    depths.append(d)
    f_av, duration_int = run(N, d, chi)
    fidelities_n_5.append(f_av)

N = 10
for d in range(100, 1000, step_size):
    f_av, duration_int = run(N, d, chi)
    fidelities_n_10.append(f_av)

N = 15
for d in range(100, 1000, step_size):
    f_av, duration_int = run(N, d, chi)
    fidelities_n_15.append(f_av)

print("Building Plot...")
fig, ax = plt.subplots()
ax.scatter(depths, fidelities_n_5, c="blue")
ax.scatter(depths, fidelities_n_10, c="red")
ax.scatter(depths, fidelities_n_15, c="green")
ax.legend()
ax.set_xlabel("D")
ax.set_ylabel("f_av")
plt.title("Fidelity with increasing depth D and number of qubits N")
plt.figtext(0.1, 0.01, f'$\chi$ = {chi}')

print(f'Saving plot as {plot_filename}...')
plt.savefig(plot_filename)
print("Done!")

plt.show()