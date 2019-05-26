from program.PartialProcess import PartialProcess
from program.Process import Process
from program.Scheduler import Scheduler


partial_process = PartialProcess()
file_path = '../' + 'test' + '/' + 'Test1.txt'
with open(file_path) as fp:
    partial_process.build(fp)

scheduler = Scheduler(partial_process)
scheduler.run_simulation()