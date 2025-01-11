from yogi import tokens

def work(n: int) -> None:
    stack = [n]
    while stack:
        n = stack.pop()
        if n > 0:
            print('', n, end='')
            stack.append(n - 1)
            stack.append(n - 1)

def main() -> None:
    for n in tokens(int):
        work(n)
        print() 


main()