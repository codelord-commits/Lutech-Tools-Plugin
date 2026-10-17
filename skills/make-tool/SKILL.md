---
name: make-tool
description: Lệnh chính cho người không biết code (UA, marketing, vận hành). Dùng khi người dùng mô tả bằng lời thường một việc lặp đi lặp lại muốn tự động hoá ("tôi muốn tool để resize creative", "làm tool đổi tên hàng loạt", "gộp report các network") hoặc gõ /lutech-tools:make-tool. Tự lo toàn bộ phần kỹ thuật từ tạo dự án đến file .exe chạy được.
---

# Làm tool cho người không biết code

Người dùng **không biết code**. Nguyên tắc nói chuyện:
- Tiếng Việt đời thường, câu ngắn. Không dùng từ: venv, commit, test, spec, plan, TDD, repo, PR, lint. Nếu buộc phải nói, giải thích trong ngoặc.
- Mỗi lượt hỏi **tối đa 3 câu**, mỗi câu có lựa chọn đánh số + một lựa chọn đề xuất. Người dùng chỉ cần gõ số.
- Không bắt người dùng gõ lệnh. Bạn tự chạy mọi thứ; chỉ báo tiến độ dạng `Bước 2/5: …`.
- Việc kỹ thuật vẫn làm **đủ chất lượng** như dev (skill nội bộ bên dưới) — chỉ là không bắt người dùng nhìn thấy.

## Bước 1/5 — Hiểu việc cần làm
Hỏi (gộp một lượt), gợi ý theo [recipes.md](recipes.md) nếu khớp:
1. Bạn đang làm tay việc gì? (vd: "mỗi ngày resize 50 ảnh ra 6 kích thước cho các network")
2. Bạn đưa vào cái gì, muốn nhận ra cái gì? (thư mục ảnh / file CSV / video…)
3. Gửi 1–2 file mẫu (để ngoài repo) hoặc mô tả tên file mẫu.

Khớp công thức trong `recipes.md` → đề xuất luôn: "Tool kiểu **Resize creative**: chọn thư mục → chọn kích thước → bấm Chạy → ra thư mục kết quả. Đúng ý không? (1) Đúng (2) Gần đúng, sửa: …".

Loại tool: mặc định **App Windows/macOS** (file .exe/.app mở giao diện trong trình duyệt, chạy offline) — không cần hỏi.
Người dùng chỉ cần chạy tự động → loại "Chỉ CLI" của `new-tool`. Người dùng muốn **web online dùng chung** hoặc **cửa sổ
Windows riêng** → giải thích ngắn theo bảng "Tool làm ra trông như thế nào?" trong `docs/HUONG-DAN.md` rồi đề xuất app mặc định;
web online thì khuyên báo team kỹ thuật.

## Bước 2/5 — Chốt bằng một "phiếu tool"
Trình một khung ngắn, người dùng chỉ trả lời **Đồng ý / Sửa**:
```
Tên tool:        Creative Resizer
Loại:            App Windows (.exe) — mở giao diện trong trình duyệt, chạy offline
Bạn làm:         chọn thư mục ảnh → tích kích thước → bấm Chạy
Tool trả về:     thư mục Output/, mỗi ảnh × mỗi kích thước, tên <tên>_<rộng>x<cao>.png
Xong khi:        50 ảnh chạy < 1 phút; ảnh lỗi được bỏ qua và liệt kê lại
Không làm:       chỉnh màu, upload lên network
```
Sau khi đồng ý: lưu phiếu này thành spec (theo skill `spec-feature`, phần trao đổi đã xong — chỉ viết file) và lập plan
(skill `plan-feature`) **không hỏi thêm** trừ khi có điểm mâu thuẫn.
Tên khách/app/network riêng mà người dùng nhắc tới → thêm vào `.privacy-blocklist`, không ghi vào code.

## Bước 3/5 — Tạo và xây tool
- Chưa có dự án → làm theo skill `new-tool` (loại **Web UI + CLI**, chọn sẵn; thư mục mặc định `~/LutechTools/<ten-tool>`),
  môi trường dùng `python scripts/setup_env.py --ui`.
- Code theo skill `implement-tdd` cho từng task. Thư viện gợi ý nằm trong `recipes.md`.
- Giao diện: một màn hình, các bước đánh số, nút chính to, chọn thư mục bằng nút "Chọn…", có thanh tiến độ, báo lỗi
  bằng câu hướng dẫn cụ thể ("Ảnh abc.psd không đọc được — hãy xuất sang PNG"). Mặc định tiếng Việt.
- Báo tiến độ cho người dùng sau mỗi 1–2 task, một dòng.

## Bước 4/5 — Tự kiểm tra
Chạy ngầm `review-change`, `ui-review`, `qa-check` (bỏ bước build nếu người dùng chưa cần gửi cho ai).
Sửa hết lỗi mức Cao. Sau đó **mở tool cho người dùng dùng thử** (preview), kèm hướng dẫn 3 dòng:
"1. Bấm Chọn thư mục… 2. … 3. Bấm Chạy". Hỏi: "Chạy với file của bạn ổn không? (1) Ổn (2) Có chỗ chưa đúng: …".

## Bước 5/5 — Giao hàng
- Đóng gói: `python scripts/build_exe.py` → báo đường dẫn file zip, dặn: "Gửi zip này cho đồng nghiệp, giải nén, mở <Tên>.exe".
- Lưu lại (commit) với mô tả dễ hiểu. **Không** đưa lên GitHub khi chưa hỏi.
- Kết thúc bằng: muốn thêm/sửa gì sau này chỉ cần gõ `/lutech-tools:fix-tool <mô tả>`.

Gặp lỗi kỹ thuật: tự xử lý; chỉ hỏi người dùng khi cần **quyết định nghiệp vụ** hoặc cần cài phần mềm (Python, Git) — khi đó
đưa link tải và hướng dẫn từng bấm.
