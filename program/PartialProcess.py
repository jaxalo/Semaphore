import json


class PartialProcess:

    def __init__(self):
        self.partial_prog = dict()
        self.keywords = ['%IN', '%PA', '%PL', '%EL', '%PE', '%EE', 'EX', 'PX', '%FI']
        self.keyparams = ['L', 'E', 'X', 'N']

    def build(self, file):
        lines = file.readlines()
        nb_lines = len(lines)
        i = 0
        temp = list()
        self.partial_prog = dict()

        while i < nb_lines:
            line = lines[i].rstrip('\n')
            if line.startswith('%'):
                current_key_word = line
                i = i + 1
                while i < nb_lines:
                    if not lines[i].startswith('#') and lines[i].strip():
                        temp.append(lines[i].rstrip('\n'))
                    i = i + 1
                    if lines[i].startswith('%'):
                        break
                self.partial_prog[current_key_word] = temp.copy()
                temp.clear()
            else:
                i = i + 1

        return self.partial_prog

    def get_partial_prog(self):
        return self.partial_prog

    def get_keywords(self):
        return self.keywords

    def get_params(self):
        return self.keyparams

    def get_mandatory_keywords(self):
        return ['%IN', '%PA', '%FI']

    def serialize(self):
        return str(json.dumps(self.partial_prog, indent=4))
