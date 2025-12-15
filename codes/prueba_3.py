from ase import build
from mace.calculators import mace_mp

# 1. Construimos la molécula H2
atoms_H2 = build.molecule('CO2')  # 2 átomos, con una distancia de enlace razonable


print(atoms_H2.get_angle(0, 1, 2))

calc = mace_mp(model="small", device="cpu")
atoms_H2.calc = calc


descriptor = calc.get_descriptors(atoms_H2)
print("Descriptor:\n", descriptor)

# # 2. Creamos el mismo tipo de calculador
# calc = mace_mp(model="small", device="cpu")

# # 3. Asociamos calculador
# atoms_H2.calc = calc

# # 4. Pedimos energía y fuerzas
# E_H2 = atoms_H2.get_potential_energy()
# F_H2 = atoms_H2.get_forces()

# print("Energía H2:", E_H2, "eV")
# print("Fuerzas H2:\n", F_H2, "eV/Å")
