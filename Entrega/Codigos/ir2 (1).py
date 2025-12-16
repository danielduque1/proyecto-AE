from ase.io import read
from ase.visualize import view
from mace.calculators import mace_mp, MACECalculator
from ase.optimize import BFGS
from ase.vibrations import Vibrations
# from ase.build import molecule
import numpy as np
import matplotlib.pyplot as plt

atoms = read("E:\Aprendizaje_Est\proyecto-AE\Entrega\datos\dataset_hemina_big.xyz", index=0)
view(atoms)
# atoms = molecule("H2O")	

# calc = mace_mp(model="medium", dispersion=False, default_dtype="float64", 
# 	#device='cuda', 
# 	txt="output-mace.txt")
#pt_head
calc = MACECalculator(model_paths="E:\Aprendizaje_Est\proyecto-AE\Entrega\Modelos\multihead_finetuned_MACE.model", device="cpu", default_dtype="float64",head="pt_head")

atoms.calc = calc

opt = BFGS(atoms, trajectory='Entrega/Codigos/trayectorias/MHpt_train_opt.traj', logfile='Entrega/Codigos/trayectorias/MHpt_train_opt.log')
opt.run(fmax=0.05)
print(atoms.get_potential_energy())

vib = Vibrations(atoms,name='Entrega/Codigos/vib_MHpt_train')
vib.run()
vib.summary(log='Entrega/Resultado/vib_summary_MHpt_train.log')

freqs = np.abs(np.array(vib.get_frequencies()))
freqs = freqs[freqs > 0]

x = np.linspace(0, freqs.max() + 200, 4000)
sigma = 20.0

spec = sum(np.exp(-(x - f)**2 / (2*sigma**2)) for f in freqs)

plt.plot(x, spec)
plt.title("Espectro de vibraciones - Hemina (pt_head Finetuned)")
plt.xlabel("Frecuencia (cm$^{-1}$)")
plt.ylabel("Intensidad (arb.)")
plt.show()

print("Frecuencias (cm^-1):", freqs)
print(f"frec originales: {vib.get_frequencies()}")