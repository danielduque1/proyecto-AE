from ase.visualize import view
from ase.io import read

traj = read('./codes/mace03_md.xyz', ':')
view(traj)

