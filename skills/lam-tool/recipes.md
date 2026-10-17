# Công thức tool hay dùng cho UA / marketing

Mỗi công thức: người dùng làm gì → tool trả gì → thư viện → tiêu chí "xong". Dùng làm điểm xuất phát, hỏi để chỉnh.
Mọi tool: chạy offline, file gốc không bị sửa, lỗi một file không dừng cả lô, có file `report.csv` tóm tắt kết quả.

## 1. Resize / crop creative theo kích thước network
- Vào: thư mục ảnh (PNG/JPG/WebP). Chọn preset kích thước (vd 1200×628, 1080×1080, 1080×1920, 320×50, 728×90) hoặc tự nhập.
- Chế độ: vừa khung (thêm nền) / cắt giữa / cắt theo điểm chọn. Giới hạn dung lượng (vd ≤ 150 KB).
- Ra: `Output/<tên>_<w>x<h>.<ext>`. Thư viện: **Pillow**.
- Xong khi: 100 ảnh × 6 size < 2 phút; ảnh vượt dung lượng tự giảm chất lượng, vẫn vượt thì ghi vào report.

## 2. Đổi tên creative theo quy tắc đặt tên (naming convention)
- Vào: thư mục file + mẫu tên `{app}_{concept}_{size}_{lang}_{v}` + giá trị từng trường (chọn từ danh sách lưu sẵn).
- Có **xem trước** tên cũ → tên mới trước khi đổi; nút **Hoàn tác** lần đổi gần nhất.
- Thư viện: chuẩn Python. Xong khi: không bao giờ ghi đè trùng tên; tên có dấu/khoảng trắng được chuẩn hoá theo tuỳ chọn.

## 3. Video ad: cắt, đổi tỉ lệ, nén, xuất nhiều độ dài
- Vào: video gốc. Ra: 16:9 / 1:1 / 9:16 / 4:5, độ dài 6s/15s/30s, giới hạn dung lượng, tuỳ chọn thêm end card ảnh.
- Thư viện: **ffmpeg** đóng kèm trong `bin/` (tải bằng script khi build, không gọi mạng lúc chạy).
- Xong khi: có thanh tiến độ theo %, bấm Dừng được, video lỗi được báo rõ.

## 4. Gộp & làm sạch report từ nhiều network
- Vào: nhiều file CSV/XLSX export từ các network (cột khác tên nhau). Tool map cột về chuẩn chung
  (date, network, campaign, country, spend, installs, …) — lưu mapping thành preset dùng lại.
- Ra: một file XLSX tổng + sheet pivot theo ngày/network/country, tính CPI, CTR, IPM.
- Thư viện: **openpyxl** (tránh pandas nếu không cần để exe nhẹ). Xong khi: số liệu tổng khớp từng file gốc; dòng lỗi liệt kê riêng.

## 5. Tạo link tracking / UTM hàng loạt
- Vào: bảng campaign (dán từ Excel) + mẫu link. Ra: cột link đã encode đúng, copy một chạm, xuất CSV.
- Thư viện: chuẩn Python (`urllib.parse`). Xong khi: kiểm tra trùng, ký tự lạ, thiếu tham số bắt buộc.

## 6. Kiểm tra creative trước khi upload
- Vào: thư mục creative + bộ luật (kích thước cho phép, dung lượng tối đa, độ dài video, định dạng, quy tắc tên).
- Ra: bảng Đạt/Không đạt kèm lý do, mở nhanh file lỗi. Thư viện: Pillow (+ ffprobe nếu có video).

## 7. Localize text ASO / ad copy
- Vào: file bảng (key, vi, en, …). Kiểm độ dài tối đa từng trường theo store, ký tự cấm, key thiếu ngôn ngữ.
- Ra: báo cáo + file đã chuẩn hoá. Không tự gọi dịch máy online trừ khi người dùng bật rõ ràng.

Không khớp công thức nào → hỏi theo khung "vào gì / ra gì / ví dụ một lần chạy tay", rồi tự đặt công thức mới theo cùng mẫu.
