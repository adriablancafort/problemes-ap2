from yogi import read, tokens


def main() -> None:
    n = read(int)
    white: dict[str, list[str]] = {}
    black: dict[str, list[str]] = {}
    for _ in range(n):
        white_player, black_player = input().split()
        if white_player not in white:
            white[white_player] = []
        if black_player not in black:
            black[black_player] = []
        white[white_player].append(black_player)
        black[black_player].append(white_player)

    for query1 in tokens(str):
        query2 = read(str)
        if query2 == "?":
            print(f"{query1} has played white against:")
            for player in sorted(white[query1]):
                print(player)
        elif query1 == "?":
            print(f"{query2} has played black against:")
            for player in sorted(black[query2]):
                print(player)
        print("")


if __name__ == "__main__":
    main()
