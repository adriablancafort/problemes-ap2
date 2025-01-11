from typing import List
from yogi import read, tokens


def min_car_range(n: int, s: int, lengths: List[int]) -> int:
    left, right = max(lengths), sum(lengths)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        stops = 0
        total = 0

        for length in lengths:
            if total + length > mid:
                stops += 1
                total = length
            else:
                total += length

        if stops <= s:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def main() -> None:
    for n in tokens(int):
        s = read(int)
        lengths = [read(int) for _ in range(n)]
        print(min_car_range(n, s, lengths))


if __name__ == "__main__":
    main()
