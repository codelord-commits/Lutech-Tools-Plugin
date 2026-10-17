---
name: dong-goi
description: Dùng khi người dùng muốn có file .exe/.app để gửi đồng nghiệp ("đóng gói", "xuất file exe", "gửi tool cho team") hoặc gõ /lutech-tools:dong-goi. Không cần GitHub.
---

# Đóng gói tool để gửi đi

1. Kiểm nhanh: `python scripts/setup_env.py` (bỏ qua nếu đã có), rồi `.venv` python `-m pytest -q -m "not ui"` phải xanh.
   Đỏ → sửa theo `implement-tdd` trước, báo người dùng một câu.
2. `python scripts/check_privacy.py --all` — có dữ liệu nhạy cảm thì dừng và giải thích bằng lời thường.
3. `python scripts/build_exe.py` → lấy đường dẫn zip.
4. Chạy thử bản đóng gói: `dist/<App>/<App>.exe cli --version` (macOS: `dist/<App>.app/Contents/MacOS/<App> cli --version`).
5. Báo người dùng:
   ```
   ✓ File gửi đi: <đường dẫn zip> (<dung lượng> MB)
   Người nhận: giải nén → mở <App>.exe → trình duyệt tự mở giao diện.
   macOS: chuột phải vào app → Open → Open (lần đầu).
   Windows báo "Windows protected your PC": bấm More info → Run anyway.
   ```
   Mở thư mục chứa file zip cho người dùng.
6. Muốn phát hành chính thức có số phiên bản và link tải chung → chuyển sang skill `release` (hỏi trước mọi bước đẩy lên mạng).
