from yogi import tokens

pila: list[int] = []

for i in tokens(int):
    print(i)
    if i.isnumeric():
        pila.append(float(i))
    else:
        x, y = pila.pop(), pila.pop()
        if i == "+":
            pila.append(x+y)
        elif i == "-":
            pila.append(x-y)
        elif i == "*":
            pila.append(x*y)
        else:
            assert False
print(pila.pop())

