import heapq
from yogi import read


def huffman_average_bits(n):
    pq = []
    for _ in range(n):
        freq = read(float)
        heapq.heappush(pq, freq)
    average = 0
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        average += (a+b)/100
        heapq.heappush(pq, a+b)
    return average


def main():
    n = read(int)
    print("expected number of bits per letter: {:.4f}".format(
        huffman_average_bits(n)))


main()
