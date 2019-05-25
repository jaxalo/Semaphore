from program.Instruction import Instruction


class Waiter(Instruction):
    NB_INSTRUCTION = 3

    def __init__(self):
        self.nb_instruction = Waiter.NB_INSTRUCTION
        self.executed_so_far = 0

    def execute(self):
        # return done and blocked and blocking semaphore
        if self.executed_so_far == self.nb_instruction - 1:
            return True, False, None
        else:
            self.executed_so_far += 1
            return False, False, None

    def get_executed_so_far(self):
        return self.executed_so_far
