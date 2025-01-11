import turtle
from yogi import read, tokens

def main() -> None:
    n = read(int)
    dic: dict[int] = {}
    i = 0
    for number in tokens(int):
        dic[i] = number
        i += 1
