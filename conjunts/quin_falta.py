from yogi import read, tokens

def quin_falta(c: set[int], n: int) -> int:
    """
    Retorna el número que falta en el conjunt.
    """
    s = {i for i in range(1, n+1)}
    return (s - c).pop()

def main() -> None:
    for n in tokens(int):
        k = read(int)
        c = {read(int) for _ in range(k)}
        print(quin_falta(c, n))

if __name__ == "__main__":
    main()