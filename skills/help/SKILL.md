---
name: help
description: Dùng khi người dùng hỏi plugin lutech-tools có lệnh gì, nên dùng lệnh nào tiếp theo, "hướng dẫn", "bắt đầu từ đâu", hoặc gõ /lutech-tools:help.
---

# Hướng dẫn lutech-tools

Trước tiên đoán người dùng là ai: không nhắc tới code/git → coi là **người không biết code** và chỉ in bảng ngắn này:

| Bạn muốn | Gõ |
|----------|----|
| Làm một tool mới | `/lutech-tools:make-tool` rồi kể việc bạn đang làm tay |
| Sửa lỗi / thêm tính năng cho tool | `/lutech-tools:fix-tool` rồi mô tả |
| Có file .exe gửi đồng nghiệp | `/lutech-tools:package-tool` |

Kèm 3 ví dụ: "resize creative ra 6 size", "đổi tên file theo naming convention", "gộp report các network thành 1 file Excel".
Dừng ở đó, trừ khi người dùng hỏi thêm.

Với dev, in bảng sau, rồi **đoán giai đoạn hiện tại** từ repo (có `docs/specs/` đã duyệt chưa? có plan chưa xong?
có diff chưa review?) và đề xuất đúng một lệnh tiếp theo.

| Lệnh | Giai đoạn | Dùng khi | Ví dụ gọi |
|------|-----------|----------|-----------|
| `/lutech-tools:make-tool` | 0→7 (cho non-tech) | Mô tả việc bằng lời, nhận tool .exe | `/lutech-tools:make-tool resize creative` |
| `/lutech-tools:fix-tool` | 8 (cho non-tech) | Sửa/thêm tính năng bằng lời | `/lutech-tools:fix-tool thêm size 300x250` |
| `/lutech-tools:package-tool` | 6–7 rút gọn | Ra file zip gửi được, không cần GitHub | `/lutech-tools:package-tool` |
| `/lutech-tools:new-tool` | 0 Khởi tạo | Bắt đầu tool mới từ template | `/lutech-tools:new-tool Photo Resizer ở D:/Projects/photo-resizer` |
| `/lutech-tools:spec-feature` | 1–2 Spec + thiết kế | Có ý tưởng/yêu cầu khách, chưa có spec | `/lutech-tools:spec-feature thêm chế độ đổi tên hàng loạt` |
| `/lutech-tools:plan-feature` | 3 Plan | Spec đã duyệt, cần chia task | `/lutech-tools:plan-feature docs/specs/2026-10-17-rename.md` |
| `/lutech-tools:implement-tdd` | 4 Code / 8 Bảo trì | Làm task trong plan, sửa bug | `/lutech-tools:implement-tdd task 2` |
| `/lutech-tools:review-change` | 5 Review | Xong tính năng, trước merge/PR | `/lutech-tools:review-change` |
| `/lutech-tools:ui-review` | 5 Review UI | Có đổi `web/static/` | `/lutech-tools:ui-review` |
| `/lutech-tools:qa-check` | 6 QA | Trước khi phát hành | `/lutech-tools:qa-check` |
| `/lutech-tools:release` | 7 Release | Phát hành bản mới lên GitHub Releases | `/lutech-tools:release patch` |
| `/lutech-tools:help` | — | Không biết làm gì tiếp | `/lutech-tools:help` |

Luồng chuẩn: `new-tool → spec-feature → plan-feature → implement-tdd → review-change (+ ui-review) → qa-check → release`.

Theo loại tool:
- **Web UI + CLI**: đi đủ luồng, luôn có `ui-review`.
- **Chỉ CLI**: bỏ `ui-review`; `qa-check` bỏ bước chạy UI, chỉ chạy `<exe> cli --help` và một job mẫu.
- **Thư viện/lõi**: bỏ `ui-review` và bước build PyInstaller trong `qa-check`; `release` chỉ tag + CHANGELOG.
- **Sửa bug nhanh**: `implement-tdd` (test tái hiện trước) → `review-change` → `qa-check` → `release patch`.

Hướng dẫn đầy đủ: `docs/PLUGIN.md` trong repo plugin.
