from yogi import tokens


def main() -> None:
    words = set()
    for word in tokens(str):
        words.add(word.lower())
    
    sorted_words = sorted(words)
    for word in sorted_words:
        print(word)


main()
