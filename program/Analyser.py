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
        self.check_init_format(process)
        self.check_param_format(process)
        print('done analysing syntax')


    def analyse_semantic(self, process):
        print('start analysing semantic')
        self.check_all_keywords_present(process)
        print('done analysing semantic')

    def check_all_keywords_present(self, process):
        for key in process.get_mandatory_keywords():
            if key not in process.get_partial_prog():
                self.check_syntax = False
                self.syntax_errors.append('{} is not present'.format(key))
                return

    def check_init_format(self, process):
        init_clauses = process.get_partial_prog()['%IN']
        if init_clauses:
            for init_clause in init_clauses:
                if not re.search(r'[A-Z]=[0-9]+', init_clause):
                    self.check_syntax = False
                    self.syntax_errors.append('{} not in the right %IN format'.format(init_clause))

    def check_param_format(self, process):
        param_clauses = process.get_partial_prog()['%PA']
        seens = list()
        if param_clauses:
            for param_clause in param_clauses:
                if not re.search(r'[A-Z]=[0-9]+', param_clause):
                    self.check_syntax = False
                    self.syntax_errors.append('{} not in the right %PA format'.format(param_clause))
                else:
                    seens.append(param_clause[0])
            print(seens)
            for seen in seens:
                if seen not in process.get_params():
                    self.check_syntax = False
                    self.syntax_errors.append('{} not in the right %PA format'.format(seen))
                else:
                    return

    def is_correct(self):
        return self.check_syntax and self.check_semantic

    def get_errors(self):
        error = '\n'.join(self.syntax_errors) + '\n'
        error += '\n'.join(self.semantic_errors) + '\n'
        return error
