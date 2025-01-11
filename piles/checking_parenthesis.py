import yogi

def check_parenthesis(expression):
    stack = []
    for token in expression:
        if token in "([":
            stack.append(token)
        elif token in ")]":
            if not stack:
                return False
            if token == ')' and stack[-1] != '(':
                return False
            if token == '}' and stack[-1] != '{':
                return False
            if token == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return not stack

while 

for line in yogi.read:

    if check_parenthesis(line.strip()):
        print(f"{line} is correct")
    else:
        print(f"{line} is incorrect")
