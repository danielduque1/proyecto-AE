import numpy as np
from ase.io import read, write

infile = "Entrega/datos/train_data.xyz"
outfile = "Entrega/datos/train_data_ref.xyz"

frames = read(infile, index=":")

fixed = []
for i, at in enumerate(frames):
    # 1) Energía: copiar de 'energy' -> 'REF_energy' si existe
    if "REF_energy" not in at.info:
        if "energy" in at.info:
            at.info["REF_energy"] = float(at.info["energy"])
        elif "free_energy" in at.info:
            at.info["REF_energy"] = float(at.info["free_energy"])
        else:
            # Si no hay energía, esto es grave para training con energía
            raise ValueError(f"Frame {i}: no encuentro energy/free_energy para construir REF_energy")

    # 2) Fuerzas: copiar de 'forces' -> 'REF_forces' si existe
    if "REF_forces" not in at.arrays:
        if "forces" in at.arrays:
            at.arrays["REF_forces"] = np.array(at.arrays["forces"], dtype=float)
        else:
            # Si no hay fuerzas, rellenar con ceros (útil para IsolatedAtom)
            at.arrays["REF_forces"] = np.zeros((len(at), 3), dtype=float)

    # 3) (Opcional) Limpieza: evita que el loader se confunda con claves antiguas
    # Puedes comentar esto si quieres conservarlas
    # at.info.pop("energy", None)
    # if "forces" in at.arrays: del at.arrays["forces"]

    fixed.append(at)

write(outfile, fixed, format="extxyz")
print(f"Escribí {len(fixed)} configuraciones en {outfile}")
