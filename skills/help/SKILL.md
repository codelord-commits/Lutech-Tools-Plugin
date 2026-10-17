---
name: help
description: Dùng khi người dùng hỏi plugin lutech-tools có lệnh gì, nên dùng lệnh nào tiếp theo, "hướng dẫn", "bắt đầu từ đâu", hoặc gõ /lutech-tools:help.
---

# Hướng dẫn lutech-tools

In cho người dùng bảng sau, rồi **đoán giai đoạn hiện tại** từ repo (có `docs/specs/` đã duyệt chưa? có plan chưa xong?
có diff chưa review?) và đề xuất đúng một lệnh tiếp theo.

| Lệnh | Giai đoạn | Dùng khi | Ví dụ gọi |
|------|-----------|----------|-----------|
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
