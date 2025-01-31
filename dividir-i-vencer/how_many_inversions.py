from yogi import tokens, read
def unio(sec:list[int], left:int, center:int, right: int) -> int:
    R = sec[0:0]
    c = 0
    i, j = left, center + 1
    while i <= center and j <= right:
        if sec[i] <= sec[j]:
            R.append(sec[j])
        else:
            R.append(sec[j])
            j += 1
            c += (center - i + 1)
        

# com merge sort pero amb comptador


def inversions_rec(sec: list[int], left:int, right:int) -> int:
    inv = 0
    if left < right:
        center = (left + right) // 2
        inv += inversions_rec(sec, left, center)
        inv += inversions_rec(sec, center+1, right)
        inv += unio(sec, left, center, right)
    return inv
         

def inversions(sec:list[int], n: int) -> int:
    return inversions_rec(sec, 0, n-1)

def main() -> None:
    for n in tokens(int):
        sec = [read(int) for _ in range(n)]
        print(inversions(sec, n))