"""Quay video demo bai Dia chi IP: giong Ngoc Huyen (VieNeu) + phu de + Chrome (Playwright) + ffmpeg.

Quy trinh: make_narration.py tao 10 file wav -> record_demo.py quay man hinh, moi canh keo dai
>= do dai loi doc, ghi lai moc bat dau canh -> ffmpeg dat tung wav dung moc (adelay) va tron (amix).

Chay (Python Windows co playwright + imageio-ffmpeg, dung Chrome that cua may):
    D:\\tmp\\btl_ip\\venv\\Scripts\\python.exe record_demo.py
Dau ra: E:\\BTL_Dia_chi_IP\\demo\\demo_video.mp4
"""
import asyncio
import json
import subprocess
import sys
import time
from pathlib import Path

import imageio_ffmpeg
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).parent
APP_URL = (HERE.parent / "source" / "index.html").resolve().as_uri()
BUILD = Path(r"D:\tmp\btl_ip\build")
VIDEO_DIR = Path(r"D:\tmp\btl_ip\video_raw")
OUTPUT = HERE / "demo_video.mp4"
SIZE = {"width": 1600, "height": 900}
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

SCENES = json.loads((HERE / "scenes.json").read_text(encoding="utf-8"))
DURS = json.loads((BUILD / "durations.json").read_text(encoding="utf-8"))

OVERLAY_JS = """
() => {
  const style = document.createElement('style');
  style.textContent = `
    #demo-caption { position: fixed; left: 50%; bottom: 18px; transform: translateX(-50%);
      max-width: 1250px; padding: 11px 22px; background: rgba(0,0,0,.86); color: #fff;
      font: 600 19px/1.4 'Plus Jakarta Sans','Segoe UI',sans-serif; border-radius: 10px; z-index: 9999;
      text-align: center; border: 1px solid rgba(255,255,255,.14); }
    #demo-cursor { position: fixed; width: 18px; height: 18px; border-radius: 50%;
      background: rgba(250,204,21,.9); border: 2px solid #fff; z-index: 10000;
      pointer-events: none; transform: translate(-50%,-50%); left: -50px; top: -50px;
      transition: transform .1s; box-shadow: 0 0 12px rgba(250,204,21,.8); }
    #demo-cursor.down { transform: translate(-50%,-50%) scale(.7); }
    #demo-title { position: fixed; inset: 0; z-index: 9998; display: flex; flex-direction: column;
      align-items: center; justify-content: center; gap: 14px; background: #0c0f17;
      color: #f1f5f9; font-family: 'Plus Jakarta Sans','Segoe UI',sans-serif; transition: opacity .6s; }
    #demo-title h1 { font-size: 46px; font-weight: 800; }
    #demo-title p { font-size: 22px; color: #94a3b8; }
    #demo-title .chip { font: 600 16px Consolas, monospace; color: #38bdf8;
      border: 1px solid #38bdf8; padding: 6px 14px; border-radius: 8px; }`;
  document.head.appendChild(style);
  const cap = Object.assign(document.createElement('div'), { id: 'demo-caption' });
  const cur = Object.assign(document.createElement('div'), { id: 'demo-cursor' });
  document.body.append(cap, cur);
  addEventListener('mousemove', e => { cur.style.left = e.clientX + 'px'; cur.style.top = e.clientY + 'px'; });
  addEventListener('mousedown', () => cur.classList.add('down'));
  addEventListener('mouseup', () => cur.classList.remove('down'));
}
"""


class Director:
    def __init__(self, page):
        self.page = page
        self.t0 = time.monotonic()

    async def caption(self, text):
        await self.page.evaluate("t => { const c = document.getElementById('demo-caption'); c.textContent = t; c.style.display = t ? 'block' : 'none'; }", text)

    async def title_card(self, show, title="", subtitle=""):
        if show:
            await self.page.evaluate(
                """([t, s]) => { const d = document.createElement('div'); d.id = 'demo-title';
                d.innerHTML = `<span class="chip">CS112 · Phân Tích &amp; Thiết Kế Thuật Toán</span>
                <h1>${t}</h1><p>${s}</p>`; document.body.appendChild(d); }""", [title, subtitle])
        else:
            await self.page.evaluate("() => { const d = document.getElementById('demo-title'); if (d) { d.style.opacity = 0; setTimeout(() => d.remove(), 700); } }")

    async def move(self, selector, steps=25):
        box = await self.page.locator(selector).first.bounding_box()
        await self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2, steps=steps)

    async def click(self, selector):
        await self.page.locator(selector).first.scroll_into_view_if_needed()
        await self.move(selector)
        await asyncio.sleep(0.25)
        await self.page.locator(selector).first.click()

    async def set_input(self, value):
        await self.move("#inputStr")
        await self.page.fill("#inputStr", value)
        await asyncio.sleep(0.4)

    async def set_speed(self, ms):
        await self.page.evaluate("ms => { const r = document.getElementById('speedRange'); r.value = ms; r.dispatchEvent(new Event('input')); }", ms)

    async def scroll_to(self, selector):
        await self.page.evaluate("s => document.querySelector(s).scrollIntoView({behavior: 'smooth', block: 'center'})", selector)
        await asyncio.sleep(0.8)

    async def wait_done(self, timeout=90):
        await self.page.wait_for_function("() => document.getElementById('btnPlay').textContent.includes('Chạy lại')", timeout=timeout * 1000)


async def scene_actions(d, name):
    if name == "intro":
        await d.title_card(True, "IP Address Restore Visualizer", "Bài Tập Lớn: Quay lui (Backtracking) trên bài Địa chỉ IP (WeCode)")
        await asyncio.sleep(7)
        await d.title_card(False)
    elif name == "problem":
        await d.set_input("25525511135")
        await d.move("#inputStr")
        await asyncio.sleep(3)
        await d.move("#digitStrip", steps=20)
    elif name == "idea":
        await d.move("#code", steps=20)
        for i in (5, 8, 9, 3, 10):
            await d.move(f"#l{i}", steps=12)
            await asyncio.sleep(2.4)
    elif name == "step":
        await d.set_input("25525511135")
        await d.click("#btnReset")
        await d.set_speed(260)
        for _ in range(12):
            await d.click("#btnStep")
            await asyncio.sleep(0.9)
    elif name == "run":
        await d.click("#btnReset")
        await d.set_speed(45)
        await d.click("#btnPlay")
        await d.wait_done()
        await d.scroll_to("#compareBox")
        await d.move("#treeWrap", steps=20)
    elif name == "compare":
        await d.scroll_to("#compareBox")
        await d.click("#btnCompare")
        await asyncio.sleep(1)
        await d.move("#compareBox", steps=20)
    elif name == "options":
        await d.page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
        await asyncio.sleep(0.8)
        await d.set_input("25525511135")
        await d.click("#chkPrune")
        await d.set_speed(25)
        await d.click("#btnPlay")
        await d.wait_done()
        await d.click("#chkPrune")
        await d.click("#btnRandom")
        await asyncio.sleep(1.5)
        await d.move("#presetSelect")
        await d.page.select_option("#presetSelect", "2")
        await asyncio.sleep(1.5)
    elif name == "leading_zero":
        await d.page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
        await asyncio.sleep(0.8)
        await d.set_input("010010")
        await d.click("#btnReset")
        await d.set_speed(40)
        await d.click("#btnPlay")
        await d.wait_done()
        await d.scroll_to("#treeWrap")
    elif name == "big":
        await d.page.evaluate("window.scrollTo({top: 0, behavior: 'smooth'})")
        await asyncio.sleep(0.8)
        await d.set_input("1" * 100)
        await d.click("#btnReset")
        await d.set_speed(200)
        await d.click("#btnPlay")
        await d.wait_done()
        await d.scroll_to("#compareBox")
        await d.click("#btnCompare")
        await asyncio.sleep(1)
        await d.move("#compareBox", steps=20)
    elif name == "tests":
        await d.scroll_to("#btnRunTests")
        await d.click("#btnRunTests")
        await asyncio.sleep(1.5)
        await d.scroll_to("#testSummary")
        await d.page.evaluate("document.getElementById('testsBox').scrollTo({top: 400, behavior: 'smooth'})")
    elif name == "outro":
        await d.title_card(True, "Cảm ơn cô đã theo dõi!", "Source code · Video demo · Bộ testcase · Báo cáo")


async def record():
    offsets = []
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    for old in VIDEO_DIR.glob("*.webm"):
        old.unlink()
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome")
        ctx = await browser.new_context(viewport=SIZE, record_video_dir=str(VIDEO_DIR), record_video_size=SIZE)
        page = await ctx.new_page()
        errs = []
        page.on("pageerror", lambda e: errs.append(str(e)))
        d = Director(page)
        await page.goto(APP_URL, wait_until="load")
        await page.evaluate(OVERLAY_JS)
        await page.mouse.move(800, 450)
        await asyncio.sleep(0.8)
        d.t0 = time.monotonic()
        for sc in SCENES:
            dur = DURS[sc["name"]]["duration"]
            offsets.append(time.monotonic() - d.t0)
            await d.caption(sc["caption"])
            await asyncio.gather(scene_actions(d, sc["name"]), asyncio.sleep(dur + 0.6))
            print(f"  canh {sc['name']:<13} bat dau {offsets[-1]:6.1f}s, loi doc {dur:5.1f}s", flush=True)
        await asyncio.sleep(1.5)
        video = page.video
        await ctx.close()
        await browser.close()
        if errs:
            print("LOI JS trong luc quay:", errs)
        return Path(await video.path()), offsets


def mux(video, offsets):
    inputs, filters = ["-i", str(video)], []
    for i, (sc, off) in enumerate(zip(SCENES, offsets), start=1):
        inputs += ["-i", DURS[sc["name"]]["file"]]
        ms = int(off * 1000)
        filters.append(f"[{i}:a]adelay={ms}|{ms}[a{i}]")
    n = len(SCENES)
    mix = "".join(f"[a{i}]" for i in range(1, n + 1))
    filters.append(f"{mix}amix=inputs={n}:duration=longest:normalize=0[aout]")
    r = subprocess.run([
        FFMPEG, "-y", *inputs, "-filter_complex", ";".join(filters),
        "-map", "0:v", "-map", "[aout]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k", "-shortest", str(OUTPUT),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:])
        raise SystemExit(1)


async def main():
    print("1/2 Quay man hinh (Chrome)...")
    video, offsets = await record()
    print("2/2 Ghep tieng + hinh thanh MP4...")
    mux(video, offsets)
    print("Xong:", OUTPUT.name)
    (HERE / "offsets.json").write_text(json.dumps(dict(zip([s["name"] for s in SCENES], offsets)), indent=1), encoding="utf-8")


if __name__ == "__main__":
    asyncio.run(main())
