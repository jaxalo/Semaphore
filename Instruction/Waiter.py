from Instruction.Instruction import Instruction


class Waiter(Instruction):
    NB_INSTRUCTION = 40

    def __init__(self, process):
        self.nb_instruction = Waiter.NB_INSTRUCTION
        self.executed_so_far = 0
        self.process = process

    def execute(self):
        if self.executed_so_far != self.nb_instruction:
            self.executed_so_far += 1

    def get_executed_so_far(self):
        return self.executed_so_far

    def is_done(self):
        return self.executed_so_far == self.nb_instruction

    def __str__(self):
        return 'Waiter ' + str(self.executed_so_far)
