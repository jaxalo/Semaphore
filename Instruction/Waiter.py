from Instruction.Instruction import Instruction


class Waiter(Instruction):
    NB_INSTRUCTION = 2

    def __init__(self, process):
        self.nb_instruction = Waiter.NB_INSTRUCTION
        self.executed_so_far = 0
        self.process = process

    def execute(self):
        # return blocked
        self.process.unblock_process()
        if self.executed_so_far == self.nb_instruction:
            return False
        else:
            self.executed_so_far += 1
            return True

    def get_executed_so_far(self):
        return self.executed_so_far

    def __str__(self):
        return 'Waiter ' + str(self.executed_so_far)
