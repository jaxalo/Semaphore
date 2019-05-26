from collections import defaultdict

from program.Semaphore import Semaphore
from program.Process import Process
from program.PartialProcess import PartialProcess
from Instruction.Take import Take
from Instruction.Release import Release
from Instruction.Waiter import Waiter


def test_waiter():
    instr_take = Waiter()
    print(instr_take.execute())
    print(instr_take.get_executed_so_far())
    print()

    print(instr_take.execute())
    print(instr_take.get_executed_so_far())
    print()

    print(instr_take.execute())
    print(instr_take.get_executed_so_far())
    print()

    print(instr_take.execute())
    print(instr_take.get_executed_so_far())
    print()


def test_take():
    watiting_processes = defaultdict(list)
    sem_list = {'L': Semaphore(2, 'L'),
                'E': Semaphore(1, 'E')}

    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    process1 = Process(partial_process, sem_list, watiting_processes, 'L', 1)
    print(process1)

    take1 = Take(sem_list['E'], watiting_processes, process1)
    take2 = Take(sem_list['E'], watiting_processes, process1)

    print(take1.execute())
    print(watiting_processes['E'])
    print(take2.execute())
    print(watiting_processes['E'])
    print(take1.execute())


def test_release():
    waiting_processes = defaultdict(list)
    sem_list = {'L': Semaphore(2, 'L'),
                'E': Semaphore(1, 'E')}

    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    process1 = Process(partial_process, sem_list, waiting_processes, 'L', 1)
    print(process1)

    take1 = Take(sem_list['E'], waiting_processes, process1)
    take2 = Take(sem_list['E'], waiting_processes, process1)

    release1 = Release(sem_list['E'], waiting_processes)

    print(take1.execute())
    print(take2.execute())
    print(release1.execute())
    print(take2.execute())


test_release()
