class E25Interpreter:
    def __init__(self):
        self.variables = {}

    def run(self, program):
        tokens = program.split()
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "SET":
                var_name = tokens[i+1]
                var_value = tokens[i+2]
                self.variables[var_name] = var_value
            elif token == "PRINT":
                var_name = tokens[i+1]
                print(self.variables.get(var_name, "Undefined variable: " + var_name))

interpreter = E25Interpreter()
program = "SET x 10\nPRINT x"
interpreter.run(program)
