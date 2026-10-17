"""Cài plugin lutech-tools không cần lệnh `claude` (dùng cho Claude Desktop).

Ghi marketplace + bật plugin trong ~/.claude/settings.json
— tab Code của Claude Desktop và Claude Code CLI dùng chung file này.
Dùng: python scripts/install_plugin.py [--uninstall] [--settings <file>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKET, PLUGIN = "lutech", "lutech-tools"
KEY = f"{PLUGIN}@{MARKET}"


def apply(settings: Path, uninstall: bool = False) -> None:
    data = json.loads(settings.read_text(encoding="utf-8")) if settings.exists() else {}
    if not isinstance(data, dict):
        raise SystemExit(f"{settings} không phải JSON object — sửa tay hoặc gửi team kỹ thuật.")
    markets = data.setdefault("extraKnownMarketplaces", {})
    enabled = data.setdefault("enabledPlugins", {})
    if uninstall:
        markets.pop(MARKET, None)
        enabled.pop(KEY, None)
    else:
        markets[MARKET] = {"source": {"source": "directory", "path": str(ROOT)}}
        enabled[KEY] = True
    settings.parent.mkdir(parents=True, exist_ok=True)
    if settings.exists():
        settings.with_suffix(".json.bak").write_text(settings.read_text(encoding="utf-8"), encoding="utf-8")
    tmp = settings.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(settings)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--uninstall", action="store_true")
    ap.add_argument("--settings", type=Path, default=Path.home() / ".claude" / "settings.json")
    a = ap.parse_args(argv)
    try:
        apply(a.settings, a.uninstall)
    except json.JSONDecodeError as e:
        print(f"{a.settings} bị lỗi định dạng (dòng {e.lineno}) — không sửa gì. Gửi file này cho team kỹ thuật.",
              file=sys.stderr)
        return 1
    print(f"✓ Đã {'gỡ' if a.uninstall else 'cài'} {PLUGIN} vào {a.settings}\n"
          "Tắt hẳn Claude Desktop rồi mở lại để nhận lệnh /lutech-tools:…")
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except Exception:  # noqa: BLE001 — console cũ không hỗ trợ đổi encoding
            pass
    sys.exit(main())
