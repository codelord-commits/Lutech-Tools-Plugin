---
name: release
description: Giai đoạn 7 của LIFECYCLE. Dùng khi người dùng muốn phát hành phiên bản mới, tạo tag, đưa .exe/.app lên GitHub Releases, hoặc công khai repo lần đầu.
---

# Phát hành

Điều kiện: `qa-check` đã xanh. Mọi bước đẩy ra ngoài (push, tag, tạo repo, publish) **phải hỏi người dùng trước từng bước**.

1. Xác định loại bản theo SemVer (`docs/RELEASE.md`) — đề xuất và hỏi người dùng: patch / minor / major.
2. `python scripts/bump_version.py <loại>`; soát lại `CHANGELOG.md` (chuyển nội dung `[Unreleased]` vào mục phiên bản mới, viết cho người dùng cuối).
3. `git add -A && git commit -m "chore(release): vX.Y.Z"` (hook sẽ chạy check_privacy).
4. **Hỏi** rồi mới: `git tag vX.Y.Z` và `git push origin main --tags`.
5. Theo dõi workflow `release` (`gh run watch`), khi xanh kiểm trang Release có đủ `BaseTool-windows.zip` và `BaseTool-macos.zip`.
6. Lần đầu công khai: nếu commit cũ từng chứa dữ liệu nhạy cảm thì squash lịch sử (hỏi trước — thao tác viết lại lịch sử);
   bật *Template repository* nếu là template, thêm mô tả/topic cho repo.
7. Báo người dùng link Release và những gì cần làm thủ công (ký mã, thông báo người dùng).

Release lỗi: không xoá tag đã công bố — sửa rồi phát hành bản patch.
