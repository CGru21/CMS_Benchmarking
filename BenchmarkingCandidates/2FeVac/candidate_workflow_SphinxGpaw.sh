#!/bin/bash
python - << EOF
from pyiron.project import Project
import math
# Create Project
project = Project(path='./Benchmarking/Results/2FeVac/SphinxGpaw/Output')

# Create Structure
originalStructure = project.create.structure.bulk('FeAl', crystalstructure='cesiumchloride', a=2.9, cubic=True)
originalStructure = originalStructure.repeat([3, 3, 3])

# Calculate chemical potential of Fe
bulk_Fe = project.create.structure.bulk('Fe', crystalstructure='bcc')
calc_potential_job = project.create.job.Gpaw('calc_potential', delete_existing_job=True)
calc_potential_job.structure = bulk_Fe
calc_potential_job.run()
chemPotential = calc_potential_job.output.energy_tot[0]

# Run Gpaw
calc_energy_og_job = project.create.job.Gpaw('calc_energy_og', delete_existing_job=True)
calc_energy_og_job.structure = originalStructure
calc_energy_og_job.run()
energyOriginal = calc_energy_og_job.output.energy_tot[0]

# Create Vacancy Fe
vacancyFe = originalStructure.copy()
del vacancyFe[0]

# Create Vacancy Fe
vacancyFe = vacancyFe.copy()
del vacancyFe[1]

# Relax Structure Sphinx
relax_job = project.create.job.Sphinx('relax_defect', delete_existing_job=True)
relax_job.structure = vacancyFe
relax_job.calc_minimize()
relax_job.run()
relaxedStructure = relax_job.get_structure()

# Run Gpaw
calc_energy_job = project.create.job.Gpaw('calc_energy_defect', delete_existing_job=True)
calc_energy_job.structure = relaxedStructure
calc_energy_job.run()
energyDefect = calc_energy_job.output.energy_tot[0]

# Calculate lattice constant and bulk modulus
reference_job = project.create.job.Gpaw('gpaw_job', delete_existing_job=True)
reference_job.structure = project.create.structure.bulk('FeAl', crystalstructure='cesiumchloride', a=2.9)
murn_job = project.create.job.Murnaghan('murn_job', delete_existing_job=True)
murn_job.ref_job = reference_job
murn_job.run()
bulk_modulus = murn_job.content['output/equilibrium_bulk_modulus']
lattice_constant = (murn_job.content['output/equilibrium_volume']) ** (1/3)

# Calculate defect formation energy
defectFormationEnergy = energyDefect - energyOriginal + 2*chemPotential

# Calculate defect concentration
k_B = 0.0000862
temp = 1000
concentration_defect = math.exp(-defectFormationEnergy/(k_B * temp))

with open('./Benchmarking/Results/2FeVac/SphinxGpaw/benchmarks.csv', 'a') as f:
    f.write(str(bulk_modulus) + ',' + str(lattice_constant) + ',' + str(defectFormationEnergy) + ',')

EOF
