# Bài tập lớn CS112: Địa chỉ IP bằng Quay lui (Backtracking)

Sinh viên: Đỗ Quốc Học, MSSV 26410045. Bài WeCode: Lab#01 BACKTRACKING, "Địa chỉ IP".

## Cấu trúc

| Thư mục / tệp | Nội dung |
|---|---|
| `source/index.html` | Ứng dụng web trực quan hóa. Mở trực tiếp bằng Chrome, Edge hoặc Firefox, không cần cài đặt. |
| `source/ip_wecode.py` | Lời giải Python (quay lui) dùng để nộp WeCode. |
| `source/ip_bruteforce.py` | Bản vét cạn độc lập, dùng sinh đáp án đối chứng. |
| `source/gen_testcases.py` | Sinh 48 testcase vào `testcases/` (hạt giống cố định). |
| `source/embed_tests.py` | Nhúng testcase vào `index.html` để chạy ngay trong trang. |
| `source/test_core.js` | Kiểm thử lõi thuật toán của `index.html` bằng Node.js. |
| `testcases/` | 48 cặp `.in`/`.out`, `tests.json`, `README.md` mô tả từng test. |
| `demo/demo_video.mp4` | Video demo 3 phút 9 giây (11 cảnh), giọng Ngọc Huyền, có phụ đề. |
| `demo/scenes.json`, `make_narration.py`, `record_demo.py` | Kịch bản lời đọc và script tạo video. |
| `report/Bao_Cao_Bai_Tap_Lon.tex`, `.pdf`, `img/` | Báo cáo (LaTeX và PDF), có mục hướng dẫn sử dụng dashboard. |

## Chạy lại

```text
python3 source/ip_wecode.py            # đọc 1 dòng từ stdin
python3 source/gen_testcases.py        # sinh lại testcase, tự đối chiếu với vét cạn
python3 source/embed_tests.py          # nhúng testcase vào index.html
node source/test_core.js source/index.html
```
