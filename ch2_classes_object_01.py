class Greetings:
    def __init__(self, default_name='World'):
        self.default_name = default_name

    def greet(self, name):
        return f'Hello {name if name else self.default_name}'


c = Greetings()
print(c.greet(''))
