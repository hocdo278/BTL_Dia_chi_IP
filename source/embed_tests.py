import json
import re
from pathlib import Path

HERE = Path(__file__).parent
tests = json.loads((HERE.parent / "testcases" / "tests.json").read_text(encoding="utf-8"))
slim = [{"group": t["group"], "name": t["name"], "input": t["input"], "expected": t["expected"]} for t in tests]
html = (HERE / "index.html").read_text(encoding="utf-8")
new = re.sub(r"/\*TESTS_BEGIN\*/.*?/\*TESTS_END\*/", lambda m: "/*TESTS_BEGIN*/" + json.dumps(slim, ensure_ascii=False) + "/*TESTS_END*/", html, flags=re.S)
(HERE / "index.html").write_text(new, encoding="utf-8")
print("da nhung", len(slim), "testcase")
