---
name: ui-review
description: Dùng khi tạo mới hoặc thay đổi giao diện trong web/static/ (HTML/CSS/JS/i18n), hoặc người dùng hỏi giao diện đã ổn chưa. Kết hợp skill ui-ux-pro-max và kiểm thật trên trình duyệt ở nhiều kích thước, sáng/tối, vi/en.
---

# Review giao diện

1. Thiết kế mới/đổi lớn: gọi skill `ui-ux-pro-max` để chọn style, palette, font pairing phù hợp sản phẩm; cập nhật `css/tokens.css`
   (cả light và `[data-theme="dark"]`), không hard-code màu.
2. Chạy preview (`.claude/launch.json`) và kiểm trên trình duyệt:
   - 375×812, 768×1024, 1440×900 — không cuộn ngang, không chữ bị cắt.
   - Sáng và tối; tiếng Việt và tiếng Anh (chuỗi tiếng Việt dài hơn — có vỡ layout không?).
   - Bàn phím: Tab đi hết control theo thứ tự hợp lý, focus nhìn thấy, Enter/Space kích hoạt.
   - Trạng thái: rỗng, đang chạy, hoàn tất, lỗi (đường dẫn sai, job đang chạy 409), nút bị vô hiệu.
   - Console không lỗi; tương phản chữ ≥ 4.5:1; vùng bấm ≥ 40px.
3. Mọi key i18n có ở cả `vi.json` và `en.json`:
   `python -c "import json;a=json.load(open('web/static/i18n/vi.json',encoding='utf-8'));b=json.load(open('web/static/i18n/en.json',encoding='utf-8'));print(set(a)^set(b))"` → `set()`.
4. Chạy `python -m pytest -q tests/ui`. Gửi người dùng ảnh chụp màn hình desktop + mobile làm bằng chứng.
