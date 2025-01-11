from yogi import tokens


def correct_expression(paraula: str) -> bool:
    pila: list[str] = []
    for i in paraula:
        if i in "([":
            pila.append(i)
        elif i == "]":
            if not pila or pila.pop() != "[":
                return False
        elif i == ")":
            if not pila or pila.pop() != "(":
                return False
    return pila == []


def main() -> None:
    for paraula in tokens(str):
        if correct_expression(paraula):
            print(f"{paraula} is correct")
        else:
            print(f"{paraula} is incorrect")


if __name__ == "__main__":
    main()
