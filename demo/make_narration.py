"""Tao loi doc bang giong Ngoc Huyen (engine VieNeu) cho tung canh trong scenes.json.

Chay bang Python co cai vieneu (Python di kem Reup-Video Studio):
    python make_narration.py
Dau ra: D:\\tmp\\btl_ip\\build\\<ten canh>.wav va durations.json
Canh nao da co file .wav thi giu nguyen, chi tao canh moi (them --force de tao lai tat ca).
"""
import json
import sys
import time
from pathlib import Path

import soundfile as sf
from vieneu import Vieneu

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).parent
BUILD = Path(r"D:\tmp\btl_ip\build")
VOICE = "Ngọc Huyền"

scenes = json.loads((HERE / "scenes.json").read_text(encoding="utf-8"))
BUILD.mkdir(parents=True, exist_ok=True)

t0 = time.time()
model = Vieneu()
print("load model:", round(time.time() - t0, 1), "s", flush=True)
try:
    print("preset voices:", model.list_preset_voices(), flush=True)
except Exception as e:
    print("khong liet ke duoc voice:", e, flush=True)

durations = {}
force = "--force" in sys.argv
for i, sc in enumerate(scenes):
    path = BUILD / f"{sc['name']}.wav"
    t = time.time()
    if force or not path.exists():
        audio = model.infer(sc["speech"], voice=VOICE)
        model.save(audio, str(path))
    dur = sf.info(str(path)).duration
    durations[sc["name"]] = {"file": str(path), "duration": dur}
    print(f"{i:02d} {sc['name']:<14} {dur:6.1f}s audio, {"giu nguyen" if (time.time() - t) < 0.5 else "tao moi"}", flush=True)

(BUILD / "durations.json").write_text(json.dumps(durations, ensure_ascii=False, indent=1), encoding="utf-8")
print("tong thoi luong loi doc:", round(sum(v["duration"] for v in durations.values()), 1), "s")
