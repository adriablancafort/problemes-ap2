import fileinput

def reverse_polish_expression(expression):
    stack = []
    for token in expression.split():
        if token in "+-*":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]


for line in fileinput.input():
    print(reverse_polish_expression(line.strip()))
