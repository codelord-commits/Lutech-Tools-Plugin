# Base Tool

Khung dự án cho **công cụ desktop chạy local**: lõi Python + CLI + giao diện web trong trình duyệt,
đóng gói thành `.exe` (Windows) và `.app` (macOS), phát hành qua GitHub Releases.

> Đây là template. Tạo dự án mới: xem [docs/TEMPLATE.md](docs/TEMPLATE.md).

## Dùng ngay (người dùng cuối)

1. Tải file zip cho hệ điều hành của bạn ở mục **Releases**.
2. Giải nén, mở `BaseTool.exe` (Windows) hoặc `BaseTool.app` (macOS).
3. Trình duyệt tự mở giao diện. Đóng cửa sổ dòng lệnh để thoát.

macOS chặn app chưa ký: chuột phải vào app → **Open** → **Open**.

## Chạy từ mã nguồn

```bash
python -m venv .venv
.venv/Scripts/pip install -e .[dev]
basetool-web                          # giao diện web
basetool run ./input ./output         # dòng lệnh
```

## Cấu trúc

```
basetool/          lõi nghiệp vụ — thuần Python, không biết gì về web
  models.py        pydantic model, validate mọi input
  processor.py     nghiệp vụ chính (thay bằng của bạn)
  preset_io.py     preset built-in + của người dùng
  io_utils.py      ghi file nguyên tử, JSON UTF-8
  defaults.py      đường dẫn cấu hình theo OS, hỗ trợ PyInstaller
  __main__.py      CLI
web/               FastAPI server local + API + static UI (Alpine.js, không CDN)
presets/           preset mặc định đi kèm
tests/             unit / web (API) / ui (Playwright)
build/             PyInstaller spec + launcher (+ icon.ico / icon.icns)
scripts/           new_project, bump_version, check_privacy
docs/              LIFECYCLE, specs/, plans/, adr/, RELEASE
.claude/           rule + skill + hook cho Claude Code
.github/           CI test, release theo tag, template PR/issue
```

## Giấy phép

MIT — xem [LICENSE](LICENSE).
