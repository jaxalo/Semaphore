from Instruction.Instruction import Instruction



# V(Semaphore)

class Release(Instruction):

    def execute(self):
        # return blocked
        self.semaphore.increment()
        if self.waiting_processes[self.semaphore.get_id()]:
            next_process = self.waiting_processes[self.semaphore.get_id()][0]
            next_process.unblock_process()
            self.reschedule = True
        return False

    def __str__(self):
        return ' Release ' + self.semaphore.__str__()
