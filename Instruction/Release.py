import random

from Instruction.Instruction import Instruction


# V(Semaphore)

class Release(Instruction):

    def execute(self):
        self.semaphore.increment()
        if self.semaphore.get_value() <= 0:
            next_process = random.choice(self.waiting_processes[self.semaphore.get_id()])
            next_process.unblock_process()

    def __str__(self):
        return ' Release ' + self.semaphore.__str__()
