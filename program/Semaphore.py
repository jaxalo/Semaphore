class Semaphore:

    def __init__(self, init_value, identifier):
        self.value = init_value
        self.identifier = identifier

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

    def get_id(self):
        return self.identifier

    def __str__(self):
        return str(self.identifier) + ' ' + str(self.value)
