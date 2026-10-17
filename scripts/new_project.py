"""Tạo dự án mới từ BaseToolProject: copy, đổi tên package/app, git init.

Dùng:
  python scripts/new_project.py D:/Projects/photo-resizer --name "Photo Resizer"
  python scripts/new_project.py ../my-tool --name "My Tool" --package mytool --no-git

Quy ước tên suy ra từ --name "Photo Resizer":
  package Python  : photoresizer     (thay `basetool`)
  tên phân phối   : photo-resizer    (thay `base-tool`)
  tên exe/app     : PhotoResizer     (thay `BaseTool`)
  tên hiển thị    : Photo Resizer    (thay `Base Tool`)
  biến môi trường : PHOTORESIZER_*   (thay `BASETOOL_`)
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE = shutil.ignore_patterns(".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".ruff_cache", "*.egg-info",
                                "dist", "out", ".privacy-blocklist", "settings.local.json", "launch.json",
                                # Phần plugin lutech-tools — chỉ sống ở repo gốc.
                                ".claude-plugin", "skills", "install.sh", "PLUGIN.md")
TEXT_EXT = {".py", ".md", ".toml", ".txt", ".json", ".yml", ".yaml", ".html", ".css", ".js", ".spec", ".cfg", ".ini",
            ".sh", ".gitignore", ".gitattributes", ""}


def names(display: str, package: str | None) -> dict[str, str]:
    words = re.findall(r"[A-Za-z0-9]+", display)
    if not words:
        raise SystemExit("--name phải có chữ cái/số")
    pkg = package or "".join(words).lower()
    if not re.fullmatch(r"[a-z_][a-z0-9_]*", pkg):
        raise SystemExit(f"Tên package không hợp lệ: {pkg}")
    # Thứ tự quan trọng: chuỗi dài/cụ thể trước.
    return {
        "io.github.basetool": f"io.github.{pkg}",
        "BASETOOL_": f"{pkg.upper()}_",
        "BaseToolProject": "".join(w.capitalize() if w.islower() else w for w in words),
        "BaseTool": "".join(w.capitalize() if w.islower() else w for w in words),
        "Base Tool": display,
        "base-tool": "-".join(w.lower() for w in words),
        "basetool": pkg,
    }


def rewrite(dest: Path, mapping: dict[str, str]) -> None:
    for p in dest.rglob("*"):
        if not p.is_file() or (p.suffix.lower() not in TEXT_EXT and p.name not in {".gitignore", ".gitattributes"}):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = text
        for old, rep in mapping.items():
            new = new.replace(old, rep)
        if new != text:
            p.write_text(new, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dest", type=Path)
    ap.add_argument("--name", required=True, help='Tên hiển thị, vd "Photo Resizer"')
    ap.add_argument("--package", help="Tên package Python (mặc định suy từ --name)")
    ap.add_argument("--no-git", action="store_true")
    a = ap.parse_args(argv)

    dest = a.dest.resolve()
    if dest.exists() and any(dest.iterdir()):
        print(f"Thư mục đích không rỗng: {dest}", file=sys.stderr)
        return 1
    mapping = names(a.name, a.package)
    shutil.copytree(ROOT, dest, ignore=IGNORE, dirs_exist_ok=True)
    (dest / "basetool").rename(dest / mapping["basetool"])
    # Bỏ phần chỉ dành cho template.
    (dest / "scripts" / "new_project.py").unlink()
    rewrite(dest, mapping)
    (dest / "docs" / "TEMPLATE.md").unlink(missing_ok=True)
    readme = dest / "README.md"
    readme.write_text("\n".join(ln for ln in readme.read_text(encoding="utf-8").splitlines()
                                if "TEMPLATE.md" not in ln) + "\n", encoding="utf-8")

    if not a.no_git:
        subprocess.run(["git", "init", "-b", "main"], cwd=dest, check=True)
    print(f"✓ Đã tạo {a.name} tại {dest}\n"
          f"Tiếp theo:\n  cd \"{dest}\"\n  python -m venv .venv && .venv/Scripts/pip install -e .[dev]\n"
          f"  python -m pytest -q\n  Mở Claude Code và chạy skill `spec-feature` để viết spec đầu tiên.")
    return 0


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except Exception:  # noqa: BLE001
            pass
    sys.exit(main())
