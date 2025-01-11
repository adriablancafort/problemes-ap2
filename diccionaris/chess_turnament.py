from yogi import read, tokens


def main() -> None:
    n = read(int)
    players = {}
    for _ in range(n):
        player = read(str)
        players[player] = [0, 0, 0]
    for player1 in tokens(str):
        player2, result = read(str), read(str)
        if result == '1-0':
            players[player1][0] += 1 
            players[player2][2] += 1
        elif result == '0-1':
            players[player1][2] += 1 
            players[player2][0] += 1
        elif result == "1/2-1/2":
            players[player1][1] += 1
            players[player2][1] += 1

    players_sorted = sorted(players.items(), key=lambda x: x[0])
    for player, (wins, draws, losses) in players_sorted:
        print(player, wins, draws, losses)


if __name__ == "__main__":
    main()
