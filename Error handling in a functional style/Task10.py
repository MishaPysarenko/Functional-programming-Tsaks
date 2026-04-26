class Ok:
    def __init__(self, value):
        self.value = value

    def map(self, func):
        return Ok(func(self.value))

    def flat_map(self, func):
        return func(self.value)


class Error:
    def __init__(self, message):
        self.message = message

    def map(self, func):
        return self

    def flat_map(self, func):
        return self