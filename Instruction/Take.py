from Instruction.Instruction import Instruction


# P(Semaphore)
class Take(Instruction):

    def execute(self):
        '''
        blocked = False
        if self.semaphore.get_value() <= 0:
            self.waiting_processes[self.semaphore.get_id()].append(self.process)
            self.process.block_process()
            blocked = True
        else:
            self.semaphore.decrement()
        return blocked
        '''

        self.semaphore.decrement()
        if self.semaphore.get_value() < 0:
            self.process.block_process()
            self.waiting_processes[self.semaphore.get_id()].append(self.process)


    def __str__(self):
        return 'Take ' + self.semaphore.__str__()
