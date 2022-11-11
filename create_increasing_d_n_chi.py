import matplotlib.pyplot as plt
from run_example_circuit import run


plot_filename = "increasing-d-n-chi.png"

depths = [64, 128, 192, 256, 320, 384, 448]
fidelities_1 = [0.9644408920889231, 0.9632109753598538, 0.9632109753598538, 0.9632109753598538, 0.9618930914694316, 0.9619299415668865, 0.9620216807845084]
fidelities_2 = [0.9700268950604446, 0.971785122331185,  0.9732882096359137, 0.9742277764466712, 0.9752805763668293, 0.9761480666020852, 0.9769123270199761]
fidelities_3 = [0.9588581677380587, 0.9590730708685185, 0.9592988844939548, 0.9629328141925366, 0.9621914476207372, 0.9619170610900144, 0.9653617333735894]

#for chi in range(64, 512, 64):
#    depths.append(chi)
#    f_av, duration_int = run(60, 40, chi)
#    fidelities_1.append(f_av)

#for chi in range(64, 512, 64):
#    
#    f_av, duration_int = run(30, 100, chi)
#    fidelities_2.append(f_av)

#for chi in range(64, 512, 64):
#    
#    f_av, duration_int = run(60, 100, chi)
#    fidelities_3.append(f_av)

print("Building Plot...")
fig, ax = plt.subplots()
ax.scatter(depths, fidelities_1, c="blue")
ax.scatter(depths, fidelities_2, c="red")
ax.scatter(depths, fidelities_3, c="green")
ax.legend()
ax.set_xlabel(r'$\chi$')
ax.set_ylabel("f_av")
plt.title("Fidelity with increasing with increasing all")
#plt.figtext(0.1, 0.01, f'$\chi$ = {chi}')

print(f'Saving plot as {plot_filename}...')
plt.savefig(plot_filename)
print("Done!")

plt.show()