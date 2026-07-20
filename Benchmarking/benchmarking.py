import subprocess

def benchmarking(workflowPath, outputPath):
    print(f'Runnning Workflow {workflowPath}...')
    result = subprocess.run(['/usr/bin/time', '-f', '%e,%M,%x', '-o', outputPath, '-a', workflowPath], capture_output=True, text=True)
    print(f'Finished with exit status: {result.returncode}')


benchmarking('./BenchmarkingCandidates/FeVac/candidate_workflow_1_GpawSphinx.sh', './Benchmarking/Results/FeVac/GpawSphinx/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/FeVac/candidate_workflow_3_SphinxSphinx.sh', './Benchmarking/Results/FeVac/SphinxSphinx/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/FeVac/candidate_workflow_8_SphinxGpaw.sh', './Benchmarking/Results/FeVac/SphinxGpaw/benchmarks.csv')
benchmarking('./BenchmarkingCandidates/FeVac/candidate_workflow_26_GpawGpaw.sh', './Benchmarking/Results/FeVac/GpawGpaw/benchmarks.csv')
