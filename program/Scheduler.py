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
        self.waiting_process = defaultdict(list)
        self.processes = self.build_processes()
        self.nb_finished_process = 0
        # stock result in a triplet format (L, E, X)
        self.process_in_critical_solution = set()
        # debug purpose
        self.index_scenario = -1

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
        self.init_waiting_process()
        partial_concurrent_proc = set()
        while not self.is_end_simualtion() and not self.is_deadlock():
            sem_id, process = self.get_unblocked_process_from_waiting_list()
            if process is None:
                process = random.choice(self.get_unblocked_process())
                # process = self.get_next_scenario()
            else:
                # erase it from waiting_list
                self.waiting_process[sem_id].remove(process)

            # if we are here that means we found one
            # print('debut boucle')
            # process.debug()
            nb_instruction_to_exec = random.randint(1, Scheduler.NB_INSTRUCTION_TO_EXEC)
            # if the process is blocked it will stay in the same instruction
            for i in range(nb_instruction_to_exec):
                if not process.is_blocked():
                    process.execute()
                if not process.is_finished_process() and process.is_in_critical_section():
                    partial_concurrent_proc.add(process.get_full_id())
                    self.add_result(partial_concurrent_proc)
                if process.quit_critical_section():
                    partial_concurrent_proc.remove(process.get_full_id())
                    self.add_result(partial_concurrent_proc)

            if process.is_finished_process():
                self.processes.remove(process)
                self.nb_finished_process += 1

            # print('fin boucle')
            # process.debug()

        # print('done')
        # for elem in self.process_in_critical_solution:
        #   print(elem)

    def run_simulations(self):
        for _ in range(self.nb_simulation):
            self.semaphores = self.build_semaphores()
            self.processes = self.build_processes()
            self.run_simulation()

    def is_end_simualtion(self):
        return self.nb_finished_process == self.nb_read + self.nb_execute + self.nb_write

    def get_semaphores(self):
        return self.semaphores

    def get_waiting_processes(self):
        return self.waiting_process

    def get_str_result(self):
        res = 'L ,E , X\n'
        res += '---------\n'
        sorted_res = self.process_in_critical_solution
        # sorted_res = sorted(list(self.process_in_critical_solution))
        for triplet in sorted_res:
            res += str(triplet) + '\n'
        return res

    def init_waiting_process(self):
        for sem_id, process_list in self.waiting_process.items():
            process_list.clear()
        self.nb_finished_process = 0

    def get_unblocked_process_from_waiting_list(self):
        for sem_id, process_list in self.waiting_process.items():
            if process_list and not process_list[0].is_blocked():
                return sem_id, process_list[0]
        return None, None

    def add_result(self, partial_concurrent_proc):
        # (L, E , X)
        res = [0, 0, 0]
        for pcp in partial_concurrent_proc:
            if pcp[0] == 'L':
                res[0] += 1
            elif pcp[0] == 'E':
                res[1] += 1
            elif pcp[0] == 'X':
                res[2] += 1
        self.process_in_critical_solution.add((res[0], res[1], res[2]))

    def is_deadlock(self):
        for process in self.processes:
            if not process.is_blocked():
                return False
        return True

    def get_next_scenario(self):
        scenario = [0, 0, 0]
        self.index_scenario = (1 + self.index_scenario) % (len(scenario))
        return self.processes[scenario[self.index_scenario]]

    def get_unblocked_process(self):
        processes = []
        for process in self.processes:
            if not process.is_blocked():
                processes.append(process)
        return processes
