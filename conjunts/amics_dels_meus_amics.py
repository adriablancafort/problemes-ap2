from yogi import tokens, read


def main() -> None:
    n = read(int)  # nombre persones
    m = read(int)  # nombre relacions d’amistat directes

    friends = [set() for _ in range(n)]

    for _ in range(m):
        x, y = read(int), read(int)
        friends[x].add(y)
        friends[y].add(x)

    persons = tokens(int)

    for p in persons:
        direct_friends = friends[p]

        friends_of_friends = set()
        for friend in direct_friends:
            friends_of_friends.update(friends[friend])

        friends_of_friends.discard(p)
        friends_of_friends.difference_update(direct_friends)

        print(len(direct_friends) + len(friends_of_friends))


main()
