# Text for menu, dictionary of commands according to vendor
class MenuItem:
    def __init__(self, text, vendorfuncdict=None):
        self.display = text
        self.func = vendorfuncdict

# String to be formatted for output, inputs required for the fields
class UserInput:
    def __init__(self, output, *inputs):
        self.text = output
        self.input = list(inputs)
        self.output = []

    def run(self):
        print self.input
        for item in self.input:
            self.output.append(raw_input(item))
        return self.text.format(*self.output)
