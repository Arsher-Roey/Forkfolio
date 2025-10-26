class InfixToPostfixConverter:
    def __init__(self):
        self.stack = []
        self.output = []

    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0

    def is_operator(self, c):
        return c in ['+', '-', '*', '/', '^']

    def convert(self, expression: str) -> str:
        self.stack = []
        self.output = []
        expression = expression.replace(" ", "")

        for token in expression:
            if token.isalnum():
                self.output.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
            elif self.is_operator(token):
                while (self.stack and 
                       self.precedence(self.stack[-1]) >= self.precedence(token)):
                    self.output.append(self.stack.pop())
                self.stack.append(token)

        while self.stack:
            self.output.append(self.stack.pop())

        return " ".join(self.output)