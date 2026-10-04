# Dùng BaseToolProject làm template

```bash
python scripts/new_project.py D:/Projects/photo-resizer --name "Photo Resizer"
cd D:/Projects/photo-resizer
python -m venv .venv
.venv/Scripts/pip install -e .[dev]
python -m pytest -q
```

Script sẽ copy toàn bộ (trừ `.git`, `.venv`, cache, build), đổi `basetool` → `photoresizer`,
`BaseTool` → `PhotoResizer`, `Base Tool` → `Photo Resizer`, `base-tool` → `photo-resizer`, rồi `git init`.

Sau đó:
1. Tạo `.privacy-blocklist` với tên khách/app khách (file này bị git bỏ qua).
2. Thêm `build/icon.ico` + `build/icon.icns` của app.
3. Mở Claude Code trong thư mục mới, chạy skill **spec-feature** để bắt đầu giai đoạn 1 của [LIFECYCLE.md](LIFECYCLE.md).
4. Thay `processor.py`, `models.py`, `presets/` và UI bằng nghiệp vụ thật — giữ nguyên các rule trong `.claude/rules/`.

Trên GitHub: bật *Template repository* cho repo này để có nút **Use this template**
(khi đó vẫn cần chạy bước đổi tên — dùng `new_project.py` trên bản clone).
