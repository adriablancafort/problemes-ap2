from yogi import tokens, read


def main() -> None:
    players_inside: dict[str, int] = {}
    for player in tokens(str):
        action = read(str)
        if action == "enters":
            if player in players_inside:
                print(f"{player} is already in the casino")
            else:
                players_inside[player] = 0
        if action == "wins":
            quantity = read(int)
            if player in players_inside:
                players_inside[player] += quantity
            else:
                print(f"{player} is not in the casino")

        if action == "leaves":
            if player in players_inside:
                quantity = players_inside[player]
                print(f"{player} has won {quantity}")
                players_inside.pop(player)
            else:
                print(f"{player} is not in the casino")


    print("----------")
    players_inside_sorted = sorted(players_inside.items(), key=lambda x: (-x[1], x[0]))
    for i in range(len(players_inside_sorted)):
        player_i, quantity_i = players_inside_sorted[i][0], players_inside_sorted[i][1]
        print(f"{player_i} is winning {quantity_i}")


if __name__ == "__main__":
    main()