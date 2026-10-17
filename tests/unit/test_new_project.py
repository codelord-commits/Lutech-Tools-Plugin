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


def test_non_tech_commands_documented():
    guide = (ROOT / "docs" / "HUONG-DAN.md").read_text(encoding="utf-8")
    for cmd in ("lam-tool", "sua-tool", "dong-goi"):
        assert (ROOT / "skills" / cmd / "SKILL.md").exists()
        assert f"/lutech-tools:{cmd}" in guide


def test_new_project_keeps_helper_scripts(tmp_path):
    dest = tmp_path / "t"
    subprocess.run([sys.executable, str(ROOT / "scripts" / "new_project.py"), str(dest), "--name", "T T", "--no-git"],
                   check=True, capture_output=True)
    for keep in ("scripts/setup_env.py", "scripts/build_exe.py"):
        assert (dest / keep).exists(), keep
    for gone in ("install.bat", "install.ps1", "install.command", "docs/HUONG-DAN.md"):
        assert not (dest / gone).exists(), gone


def test_install_plugin_merges_settings(tmp_path):
    sys.path.insert(0, str(ROOT / "scripts"))
    from install_plugin import apply

    s = tmp_path / "settings.json"
    s.write_text(json.dumps({"theme": "dark", "enabledPlugins": {"x@y": True}}), encoding="utf-8")
    apply(s)
    d = json.loads(s.read_text(encoding="utf-8"))
    assert d["theme"] == "dark" and d["enabledPlugins"] == {"x@y": True, "lutech-tools@lutech": True}
    assert d["extraKnownMarketplaces"]["lutech"]["source"] == {"source": "directory", "path": str(ROOT)}
    apply(s, uninstall=True)
    d = json.loads(s.read_text(encoding="utf-8"))
    assert "lutech" not in d["extraKnownMarketplaces"] and d["enabledPlugins"] == {"x@y": True}
