def write(n):
    s = []
    for i in range(n, 0, -1):
        s.append(i)
    while s:
        top = s[-1]
        print('', top, end='')
        s.pop()
        if top > 1:
            for i in range(top - 1, 0, -1):
                s.append(i)

def main():
    while True:
        try:
            n = int(input())
            write(n)
            print()
        except EOFError:
            break

main()
