---
name: fix-tool
description: Dùng khi người không biết code muốn sửa lỗi hoặc thêm/đổi tính năng cho tool đã có, mô tả bằng lời thường ("tool bị lỗi khi ảnh có tên tiếng Việt", "thêm kích thước 300x250", "nút chạy không bấm được") hoặc gõ /lutech-tools:fix-tool.
---

# Sửa / nâng cấp tool bằng lời thường

Cùng cách nói chuyện như skill `make-tool`: tiếng Việt đời thường, tối đa 3 câu hỏi có lựa chọn đánh số, không bắt gõ lệnh.

1. **Xác định tool**: thư mục hiện tại là dự án tool? Nếu không, tìm trong `~/LutechTools/` và hỏi chọn theo số.
2. **Phân loại** yêu cầu, nói lại một câu để người dùng xác nhận:
   - *Lỗi* → hỏi: làm gì thì lỗi, file nào (gửi mẫu hoặc mô tả), thấy thông báo gì (chụp màn hình được thì tốt).
   - *Thêm/đổi* → trình "phiếu thay đổi" 3 dòng: Trước / Sau / Không đổi. Chờ Đồng ý.
3. Môi trường chưa sẵn → `python scripts/setup_env.py`.
4. Làm theo skill `implement-tdd` (lỗi: tái hiện bằng test trước). Thay đổi lớn hơn ~3 task → lưu spec ngắn + plan
   (`spec-feature`, `plan-feature`) không hỏi thêm.
5. Chạy ngầm `review-change` (+ `ui-review` nếu đổi giao diện) và test toàn bộ.
6. Mở tool cho người dùng thử lại đúng tình huống họ báo. Hỏi "(1) Ổn (2) Vẫn chưa: …".
7. Ổn → ghi vào CHANGELOG bằng câu người dùng hiểu, lưu lại (commit). Hỏi có cần đóng gói gửi đi không →
   `/lutech-tools:package-tool`.
