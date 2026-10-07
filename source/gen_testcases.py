import random
import subprocess
import sys
from pathlib import Path

from ip_bruteforce import solve as brute

HERE = Path(__file__).parent
OUT = HERE.parent / "testcases"
random.seed(26410111)

groups = []

def add(group, name, s, note):
    groups.append((group, name, s, note))

add("sample", "sample_de_bai", "25525511135", "Vi du trong de wecode")
add("normal", "normal_01", "192168001001", "12 chu so nhung doan 001 co so 0 dau, vo nghiem")
add("normal", "normal_02", "1921681", "7 chu so, nhieu dap an")
add("normal", "normal_03", "101023", "Ket qua gom nhieu dia chi")
add("normal", "normal_04", "172161", "6 chu so")
add("normal", "normal_05", "123456789", "9 chu so")
add("boundary", "edge_min_len_4", "1111", "Do dai toi thieu de co nghiem: 4")
add("boundary", "edge_max_len_12", "255255255255", "Do dai toi da co nghiem: 12, dung 1 cach")
add("boundary", "edge_len_13", "1111111111111", "13 chu so, vo nghiem")
add("boundary", "edge_len_3", "123", "3 chu so, vo nghiem")
add("boundary", "edge_len_1", "1", "1 chu so, vo nghiem")
add("boundary", "edge_all_zero_4", "0000", "Chi co 0.0.0.0")
add("boundary", "edge_all_zero_12", "000000000000", "Vo nghiem vi so 0 dau")
add("boundary", "edge_255_max", "255255255255", "Moi doan = 255")
add("boundary", "edge_256", "256256256256", "Moi doan 256 > 255, vo nghiem")
add("special", "special_leading_zero_1", "010010", "So 0 dung dau doan nhieu chu so")
add("special", "special_leading_zero_2", "0100", "Chi 0.1.0.0")
add("special", "special_leading_zero_3", "00000", "0 dau, nhieu so 0")
add("special", "special_one_way_12", "111111111111", "12 chu so 1, dung 1 cach 111.111.111.111")
add("special", "special_many_answers", "1111111", "7 chu so 1, nhieu dap an")
add("special", "special_digits_10", "1234567890", "10 chu so")
add("special", "special_255_mixed", "2552551113", "Gia tri sat 255")
add("invalid", "invalid_letters", "12a45", "Co ky tu khong phai so")
add("invalid", "invalid_empty", "", "Chuoi rong")
for i in range(15):
    n = random.randint(4, 12)
    add("random", f"random_{i+1:02d}", "".join(random.choice("0123456789") for _ in range(n)), f"Ngau nhien do dai {n}")
for i in range(5):
    n = random.randint(4, 12)
    add("random", f"random_small_alpha_{i+1:02d}", "".join(random.choice("0125") for _ in range(n)), f"Ngau nhien bang chu so 0125, do dai {n}")
add("large", "large_100_ones", "1" * 100, "100 chu so, vo nghiem, kiem tra cat tia")
add("large", "large_100_random", "".join(random.choice("0123456789") for _ in range(100)), "100 chu so ngau nhien")
add("large", "large_100_zeros", "0" * 100, "100 so 0")
add("large", "large_13_ones", "1" * 13, "13 chu so, vuot 12")

for p in OUT.glob("*"):
    if p.is_file():
        p.unlink()

rows = []
bad = 0
for group, name, s, note in groups:
    (OUT / f"{name}.in").write_text(s + "\n", encoding="utf-8")
    exp = sorted(brute(s))
    r = subprocess.run([sys.executable, str(HERE / "ip_wecode.py")], input=s + "\n", capture_output=True, text=True)
    got = sorted(r.stdout.split())
    ok = got == exp
    bad += not ok
    (OUT / f"{name}.out").write_text("\n".join(exp) + ("\n" if exp else ""), encoding="utf-8")
    rows.append((group, name, len(s), len(exp), "OK" if ok else "FAIL", note))

with open(OUT / "README.md", "w", encoding="utf-8") as f:
    f.write("# Bo testcase bai Dia chi IP\n\n")
    f.write("Dap an (`.out`) sinh boi `ip_bruteforce.py` (duyet 3 vi tri cat, doc lap voi thuat toan quay lui). ")
    f.write("Thu tu dong trong `.out` da sap xep, khi so sanh can sap xep ket qua.\n\n")
    f.write("| Nhom | Ten | Do dai | So dap an | Khop brute force | Ghi chu |\n|---|---|---|---|---|---|\n")
    for r in rows:
        f.write("| " + " | ".join(str(x) for x in r) + " |\n")

import json
manifest = []
for group, name, s_, note in groups:
    manifest.append({"group": group, "name": name, "input": s_, "expected": sorted(brute(s_)), "note": note})
(OUT / "tests.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
print("tong", len(rows), "test, sai:", bad)
