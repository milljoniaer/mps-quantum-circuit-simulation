import matplotlib.pyplot as plt
from run_example_circuit import run

chi = 512
step_size = 100

plot_filename = "increasing-depth-n.png"

depths = []
fidelities_n_1 = []
fidelities_n_2 = []
fidelities_n_3 = []

N = 10
for d in range(100, 1000, step_size):
    depths.append(d)
    f_av, duration_int = run(N, d, chi)
    fidelities_n_1.append(f_av)

N = 30
for d in range(100, 1000, step_size):
    f_av, duration_int = run(N, d, chi)
    fidelities_n_2.append(f_av)

N = 60
for d in range(100, 1000, step_size):
    f_av, duration_int = run(N, d, chi)
    fidelities_n_3.append(f_av)

print("Building Plot...")
fig, ax = plt.subplots()
ax.scatter(depths, fidelities_n_1, c="blue")
ax.scatter(depths, fidelities_n_2, c="red")
ax.scatter(depths, fidelities_n_3, c="green")
ax.legend()
ax.set_xlabel("D")
ax.set_ylabel("f_av")
plt.title("Fidelity with increasing depth D and number of qubits N")
plt.figtext(0.1, 0.01, f'$\chi$ = {chi}')

print(f'Saving plot as {plot_filename}...')
plt.savefig(plot_filename)
print("Done!")

plt.show()