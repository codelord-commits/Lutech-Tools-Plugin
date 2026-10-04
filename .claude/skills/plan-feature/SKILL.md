---
name: plan-feature
description: Giai đoạn 3 của LIFECYCLE. Dùng khi đã có spec được duyệt trong docs/specs/ và cần chia thành task nhỏ trước khi code, hoặc khi người dùng nói "lên kế hoạch", "chia task".
---

# Lập plan

1. Đọc spec đã duyệt và code hiện có ở các module sẽ đụng tới.
2. Chia task theo `docs/plans/_TEMPLATE.md`, lưu `docs/plans/YYYY-MM-DD-<slug>.md`. Mỗi task:
   - nhỏ đủ cho 1 commit (≈ 15–60 phút), có thứ tự phụ thuộc rõ;
   - ghi file sẽ sửa/tạo, **test sẽ viết trước** (tên test + AC nó kiểm), lệnh kiểm;
   - đi từ trong ra ngoài: model → lõi → CLI → API → UI → đóng gói/docs.
3. Mọi AC của spec phải xuất hiện ở ít nhất một task. Liệt kê rủi ro (hiệu năng, tương thích OS, tool ngoài).
4. Task độc lập nhau có thể giao subagent song song — đánh dấu `[song song]`.
5. Trình người dùng; khi đồng ý, commit `docs(plan): …` rồi chuyển sang skill `implement-tdd`.
