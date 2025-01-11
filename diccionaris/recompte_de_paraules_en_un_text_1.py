from yogi import tokens


def main() -> None:
    paraules = dict()
    for paraula in tokens(str):
        paraula = paraula.lower()
        paraules[paraula] = paraules.get(paraula, 0) + 1

    paraules_ordenades = sorted(paraules.items())

    for paraula, count in paraules_ordenades:
        print(f"{paraula} {count}")


main()
