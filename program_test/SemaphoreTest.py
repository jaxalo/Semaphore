from program.Semaphore import Semaphore
from program.Take import Take
from program.Release import Release
from program.Waiter import Waiter


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
    sem1 = Semaphore(2, 'A')
    take1 = Take(sem1)
    take2 = Take(sem1)

    print(take1.execute())
    print(take2.execute())
    print(take1.execute())


def test_release():
    sem1 = Semaphore(2, 'A')
    waiting = [1, 2, 4, 5]
    release1 = Release(waiting, sem1)
    print(release1.execute())
    print(release1.get_next_process())
    print(release1.execute())
    print(release1.get_next_process())
    waiting.clear()
    print(release1.execute())
    print(release1.get_next_process())
