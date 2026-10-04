---
name: qa-check
description: Giai đoạn 6 của LIFECYCLE. Dùng trước khi release hoặc khi người dùng hỏi "đã sẵn sàng phát hành chưa", "test toàn bộ". Chạy toàn bộ kiểm tra tự động, test dữ liệu thật (local) và build thử bản đóng gói.
---

# QA trước release

Chạy lần lượt, dừng ở bước đầu tiên fail và báo kèm output:

1. `ruff check .`
2. `python -m pytest -q` (gồm UI). Ghi số test pass/skip.
3. Có dữ liệu thật? `BASETOOL_REAL_DATA=<đường dẫn ngoài repo> python -m pytest -q -m real`.
4. `python scripts/check_privacy.py --all`.
5. Build thử: `pip install pyinstaller` rồi `pyinstaller build/app.spec --noconfirm --workpath build/out --distpath dist`.
6. Chạy bản build: `dist/BaseTool/BaseTool.exe cli --version`, rồi mở `dist/BaseTool/BaseTool.exe`, chạy một job mẫu qua UI.
7. Kiểm thủ công nhanh: tên file có dấu, thư mục rỗng, bấm Dừng giữa chừng, đóng/mở lại app (preset người dùng còn).
8. Báo cáo bảng: bước | kết quả | ghi chú. Chỉ nói "sẵn sàng" khi tất cả xanh.
