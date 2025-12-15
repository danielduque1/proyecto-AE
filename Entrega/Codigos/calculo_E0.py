from ase.build import molecule
from ase.io import read, write
from ase import Atoms
from gpaw import GPAW
from gpaw import Mixer, MixerSum, MixerDif, FermiDirac


molecule = read("opt2.traj@0")
c = molecule.get_cell()

for name in ['Fe']:
    system = Atoms(name)
    system.set_cell(c)
    system.center()
    hund = True
    calc = GPAW(mode='fd', h=0.18, hund=hund, 
                txt=f'gpaw-{name}.txt', xc="PBE",
                mixer=MixerSum(0.02, 5, 100),
                occupations=FermiDirac(0.0, fixmagmom=True)
                )
    system.calc = calc

    energy = system.get_potential_energy()
    write(f'{name}.xyz', system)
    print(name, energy)


