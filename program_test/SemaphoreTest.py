from collections import defaultdict

from program.Semaphore import Semaphore
from program.Process import Process
from program.PartialProcess import PartialProcess
from program.Scheduler import Scheduler
from Instruction.Take import Take
from Instruction.Release import Release
from Instruction.Waiter import Waiter


def test_waiter():
    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    scheduler = Scheduler(partial_process)
    process1 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'E', 1)

    process1.instruction_list.clear()
    process1.instruction_list.append(Waiter(process1))

    print()
    print('init')
    process1.debug()
    print('first instr')
    process1.execute()
    process1.debug()
    print('second inst')
    process1.execute()
    process1.debug()
    print('end inst')
    # process1.execute()
    # process1.debug()


def test_take():
    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    scheduler = Scheduler(partial_process)
    process1 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'L', 0)
    process2 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'L', 1)
    process3 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'E', 2)

    '''
    % PL  
    P(L)
    % EL
    V(L)
    '''

    '''
    %PE
    P(E)
    P(L)
    %EE
    V(L)
    V(E)
    '''

    Waiter.NB_INSTRUCTION = 1
    print('init')
    process1.debug()
    process2.debug()
    process3.debug()
    print('instr1 de L0')
    process1.execute()
    process1.debug()
    print('instr1 de L1')
    process2.execute()
    process2.debug()
    print('instr2 de L0')
    process1.execute()
    process1.debug()
    print('instr1 de E2')
    process3.execute()
    process3.debug()
    print('instr2 de E2 semaphore bloque')
    process3.execute()
    process3.debug()
    print('instr2 de E2 semaphore bloque')
    process3.execute()
    process3.debug()


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


test_take()
