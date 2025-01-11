from yogi import read, tokens


def main() -> None:
    for n in tokens(int):
        k = read(int)
        paraules: dict[str, int] = {}
        for _ in range(n):
            paraula = read(str)
            if paraula in paraules:
                paraules[paraula] += 1
            else:
                paraules[paraula] = 1
        paraules_ord = sorted(paraules.items(), key=lambda x: (-x[1], x[0]))

        for i in range(k):
            print(paraules_ord[i][0])
        print("----------")


main()
