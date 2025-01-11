import heapq
from yogi import tokens, read

def print_mesures(cua) -> None:
    if cua:
        print(
            f"minimum: {cua[0]}, maximum: {max(cua)}, average: {sum(cua)/len(cua):.4f}")
    else:
        print("no elements")

def main() -> None:
    cua = []
    for i in tokens(str):
        if i == "number":
            n = read(int)
            heapq.heappush(cua, n)
        elif i == "delete":
            if cua:
                heapq.heappop(cua)
        else:
            assert False
        print_mesures(cua)


main()
