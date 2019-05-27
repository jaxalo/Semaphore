import json


class PartialProcess:

    def __init__(self):
        self.partial_prog = dict()
        self.keywords = ['%IN', '%PA', '%FI', '%PL', '%EL', '%PE', '%EE', '%EX', '%PX']

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
                        str_without_space = lines[i].strip().replace(' ', '')
                        temp.append(str_without_space)
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

    def get_keyprog(self):
        return self.keywords[3::]

    def get_mandatory_keywords(self):
        return ['%IN', '%PA', '%FI']

    def serialize(self):
        return str(json.dumps(self.partial_prog, indent=4))
