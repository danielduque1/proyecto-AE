from ase import Atoms
from mace.calculators import mace_off

# 1. Definimos un átomo de hidrógeno en el origen
atoms_H = Atoms('H', positions=[[0.0, 0.0, 0.0]])

# 2. Creamos un calculador MACE-OFF23
#    - model="small" o "medium" o "large" según quieras
#    - device="cpu" para probar en CPU
calc = mace_off(model="small", device="cpu")  # usa OFF23 pretrained :contentReference[oaicite:2]{index=2}

# 3. Asociamos el calculador al sistema
atoms_H.calc = calc

# 4. Pedimos energía y fuerzas
E_H = atoms_H.get_potential_energy()   # escalar (eV)
F_H = atoms_H.get_forces()             # array (1, 3) en eV/Å

print("Energía H:", E_H, "eV")
print("Fuerzas H:\n", F_H, "eV/Å")
