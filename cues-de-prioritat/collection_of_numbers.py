import heapq
from yogi import tokens, read

cua = []

for n in tokens(str):
    if n == "S":
        # store x in cua
        x = read(int) 
        heapq.heappush(cua, x)
    elif n == "A":
        # prints the largest number
        if cua:
            y = heapq.nlargest(1, cua)[0]
            print(y)
        else:
            print("error!")
    elif n == "R":
        # removes greatest number
        if cua:
            y = heapq.nlargest(1, cua)[0]
            cua.remove(y)
            heapq.heapify(cua)
        else:
            print("error!")
    elif n == "I":
        # increase greatest number by x units
        x = read(int)
        if cua:
            y = heapq.nlargest(1, cua)[0]
            cua.remove(y)
            heapq.heapify(cua)
            heapq.heappush(cua, y + x)
        else:
            print("error!")
    elif n == "D":
        # decrease greatest number by x units
        x = read(int)
        if cua:
            y = heapq.nlargest(1, cua)[0]
            cua.remove(y)
            heapq.heapify(cua)
            heapq.heappush(cua, y - x)
        else:
            print("error!")
    else:
        print(f"Invalid command: {n}")
