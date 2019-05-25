import random

from program.Instruction import Instruction
from program.Semaphore import Semaphore


# V(Semaphore)

class Release(Instruction):

    def __init__(self, waiting_process, semaphore):
        self.next_process = None
        self.waiting_process = waiting_process
        self.semaphore = semaphore

    def execute(self):
        # return done and blocked and blocking semaphore
        if not self.waiting_process:
            self.semaphore.increment()
            self.next_process = None
        else:
            self.next_process = random.choice(self.waiting_process)
        return True, False, None

    def get_next_process(self):
        return self.next_process
