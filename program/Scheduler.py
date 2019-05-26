import random
from collections import defaultdict

from program.Semaphore import Semaphore
from program.Process import Process


class Scheduler:

    NB_INSTRUCTION_TO_EXEC = 7

    def __init__(self, partial_process):
        self.partial_process = partial_process
        self.semaphores = self.build_semaphores()
        self.nb_read, self.nb_write, self.nb_execute, self.nb_simulation = self.build_params()
        print(self.nb_read, self.nb_write, self.nb_execute, self.nb_simulation)
        self.waiting_process = defaultdict(set)
        self.processes = self.build_processes()
        self.nb_finished_process = 0

        print('debug')
        for process in self.processes:
            print()
            print(process)
            print()
        print('end')

    def build_semaphores(self):
        init_clauses = self.partial_process.get_partial_prog()['%IN']
        semaphores = dict()
        for init_clause in init_clauses:
            temp = init_clause.split('=')
            identifier = temp[0]
            init_value = int(temp[1])
            semaphore = Semaphore(init_value, identifier)
            semaphores[identifier] = semaphore
        return semaphores

    def build_params(self):
        nb_read, nb_write, nb_execute, nb_simulation = 0, 0, 0, 0
        params = self.partial_process.get_partial_prog()['%PA']

        for assignment in params:
            temp = assignment.split('=')
            if temp[0] == 'L':
                nb_read = int(temp[1])
            elif temp[0] == 'E':
                nb_write = int(temp[1])
            elif temp[0] == 'X':
                nb_execute = int(temp[1])
            elif temp[0] == 'N':
                nb_simulation = int(temp[1])

        return nb_read, nb_write, nb_execute, nb_simulation

    def build_processes(self):
        processes = list()

        # building reading process
        for i in range(self.nb_read):
            process = Process(self.partial_process, self.semaphores, self.waiting_process, 'L', i)
            processes.append(process)

        # building writing process
        for i in range(self.nb_read, self.nb_read + self.nb_write):
            process = Process(self.partial_process, self.semaphores, self.waiting_process, 'E', i)
            processes.append(process)

        # building executing process
        for i in range(self.nb_read + self.nb_write, self.nb_read + self.nb_write + self.nb_execute):
            process = Process(self.partial_process, self.semaphores, self.waiting_process, 'X', i)
            processes.append(process)

        return processes

    def run_simulation(self):
        while not self.is_end_simualtion():
            #check si le premie de la liste est bloque s'il est tu en choisi un au hasard
            #sinon c'est lui qu'on execute
            #vider simulation
            process = random.choice(self.processes)
            # Search for a un_blocked process
            while process.is_blocked():
                process = random.choice(self.processes)
            # if we are here that means we found one
            nb_instruction_to_exec = random.randint(1, Scheduler.NB_INSTRUCTION_TO_EXEC)

            # if the process is blocked it will stay in the same instruction
            for i in range(nb_instruction_to_exec):
                done, blocked, blocking_semaphore = process.execute()
                if blocking_semaphore is not None:
                    self.waiting_process[blocking_semaphore.get_id()].add(process)

            # check if the process is done to kill it
            if process.is_finished_process():
                self.processes.remove(process)

    def is_end_simualtion(self):
        return self.nb_finished_process == self.nb_read + self.nb_execute + self.nb_write

    def get_semaphores(self):
        return self.semaphores
