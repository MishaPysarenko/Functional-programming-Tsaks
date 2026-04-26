class Some:
    def __init__(self, value):
        self.value = value

    def map(self, func):
        return Some(func(self.value))


class Nothing:
    def map(self, func):
        return self