import subprocess

def benchmarking(workflowPath, outputPath):
    print(f'Runnning Workflow {workflowPath}...')
    result = subprocess.run(['/usr/bin/time', '-f', '%e,%M,%x', '-o', outputPath, '-a', workflowPath], capture_output=True, text=True)
    print(f'Finished with exit status: {result.returncode}\n{result.stderr}')


benchmarking('./BenchmarkingCandidates/2FeVac2Relax/candidate_workflow_19_GpawSphinx.sh', './Benchmarking/Results/2FeVac2Relax/GpawSphinx/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/2FeVac2Relax/candidate_workflow_1_SphinxSphinx.sh', './Benchmarking/Results/2FeVac2Relax/SphinxSphinx/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/2FeVac2Relax/candidate_workflow_22_SphinxGpaw.sh', './Benchmarking/Results/2FeVac2Relax/SphinxGpaw/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/2FeVac2Relax/candidate_workflow_18_GpawGpaw.sh', './Benchmarking/Results/2FeVac2Relax/GpawGpaw/benchmarks.csv')
