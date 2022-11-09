import matplotlib.pyplot as plt
from run_example_circuit import run

N = 10
D = 500

plot_filename = "increasing-chi.png"

chis = []
fidelities = []

for chi in range(4, 56):
    f_av, duration_int = run(N, D, chi)
    chis.append(chi)
    fidelities.append(f_av)

print("Building Plot...")
fig, ax = plt.subplots()
ax.scatter(chis, fidelities)
ax.set_xlabel(r'$\chi$')
ax.set_ylabel("f_av")
plt.title("Fidelity with increasing " + r'$\chi$')
plt.figtext(0.01, 0.01, f'N = {N}; D = {D}')

print(f'Saving plot as {plot_filename}...')
plt.savefig(plot_filename)
print("Done!")

plt.show()