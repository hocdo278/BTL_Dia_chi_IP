import sys
from itertools import combinations

def solve(s):
    n = len(s)
    res = []
    if not s.isdigit() or n < 4 or n > 12:
        return res
    for a, b, c in combinations(range(1, n), 3):
        segs = [s[:a], s[a:b], s[b:c], s[c:]]
        if all(1 <= len(x) <= 3 and int(x) <= 255 and (len(x) == 1 or x[0] != "0") for x in segs):
            res.append(".".join(segs))
    return res

if __name__ == "__main__":
    r = solve(sys.stdin.readline().strip())
    if r:
        sys.stdout.write("\n".join(r) + "\n")
