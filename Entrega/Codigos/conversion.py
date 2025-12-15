from ase.io import read, write
from ase.visualize import view
# from ase.io.sdf import read_sdf

# Leer todas las imágenes
atoms_list = read("Entrega/datos/dataset_hemina_big.xyz",":")
print(f"Número de imágenes leídas: {len(atoms_list)}")
print(f"numero de atomos : {len(atoms_list[2])}")
print(f"info : {atoms_list[2].arrays}")
print(f"CH symbols : {atoms_list[2].get_chemical_symbols()}")


view(atoms_list)

# Escribir a xyz (multi-frame)
# write("Entrega/datos/data1.xyz", atoms_list)
