def cartesian_product(a: set[int], b: set[int]) -> set[tuple[int, int]]:
    return [(i, j) for i in a for j in b]


def main() -> None:
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(cartesian_product(a, b))

main()
