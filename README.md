# CMS_Benchmarking
---

This repository was created as part of the master thesis "Automated Composition and Benchmarking of Data Analysis Workflows in Computational Materials Science".

The project includes a domain model for the defect formation energy workflow as well as implementations for the individual workflow steps. The model can be used to generate workflow candidates with the Automated Pipeline Explorer (APE). Additionally, workflows were chosen as benchmarking candidates:

- FeVac: workflows calculating the defect formation energy of a 16-atom B2-FeAl structure with a single iron vacancy
- 2FeVac: workflows calculating the defect formation energy of a 54-atom B2-FeAl structure with a double iron vacancy
- 2FeVac2Relax: workflows calculating the defect formation energy of a 54-atom B2-FeAl structure with a double iron vacancy and an additional relaxation step

The candidates were benchmarked using consistency, defect formation energy, bulk modulus, lattice constant, peak memory and runtime as criteria.

### License
---
This project is licensed under a [MIT license](/LICENSE.txt).

### Citation
---
You can cite this project using the metadata in the [Citation.cff](/CITATION.cff) file.