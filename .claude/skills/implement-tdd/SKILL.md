---
name: implement-tdd
description: Giai đoạn 4 và 8 của LIFECYCLE. Dùng khi thực thi task trong docs/plans/, viết bất kỳ code nghiệp vụ nào, hoặc sửa bug. Bắt buộc test-trước (đỏ → xanh → dọn) và tuân thủ .claude/rules.
---

# Code theo TDD

Với **từng task** trong plan (hoặc bug):

1. **Đỏ** — viết test cho hành vi (bug: test tái hiện). Chạy và xác nhận nó fail *đúng lý do*:
   `.venv/Scripts/python -m pytest -q <file>::<test>`.
2. **Xanh** — viết code tối thiểu để pass. Tôn trọng:
   - `architecture.md`: logic ở `basetool/`, CLI/web chỉ là vỏ;
   - `python.md`: UTF-8, `pathlib`, ghi nguyên tử, lỗi item không dừng batch;
   - `web-ui.md` nếu đụng `web/static/` (i18n cả vi/en, token CSS, `data-testid`).
3. **Dọn** — refactor khi vẫn xanh. Chạy toàn bộ: `python -m pytest -q` và `ruff check .`.
4. Đánh dấu task xong trong plan, cập nhật `CHANGELOG.md` `[Unreleased]` nếu người dùng thấy được, commit theo Conventional Commits.
5. Đổi UI → mở preview (`.claude/launch.json` cấu hình `web.server --no-browser --port 8765 --token devtoken`) và xem thật trước khi báo xong.

Gặp lỗi khó hiểu: dừng, tái hiện, tìm nguyên nhân gốc trước khi sửa — không đoán mò sửa nhiều chỗ.
Không báo "xong" khi chưa dán kết quả test.
