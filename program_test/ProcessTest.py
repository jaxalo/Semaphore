from program.PartialProcess import PartialProcess
from program.Process import Process
from program.Scheduler import Scheduler


def test_init_process():
    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    scheduler = Scheduler(partial_process)
    waiting_process = [i for i in range(5)]
    process1 = Process(partial_process, scheduler.get_semaphores(), waiting_process, 'L', 1)
    print(process1)
    process2 = Process(partial_process, scheduler.get_semaphores(), waiting_process, 'E', 1)
    print(process2)


def test_executing_process():
    partial_process = PartialProcess()
    file_path = '../' + 'test' + '/' + 'Test1.txt'
    with open(file_path) as fp:
        partial_process.build(fp)

    scheduler = Scheduler(partial_process)
    process1 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'E', 1)
    print(process1)
    process2 = Process(partial_process, scheduler.get_semaphores(), scheduler.get_waiting_processes(), 'E', 2)
    print(process2)
    print('start_simulation\n')

    # instr : 1
    print('instr : 1')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    print()

    # instr : 1
    print('instr : 1')
    print(process2.execute())
    print(process2.is_blocked())
    print(process2.get_actual_instruction())
    print()

    # instr : 1
    print('instr : 1')
    print(process2.execute())
    print(process2.is_blocked())
    print(process2.get_actual_instruction())
    print()

    # instr : 2
    print(' instr : 2')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    # VRAI
    print(process1.is_in_critical_section())
    print()

    # instr : 1
    print('instr : 1')
    print(process2.execute())
    print(process2.is_blocked())
    print(process2.get_actual_instruction())
    print()

    # instr : 3
    print('instr : 3')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    # VRAI
    print(process1.is_in_critical_section())
    print()

    # instr : 4
    print('instr : 4')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    # FAUX
    print(process1.is_in_critical_section())
    print()

    # instr : 5
    print('instr : 5')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    print(process1.is_finished_process())
    # FAUX
    print(process1.is_in_critical_section())
    print(scheduler.get_semaphores()['E'])
    print()

    # instr : 6
    print('instr : 6')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    print(process1.is_finished_process())
    print(scheduler.get_semaphores()['E'])
    print()

    # instr : 7
    print('instr : 7')
    print(process1.execute())
    print(process1.is_blocked())
    print(process1.get_actual_instruction())
    print(process1.is_finished_process())
    print(scheduler.get_semaphores()['E'])
    print()

    # instr : 1
    print('instr : 1')
    print(process2.execute())
    print(process2.is_blocked())
    print(process2.get_actual_instruction())
    print()


test_executing_process()
