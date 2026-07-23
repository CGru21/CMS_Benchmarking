import subprocess

def benchmarking(workflowPath, outputPath):
    print(f'Runnning Workflow {workflowPath}...')
    result = subprocess.run(['/usr/bin/time', '-f', '%e,%M,%x', '-o', outputPath, '-a', workflowPath], capture_output=True, text=True)
    print(f'Finished with exit status: {result.returncode}\n{result.stderr}')


#benchmarking('./BenchmarkingCandidates/2FeVac/candidate_workflow_4_GpawSphinx.sh', './Benchmarking/Results/2FeVac/GpawSphinx/benchmarks.csv')
#benchmarking('./BenchmarkingCandidates/2FeVac/candidate_workflow_6_SphinxSphinx.sh', './Benchmarking/Results/2FeVac/SphinxSphinx/benchmarks.csv')
#benchmarking('./BenchmarkingCandidates/2FeVac/candidate_workflow_1_SphinxGpaw.sh', './Benchmarking/Results/2FeVac/SphinxGpaw/benchmarks.csv')
#benchmarking('./BenchmarkingCandidates/2FeVac/candidate_workflow_2_GpawGpaw.sh', './Benchmarking/Results/2FeVac/GpawGpaw/benchmarks.csv')
