path = "./Entrega/datos/b-hematin acuoso.txt"

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(path)
frequencies = data[:, 0]
intensities = data[:, 1]

intensities = intensities.max() - intensities

plt.plot(frequencies, intensities)
plt.xlabel("Frecuencia (cm$^{-1}$)")
plt.ylabel("Intensidad (arb.)")
plt.title("Espectro IR de B-hematin en agua")
plt.show()
