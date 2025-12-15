from ase.io import read
from mace.calculators import mace_mp
from ase.optimize import BFGS, QuasiNewton
from ase.vibrations import Vibrations

atoms = read("Entrega/datos/dataset_hemina_big.xyz", index=0)
calc = mace_mp(model="medium", dispersion=False, default_dtype="float64", 
	#device='cuda', 
	txt="output-mace.txt")

atoms.calc = calc
print(atoms.get_potential_energy())

opt = BFGS(atoms, trajectory='opt.traj', logfile='opt.log')
opt.run(fmax=0.05)

vib = Vibrations(atoms)
vib.run()
vib.summary(log='Entrega/Resultado/vib_summary.log')

