#!/usr/bin/env bash
# Cài plugin lutech-tools cho Claude Code.
#
#   ./install.sh                 cài từ thư mục chứa script này (bản clone local)
#   ./install.sh <owner/repo>    cài từ GitHub (vd lutech/BaseToolProject)
#   ./install.sh --update        cập nhật lên bản mới nhất
#   ./install.sh --uninstall     gỡ plugin
#
# Chạy được trên macOS, Linux và Windows (Git Bash).
set -euo pipefail

MARKET="lutech"
PLUGIN="lutech-tools"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

say()  { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
die()  { printf '\033[1;31mLỗi:\033[0m %s\n' "$*" >&2; exit 1; }

if ! command -v claude >/dev/null 2>&1; then
  # Chỉ có Claude Desktop (không có CLI): ghi thẳng ~/.claude/settings.json.
  PY="$(command -v python3 || command -v python || true)"
  [ -n "$PY" ] || die "Chưa có Python. Tải tại https://www.python.org/downloads/ rồi chạy lại."
  [ -z "${1:-}" ] || [ "$1" = "--uninstall" ] || [ "$1" = "--update" ] || die "Cài từ GitHub cần lệnh claude. Tải zip, giải nén rồi chạy install trong đó."
  say "Cài cho Claude Desktop"
  if [ "${1:-}" = "--uninstall" ]; then "$PY" "$HERE/scripts/install_plugin.py" --uninstall
  else "$PY" "$HERE/scripts/install_plugin.py"; fi
  echo "Tắt hẳn Claude rồi mở lại, vào tab Code và gõ /lutech-tools:lam-tool"
  exit 0
fi

case "${1:-}" in
  --update)
    say "Cập nhật marketplace $MARKET"
    claude plugin marketplace update "$MARKET"
    claude plugin update "$PLUGIN@$MARKET" 2>/dev/null || claude plugin install "$PLUGIN@$MARKET"
    ;;
  --uninstall)
    say "Gỡ $PLUGIN"
    claude plugin uninstall "$PLUGIN@$MARKET" || true
    claude plugin marketplace remove "$MARKET" || true
    ;;
  -h|--help)
    sed -n '2,9p' "$0"; exit 0
    ;;
  *)
    SRC="${1:-$HERE}"
    [ -n "${1:-}" ] || [ -f "$HERE/.claude-plugin/marketplace.json" ] || die "Không thấy .claude-plugin/marketplace.json trong $HERE"
    say "Thêm marketplace $MARKET từ $SRC"
    claude plugin marketplace add "$SRC" || say "Marketplace đã có — bỏ qua"
    say "Cài $PLUGIN@$MARKET"
    claude plugin install "$PLUGIN@$MARKET"
    ;;
esac

cat <<EOF

✓ Xong. Mở lại Claude Code rồi gõ:
    /lutech-tools:lam-tool    rồi kể việc bạn muốn tự động hoá
    /lutech-tools:help        xem tất cả lệnh
EOF
