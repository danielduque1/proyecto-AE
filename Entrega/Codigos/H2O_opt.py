from utils import *

from mace.calculators import mace_mp

from ase import Atoms
from ase.optimize import BFGS
from ase.io import read
from ase.visualize import view
import os

directorio_actual = os.getcwd()
print(directorio_actual)

path_traj = "./Entrega/Codigos/trayectorias"

N2 = Atoms('N2', positions=[[0, 0, -1], [0, 0, 1]])
N2.center(vacuum=3.5)

calc_mace = mace_mp(model="medium", default_dtype="float64", device="cpu")
N2.calc = calc_mace 
opt_N2 = BFGS(N2,trajectory=path_traj + "/traj_n2.traj")
opt_N2.run(fmax=0.01)

traj = read(path_traj + "/traj_n2.traj", ':')   # dos puntos = leer toda la trayectoria
view(traj) 

vib_N2 = Vibrations(N2, name='./Entrega/Codigos/vib_N2')
vib_N2.run()
vib_N2.summary(log='./Entrega/Codigos/txt/N2_vib_summary.log')