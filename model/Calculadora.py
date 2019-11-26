class Calculadora:

    def __init__(self):
        self.__accumulator = 0
        self.__history = [0]

    def clear(self):
        self.__accumulator = 0

    def getTotal(self):
        return self.__accumulator

    def multiply(self, operator):
        self.__memorize()
        self.__accumulator = self.__accumulator * operator

    def sub(self, operator):
        self.__memorize()
        self.__accumulator = self.__accumulator - operator

    def sum(self, operator):
        self.__memorize()
        self.__accumulator = self.__accumulator + operator

    def divide(self, operator):
        self.__memorize()

        if operator == 0:
            print("Erro! Divisão por zero!!")
        self.__accumulator = self.__accumulator / operator

    def memorize(self):
        """ Memoriza o último valor do acumulador para poder retroceder """
        self.__history.append(self.__accumulator)

    def remember(self):
        """ Relembra o último resultado """
        self.__accumulator = self.__history.pop()

    def parse(self, text):
        tokens = text.split(" ")
        result = []
        stack = []
        precedence = {'+':1, '-':1, '*':2, '/':2, '(':4, ')': 4}
        for token in tokens:
            if token not in operators:
                print("OPERANDO!", token)
                result.push(float(token))
            else:
                if operators.index(token) < operators.index(stack[-1]) or stack[-1] == '(':
                    print("Empilhando", token)
                    stack.push(token)
                else:
                    for op in stack:
                        if operators.index(token) >= operators.index(op) and op != '(':
