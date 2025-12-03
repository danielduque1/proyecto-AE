from mace.calculators import mace_off
from ase import build

atoms = build.molecule('H2O')
calc = mace_off(model="medium", device='cpu')
atoms.set_calculator(calc)
print(atoms.get_potential_energy())