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


preprocessing('./BenchmarkingCandidates/FeVac/candidate_workflow_26_GpawGpaw.sh', './Benchmarking/Results/FeVac/GpawGpaw')