# Hướng dẫn cho người không biết code

Bạn kể việc đang làm tay → Claude tự làm ra tool → bạn nhận file `.exe` dùng và gửi đồng nghiệp.
n> Dùng AI cho các việc UA cụ thể (báo cáo, research, cảnh báo camp…): xem [HUONG-DAN-UA.md](HUONG-DAN-UA.md).
Không cần biết lập trình, không cần gõ lệnh.

## Cài một lần (5 phút)

1. Cài **Claude** (desktop): <https://claude.com/download> — đăng nhập bằng tài khoản công ty.
2. Cài **Python**: <https://www.python.org/downloads/> — Windows: **tích ô "Add python.exe to PATH"** trước khi bấm Install.
3. Tải bộ tool Lutech (file zip từ team kỹ thuật), giải nén vào chỗ cố định, vd `Documents/lutech-tools`
   (**đừng xoá hay di chuyển** thư mục này sau khi cài — plugin chạy từ đó).
4. Double-click **`install.bat`** (Windows) hoặc **`install.command`** (macOS). Thấy chữ **XONG** là được.
5. **Tắt hẳn Claude** (Windows: chuột phải icon Claude ở khay đồng hồ → Quit; macOS: Cmd+Q) rồi mở lại.

> macOS báo "không mở được vì từ nhà phát triển không xác định": chuột phải vào `install.command` → **Open** → **Open**.

## Dùng hằng ngày — chỉ 3 lệnh

Mở Claude Desktop → chuyển sang tab **Code** (không phải tab Chat — chỉ tab Code mới tạo và chạy được tool trên máy bạn)
→ chọn thư mục làm việc, vd `Documents/LutechTools` (tạo thư mục trống nếu chưa có) → gõ `/` để thấy danh sách lệnh, hoặc gõ:

| Bạn muốn | Gõ |
|----------|----|
| Làm tool mới | `/lutech-tools:make-tool` + kể việc bạn đang làm |
| Sửa lỗi, thêm tính năng | `/lutech-tools:fix-tool` + mô tả |
| Có file gửi đồng nghiệp | `/lutech-tools:package-tool` |

Quên lệnh? Gõ `/lutech-tools:help`.

## Tool làm ra trông như thế nào?

| Loại | Trông như thế nào | Khi nào dùng | Làm được? |
|------|-------------------|--------------|-----------|
| **App Windows / macOS** (mặc định) | File `CreativeResizer.exe` (macOS: `.app`). Bấm đúp → **trình duyệt tự mở màn hình của tool** (nút Chọn thư mục, Chạy, thanh tiến độ). Đóng cửa sổ đen để thoát. | Hầu hết việc: xử lý ảnh, video, file Excel/CSV trên máy bạn | ✅ Có |
| **Dòng lệnh** | Gõ lệnh trong cửa sổ đen, không có nút bấm | Team kỹ thuật muốn chạy tự động hằng ngày | ✅ Có — nói "chỉ cần dòng lệnh" |
| **Web tool online** (một link cả team mở chung) | Website trên mạng, có đăng nhập | Cần dữ liệu chung cho nhiều người cùng lúc | ❌ Chưa — bộ này làm tool chạy trên từng máy. Cần thì báo team kỹ thuật |
| **App cửa sổ Windows kiểu truyền thống** (không dùng trình duyệt) | Cửa sổ riêng như Word/Excel | — | ❌ Không cần — app mặc định đã có giao diện đầy đủ, chỉ hiển thị trong trình duyệt |

Lưu ý: dù hiện trong trình duyệt, tool mặc định **chạy hoàn toàn trên máy bạn, không cần mạng**, file không gửi đi đâu.

## Ví dụ một lần làm tool

```
Bạn:    /lutech-tools:make-tool mỗi ngày mình resize khoảng 50 ảnh creative ra
        1200x628, 1080x1080, 1080x1920 để up lên các network, làm tay mất 1 tiếng
Claude: Mình hiểu là tool "Resize creative". Hỏi nhanh 3 câu:
        1. Ảnh lệch tỉ lệ thì: (1) thêm nền (2) cắt giữa  ← đề xuất 2
        2. Có giới hạn dung lượng không? (1) ≤150KB (2) không ...
Bạn:    2, 1, ...
Claude: [Phiếu tool] ... Đồng ý không?
Bạn:    đồng ý
Claude: Bước 3/5: đang xây tool...  →  Bước 4/5: mở tool để bạn thử
Bạn:    ổn
Claude: ✓ File gửi đi: dist/CreativeResizer-windows.zip
```

Khi Claude hỏi, **chỉ cần trả lời bằng số** hoặc vài chữ. Claude xin phép trước khi chạy thứ gì quan trọng —
đọc dòng mô tả rồi bấm **Allow**.

## Tool làm được ngay (có công thức sẵn)

| Tool | Làm gì |
|------|--------|
| Resize creative | Một ảnh → nhiều kích thước network, giới hạn dung lượng |
| Đổi tên theo naming convention | Xem trước, đổi hàng loạt, hoàn tác được |
| Video ad | Cắt độ dài, đổi tỉ lệ 16:9 / 1:1 / 9:16, nén |
| Gộp report network | Nhiều CSV/Excel → 1 file Excel tổng, tính CPI/CTR/IPM |
| Link tracking / UTM | Tạo link hàng loạt từ bảng campaign |
| Kiểm creative trước khi up | Báo Đạt/Không đạt theo kích thước, dung lượng, tên |
| Kiểm text ASO / ad copy | Độ dài theo store, thiếu ngôn ngữ, ký tự cấm |

Việc khác cũng làm được — cứ kể: *đưa vào cái gì, muốn nhận ra cái gì, thường làm tay thế nào*.

## Mẹo để tool ra đúng ý
- Gửi kèm **1–2 file mẫu thật** (ảnh, report) — để ngoài thư mục tool.
- Nói rõ **"xong" là thế nào**: "50 ảnh chạy dưới 1 phút", "tên file theo dạng app_concept_size".
- Tool chạy hoàn toàn trên máy bạn, không gửi file đi đâu. Tên khách/app riêng được giữ kín, không ghi vào code.

## Gặp sự cố
| Thấy | Làm |
|------|-----|
| `install.bat` báo thiếu Claude/Python | Cài theo link nó mở ra, rồi chạy lại `install.bat` |
| Gõ `/lutech-tools:` không thấy lệnh | Kiểm đang ở tab **Code**; tắt hẳn Claude (Quit) rồi mở lại |
| Đang ở tab Chat | Chuyển sang tab **Code** — tab Chat không chạy được tool trên máy |
| Windows báo "Windows protected your PC" khi mở tool | **More info** → **Run anyway** |
| Tool chạy sai | `/lutech-tools:fix-tool` + mô tả + ảnh chụp màn hình |
| Muốn bản plugin mới nhất | Chạy lại `install.bat` |
