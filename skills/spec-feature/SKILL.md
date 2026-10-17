---
name: spec-feature
description: Giai đoạn 1–2 của LIFECYCLE. Dùng khi người dùng muốn thêm tính năng mới, bắt đầu dự án từ yêu cầu/spec của khách, hoặc nói "làm tính năng X" mà chưa có spec trong docs/specs/. Tạo spec trung tính (không lộ thông tin khách), có tiêu chí chấp nhận đo được, và ADR cho quyết định khó đảo ngược.
---

# Viết spec

1. **Đọc bối cảnh**: `CLAUDE.md`, `docs/LIFECYCLE.md`, các spec/ADR liên quan trong `docs/`. Nếu người dùng đưa spec gốc của khách
   (thường nằm ngoài repo), đọc nó nhưng **không copy tên khách/app khách** vào repo — thêm các từ đó vào `.privacy-blocklist`.
2. **Hỏi để làm rõ** — tối đa 4 câu mỗi lượt, mỗi câu có lựa chọn và đề xuất. Ưu tiên: người dùng là ai, luồng chính,
   thế nào là xong, khối lượng dữ liệu, ngoài phạm vi. Không hỏi điều tự tìm được trong code.
3. **Đề xuất 2–3 hướng** kèm đánh đổi và khuyến nghị một hướng. Chờ người dùng chọn.
4. **Viết spec** vào `docs/specs/YYYY-MM-DD-<slug>.md` theo `docs/specs/_TEMPLATE.md`:
   - Mỗi tiêu chí chấp nhận dạng "Cho / Khi / Thì", kiểm được bằng test.
   - Edge case: tên file có dấu/emoji, rỗng, hỏng, input = output, huỷ giữa chừng, ổ đầy.
   - Mục Kiến trúc tôn trọng `.claude/rules/architecture.md` (lõi không import web).
   - Có UI cho khách → ghi chú dùng `ui-ux-pro-max` ở giai đoạn thiết kế.
5. Quyết định khó đảo ngược (định dạng file, thư viện chính, cách lưu dữ liệu) → `docs/adr/NNNN-<slug>.md`.
6. **Tự soát**: không còn TODO/placeholder, "Câu hỏi mở" rỗng, không mâu thuẫn, không chứa dữ liệu khách
   (`python scripts/check_privacy.py` sau khi `git add`).
7. Trình người dùng duyệt. Khi được duyệt: đổi trạng thái thành "Đã duyệt", commit `docs(spec): …`, chuyển sang skill `plan-feature`.
