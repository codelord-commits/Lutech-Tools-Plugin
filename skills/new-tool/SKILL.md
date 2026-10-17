---
name: new-tool
description: Giai đoạn 0 của LIFECYCLE. Dùng khi người dùng muốn tạo công cụ/dự án mới ("tạo tool mới", "khởi tạo dự án", "new tool") từ template Lutech Base Tool — copy khung, đổi tên package/app, git init, cài môi trường và chạy test lần đầu.
---

# Tạo tool mới từ template

Template nằm ngay trong plugin: `${CLAUDE_PLUGIN_ROOT}/scripts/new_project.py`
(nếu biến không được thay, dùng `${CLAUDE_SKILL_DIR}/../../scripts/new_project.py`).

1. **Hỏi** (một lượt, có đề xuất): tên hiển thị (vd "Photo Resizer"), thư mục đích (phải trống), **loại tool**:

   | Loại | Khi nào chọn | Sau khi tạo, làm gì |
   |------|--------------|---------------------|
   | **Web UI + CLI** (mặc định) | Người dùng cuối không rành dòng lệnh, cần chọn thư mục/preset bằng giao diện | Giữ nguyên `web/`; thiết kế UI bằng `ui-ux-pro-max` ở bước spec |
   | **Chỉ CLI** | Tool cho dev/automation, chạy trong script/CI | Xoá `web/`, `tests/web`, `tests/ui`, entry `*-web` trong `pyproject.toml`, `build/launcher.py` mở thẳng CLI |
   | **Thư viện/lõi** | Code dùng lại ở dự án khác | Bỏ `web/` và `build/`; giữ `basetool/` + test; bỏ workflow release zip |

2. Chạy: `python "<đường dẫn new_project.py>" "<đích>" --name "<Tên>"` (thêm `--package <ten>` nếu muốn tên package khác).
3. Trong thư mục mới: `python -m venv .venv`, `.venv/Scripts/pip install -e .[dev]` (macOS/Linux: `.venv/bin/pip`),
   rồi `python -m pytest -q -m "not ui"` — phải xanh. Nếu là Web UI: `python -m playwright install chromium` rồi chạy cả test UI.
4. Áp dụng phần dọn theo loại tool ở bảng trên (nếu không phải mặc định), chạy lại test.
5. Nhắc người dùng: tạo `.privacy-blocklist` (tên khách, app khách, domain nội bộ — file bị gitignore), thêm icon
   `build/icon.ico` / `build/icon.icns`.
6. Commit đầu `chore: khởi tạo <Tên> từ template Lutech`. **Không** tạo repo GitHub/push khi chưa hỏi.
7. Gợi ý bước tiếp: mở Claude Code trong thư mục mới và chạy `/lutech-tools:spec-feature`.
