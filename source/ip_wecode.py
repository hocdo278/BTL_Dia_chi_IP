import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    out = []
    parts = []

    def bt(pos):
        k = len(parts)
        left = n - pos
        if left < 4 - k or left > 3 * (4 - k):
            return
        if k == 4:
            out.append(".".join(parts))
            return
        for ln in (1, 2, 3):
            if pos + ln > n:
                break
            seg = s[pos:pos + ln]
            if ln > 1 and seg[0] == "0":
                break
            if int(seg) > 255:
                break
            parts.append(seg)
            bt(pos + ln)
            parts.pop()

    if s.isdigit():
        bt(0)
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
