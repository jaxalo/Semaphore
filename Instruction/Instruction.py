class Instruction:

    def __init__(self, semaphore, waiting_processes, process=None):
        self.semaphore = semaphore
        self.waiting_processes = waiting_processes
        self.process = process
        self.reschedule = False

    def execute(self):
        raise NotImplementedError

    def get_reshecudule(self):
        return self.reschedule

    def __str__(self):
        res = "semaphore " + self.semaphore.__str__() + " \n"
        if self.process:
            res += " process : " + self.process.__str__()
