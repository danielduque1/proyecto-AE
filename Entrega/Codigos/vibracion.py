from ase.io import read
from mace.calculators import mace_mp, MACECalculator
from ase.optimize import BFGS, QuasiNewton
from ase.vibrations import Vibrations

import numpy as np
import matplotlib.pyplot as plt

atoms = read("./Entrega/datos/dataset_hemina_big.xyz", index=0)

# calc = mace_mp(model="medium", dispersion=False, default_dtype="float64", 
# 	#device='cuda', 
# 	txt="output-mace.txt")

calc = MACECalculator(model_paths="./Entrega/Modelos/mace01.model", device="cpu", default_dtype="float64")

atoms.calc = calc
vib = Vibrations(atoms,name='./Entrega/Codigos/vib_ReTrain')

freqs = np.abs(np.array(vib.get_frequencies()))
freqs = freqs[freqs > 0]

x = np.linspace(0, freqs.max() + 200, 4000)
sigma = 20.0

spec = sum(np.exp(-(x - f)**2 / (2*sigma**2)) for f in freqs)

plt.plot(x, spec)
plt.title("Espectro de vibraciones - Hemina (Reentrenado)")
plt.xlabel("Frecuencia (cm$^{-1}$)")
plt.ylabel("Intensidad (arb.)")
plt.show()
