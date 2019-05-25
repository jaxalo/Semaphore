from program.Instruction import Instruction
from program.Semaphore import Semaphore

#P(Semaphore)
class Take(Instruction):

    def __init__(self, semaphore):
        self.semaphore = semaphore

    def execute(self):
        # return done and blocked and blocking semaphore
        if self.semaphore.get_value() > 0:
            self.semaphore.decrement()
            return True, False, None
        elif self.semaphore.get_value() == 0:
            return False, True, self.semaphore

    def __str__(self):
        return 'Take ' + self.semaphore.__str__()
