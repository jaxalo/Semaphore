from program.Waiter import Waiter
from program.Take import Take
from program.Release import Release


class Process:

    def __init__(self, partial_process, semaphores, waiting_process, process_type, identifier):
        self.partial_process = partial_process
        self.semaphores = semaphores
        self.process_type = process_type
        self.identifier = identifier
        self.critical_section = None
        self.instruction_list = self.build_instruction_list(partial_process, process_type, waiting_process)
        self.actual_instruction = 0
        self.blocked = False

    def build_instruction_list(self, partial_process, process_type, waiting_process):
        key_epilog = ''
        key_prolog = ''
        instruction_list = list()

        if process_type == 'L':
            key_epilog = '%EL'
            key_prolog = '%PL'
        elif process_type == 'E':
            key_epilog = '%EE'
            key_prolog = '%PE'
        elif process_type == 'X':
            key_epilog = '%EX'
            key_prolog = '%PX'

        prolog = partial_process.get_partial_prog()[key_prolog]
        epilog = partial_process.get_partial_prog()[key_epilog]

        # building prolog
        for prolog_clause in prolog:
            instruction = None
            if prolog_clause[0] == 'P':
                instruction = Take(self.semaphores[prolog_clause[2]])
            elif prolog_clause[0] == 'V':
                instruction = Release(waiting_process, self.semaphores[prolog_clause[2]])
            instruction_list.append(instruction)

        # building critical_section
        self.critical_section = Waiter()
        instruction_list.append(self.critical_section)

        # building epilog
        for epilog_clause in epilog:
            instruction = None
            if epilog_clause[0] == 'P':
                instruction = Take(self.semaphores[epilog_clause[2]])
            elif epilog_clause[0] == 'V':
                instruction = Release(waiting_process, self.semaphores[epilog_clause[2]])
            instruction_list.append(instruction)

        return instruction_list

    def execute(self):
        done, blocked, blocking_semaphore = self.instruction_list[self.actual_instruction].execute()

        if done:
            self.actual_instruction += 1
            self.blocked = blocked
        else:
            self.blocked = blocked

        return done, blocked, blocking_semaphore

    def is_blocked(self):
        return self.blocked

    def is_in_critical_section(self):
        return type(self.instruction_list[self.actual_instruction]) is Waiter

    def is_finished_process(self):
        return self.actual_instruction == len(self.instruction_list)

    def get_actual_instruction(self):
        return self.actual_instruction

    def __str__(self):
        res = str(self.identifier) + '  ' + self.process_type
        for instruction in self.instruction_list:
            res += instruction.__str__() + '\n'
        return res
