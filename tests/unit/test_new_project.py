import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_plugin_manifest_lists_all_skills():
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert market["plugins"][0]["name"] == plugin["name"] == "lutech-tools"
    for skill in (ROOT / "skills").iterdir():
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        assert f"name: {skill.name}\n" in text
        assert f"/lutech-tools:{skill.name}" in (ROOT / "docs" / "PLUGIN.md").read_text(encoding="utf-8")


def test_new_project_skips_plugin_files(tmp_path):
    dest = tmp_path / "Công cụ mới"
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "new_project.py"), str(dest), "--name", "Photo Resizer",
                        "--no-git"], capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stderr
    assert (dest / "photoresizer" / "__init__.py").exists()
    for gone in (".claude-plugin", "skills", "install.sh", "docs/PLUGIN.md"):
        assert not (dest / gone).exists(), gone
