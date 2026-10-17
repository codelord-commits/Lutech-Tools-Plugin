---
name: review-change
description: Giai đoạn 5 của LIFECYCLE. Dùng sau khi hoàn thành một tính năng/fix, trước khi merge hoặc mở PR, hoặc khi người dùng nói "review", "kiểm tra code".
---

# Review thay đổi

1. Xem diff so với `main` (`git diff main...HEAD`), đối chiếu spec + plan: mọi AC có test? có gì ngoài phạm vi lọt vào?
2. Chạy `/code-review` cho lỗi đúng/sai. Nếu đụng `web/server.py`, `web/api/`, IO, subprocess → chạy thêm `/security-review`.
3. Soát theo rule:
   - Ranh giới: `grep -rn "import web\|from web\|fastapi" basetool/` phải rỗng.
   - Lỗi: không nuốt exception im lặng; thông báo lỗi tiếng người.
   - Hiệu năng: không đọc cả file lớn vào RAM khi không cần; không chặn event loop.
   - Quyền riêng tư: `python scripts/check_privacy.py --all`.
4. Đổi UI → chạy skill `ui-review`.
5. Báo cáo theo mức **Cao / Trung bình / Thấp**, mỗi mục có file:dòng + cách sửa. Sửa hết mức Cao trước khi sang `qa-check`.
