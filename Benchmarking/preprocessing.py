from pathlib import Path

def preprocessing(scriptPath, outputPath):
    # create output file
    outputFile = Path(outputPath + '/benchmarks.csv')
    outputFile.parent.mkdir(parents=True, exist_ok=True)
    Path(outputPath + '/Output').mkdir(parents=True, exist_ok=True)
    with open(outputFile, 'w') as f:
        f.write('bulkModulus,latticeConstant,defectFormationEnergy,runtime,memoryusage,exitStatus\n')
    # remove unneccessary lines
    with open(scriptPath, 'r') as f:
        lines = f.readlines()
    with open(scriptPath, 'w') as f:
        f.writelines(lines[0])
        f.writelines(lines[11:-1])
    with open(scriptPath, 'a') as f:
        f.write(f'''\
with open('./{outputFile}', 'a') as f:
    f.write(str(bulk_modulus) + ',' + str(lattice_constant) + ',' + str(defectFormationEnergy) + ',')

EOF
''')


preprocessing('./BenchmarkingCandidates/2FeVac/candidate_workflow_4_GpawSphinx.sh', './Benchmarking/Results/2FeVac/GpawSphinx')
preprocessing('./BenchmarkingCandidates/2FeVac/candidate_workflow_6_SphinxSphinx.sh', './Benchmarking/Results/2FeVac/SphinxSphinx')
preprocessing('./BenchmarkingCandidates/2FeVac/candidate_workflow_1_SphinxGpaw.sh', './Benchmarking/Results/2FeVac/SphinxGpaw')
preprocessing('./BenchmarkingCandidates/2FeVac/candidate_workflow_2_GpawGpaw.sh', './Benchmarking/Results/2FeVac/GpawGpaw')
