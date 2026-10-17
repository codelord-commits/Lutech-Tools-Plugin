# Plugin `lutech-tools` cho Claude Code

Repo này vừa là **template** công cụ desktop local, vừa là **plugin** Claude Code đóng gói toàn bộ quy trình
[LIFECYCLE](LIFECYCLE.md) thành lệnh `/lutech-tools:*` dùng được ở mọi dự án.

## 1. Cài đặt (1 lệnh)

Cần [Claude Code](https://docs.claude.com/claude-code) (lệnh `claude`) và Python ≥ 3.10.

```bash
git clone <url-repo> lutech-tools && cd lutech-tools && ./install.sh
```

| Muốn | Lệnh |
|------|------|
| Cài từ bản clone local | `./install.sh` |
| Cài thẳng từ GitHub | `./install.sh <owner>/<repo>` |
| Cập nhật | `./install.sh --update` |
| Gỡ | `./install.sh --uninstall` |

Windows: chạy trong **Git Bash**. Không có terminal? Trong Claude Code gõ
`/plugin marketplace add <đường-dẫn-repo>` rồi `/plugin install lutech-tools@lutech`.

Kiểm tra: mở lại Claude Code, gõ `/lutech-tools:help`.

## 2. Danh sách lệnh

| Lệnh | Giai đoạn | Làm gì | Đầu ra |
|------|-----------|--------|--------|
| `/lutech-tools:help` | — | Liệt kê lệnh, đoán giai đoạn hiện tại, gợi ý lệnh tiếp | — |
| `/lutech-tools:new-tool` | 0 | Tạo dự án mới từ template, đổi tên, cài venv, chạy test | thư mục dự án + commit đầu |
| `/lutech-tools:spec-feature` | 1–2 | Hỏi làm rõ, đề xuất hướng, viết spec + ADR | `docs/specs/…`, `docs/adr/…` |
| `/lutech-tools:plan-feature` | 3 | Chia spec thành task nhỏ có test | `docs/plans/…` |
| `/lutech-tools:implement-tdd` | 4, 8 | Code từng task: test đỏ → xanh → dọn | code + test + commit |
| `/lutech-tools:review-change` | 5 | Review diff theo spec, rule, bảo mật | báo cáo Cao/TB/Thấp |
| `/lutech-tools:ui-review` | 5 | Kiểm UI: responsive, sáng/tối, vi/en, a11y | ảnh chụp + checklist |
| `/lutech-tools:qa-check` | 6 | Test toàn bộ, privacy, build exe, chạy thử | bảng QA |
| `/lutech-tools:release` | 7 | Bump version, CHANGELOG, tag, GitHub Release | Release kèm zip |

Có thể gõ kèm mô tả, vd `/lutech-tools:spec-feature thêm nén ảnh WebP`. Claude cũng tự gọi skill khi bạn nói tự nhiên
("lên kế hoạch", "review giúp", "phát hành bản mới").

## 3. Hướng dẫn theo loại tool

### Web UI + CLI (mặc định) — tool cho người dùng cuối
```
/lutech-tools:new-tool "Photo Resizer" tại D:/Projects/photo-resizer
/lutech-tools:spec-feature resize ảnh hàng loạt theo preset      # chọn style UI bằng ui-ux-pro-max
/lutech-tools:plan-feature
/lutech-tools:implement-tdd                                       # lặp tới hết task
/lutech-tools:review-change  →  /lutech-tools:ui-review
/lutech-tools:qa-check       →  /lutech-tools:release minor
```
Kết quả: `PhotoResizer.exe` / `.app` trên GitHub Releases, mở lên tự bật giao diện trình duyệt.

### Chỉ CLI — tool cho dev / automation
- `new-tool` chọn loại **Chỉ CLI**: bỏ `web/`, test web/ui.
- Bỏ `ui-review`. `qa-check` chỉ chạy `<exe> cli --help` và một job mẫu.

### Thư viện / lõi dùng lại
- `new-tool` chọn loại **Thư viện**: giữ `basetool/` + test, bỏ `web/`, `build/`.
- Bỏ `ui-review` và bước PyInstaller; `release` chỉ bump version + CHANGELOG + tag.

### Sửa bug / bảo trì
```
/lutech-tools:implement-tdd sửa lỗi tên file có dấu bị mất ký tự   # viết test tái hiện trước
/lutech-tools:review-change → /lutech-tools:qa-check → /lutech-tools:release patch
```

## 4. Nguyên tắc plugin luôn giữ
- Không push, tag, tạo repo hay publish khi chưa hỏi bạn — mỗi lần.
- Không commit dữ liệu khách: thêm tên khách vào `.privacy-blocklist`; hook `guard_git.py` của dự án chặn commit vi phạm.
- Không báo "xong" khi chưa chạy test và thấy kết quả.

## 5. Cho người bảo trì plugin
- Skill nằm ở `skills/<tên>/SKILL.md`; manifest ở `.claude-plugin/` (`plugin.json`, `marketplace.json`).
- Version plugin đồng bộ với `pyproject.toml` qua `scripts/bump_version.py`.
- `scripts/new_project.py` không copy phần plugin (`.claude-plugin/`, `skills/`, `install.sh`, `PLUGIN.md`) sang dự án mới.
- Sửa skill rồi `./install.sh --update` để nhận bản mới.
