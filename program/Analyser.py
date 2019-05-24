import re


class Analyser:

    def __init__(self):
        self.check_syntax = True
        self.check_semantic = True
        self.syntax_errors = list()
        self.semantic_errors = list()

    def analyse_syntax(self, process):
        print('start analysing syntax')
        self.check_all_keywords_present(process)
        self.check_dummy_keyword(process)
        if not self.syntax_errors:
            self.check_init_format(process)
            self.check_param_format(process)
            self.check_prolog_epilog(process)
        print('done analysing syntax')

    def analyse_semantic(self, process):
        if self.check_syntax:
            print('start analysing semantic')
            self.check_undeclared_semaphore(process)
            print('done analysing semantic')
        else:
            print('syntax error found so no syntax analysis done')

    def check_all_keywords_present(self, process):
        for key in process.get_mandatory_keywords():
            if key not in process.get_partial_prog():
                self.check_syntax = False
                self.syntax_errors.append('{} is not present'.format(key))
                return

    def check_dummy_keyword(self, process):
        for key in process.get_partial_prog().keys():
            if key not in process.get_keywords():
                self.check_syntax = False
                self.syntax_errors.append('{} is not a keyword'.format(key))
                return

    def check_init_format(self, process):
        init_clauses = process.get_partial_prog()['%IN']
        if init_clauses:
            for init_clause in init_clauses:
                if not re.search(r'[A-Z]=[0-9]+', init_clause):
                    self.check_syntax = False
                    self.syntax_errors.append('{} not in the right %IN format'.format(init_clause))
                    return

    def check_param_format(self, process):
        param_clauses = process.get_partial_prog()['%PA']
        if param_clauses:
            for param_clause in param_clauses:
                if not re.search(r'[L|E|N|X]=[0-9]+', param_clause):
                    self.check_syntax = False
                    self.syntax_errors.append('{} not in the right %PA format'.format(param_clause))
                    return

    def check_prolog_epilog(self, process):
        prog_clauses = process.get_keyprog()
        partial_prog = process.get_partial_prog()
        for prog_clause in prog_clauses:
            if prog_clause in partial_prog:
                for statement in partial_prog[prog_clause]:
                    # Empty or respecting regex
                    if not re.search(r'[P|V]\(([A-Z])\)', statement) or not statement:
                        self.check_syntax = False
                        self.syntax_errors.append('{} not in the right {}'.format(statement, prog_clause))
                        return

    def check_undeclared_semaphore(self, process):
        semaphores = []
        # get declared semaphores
        for assignment in process.get_partial_prog()['%IN']:
            semaphores.append(assignment[0])

        # check if the semaphores in the init are present in all the epilogs and prologs
        prog_clauses = process.get_keyprog()
        partial_prog = process.get_partial_prog()
        for prog_clause in prog_clauses:
            if prog_clause in partial_prog:
                for statement in partial_prog[prog_clause]:
                    # Could do better to get the semaphore between bracket
                    semaphore = statement[2]
                    if semaphore not in semaphores:
                        self.check_semantic = False
                        self.semantic_errors.append('undeclared semaphore {}'.format(semaphore))
                        return

    def is_correct(self):
        return self.check_syntax and self.check_semantic

    def get_errors(self):
        error = '\n'.join(self.syntax_errors) + '\n'
        error += '\n'.join(self.semantic_errors) + '\n'
        return error
