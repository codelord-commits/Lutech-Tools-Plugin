# Cài plugin lutech-tools (Windows). Thường được gọi từ install.bat (double-click).
#   install.ps1                 cài từ thư mục này
#   install.ps1 <owner/repo>    cài từ GitHub (cần lệnh claude)
#   install.ps1 -Update | -Uninstall
# Có lệnh `claude` (Claude Code CLI) thì dùng nó; không có (chỉ cài Claude Desktop) thì ghi ~/.claude/settings.json.
param([string]$Source = "", [switch]$Update, [switch]$Uninstall)
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$Market = "lutech"; $Plugin = "lutech-tools"; $Here = $PSScriptRoot

function Step($m) { Write-Host "==> $m" -ForegroundColor Cyan }
function Fail($m, $url) {
    Write-Host $m -ForegroundColor Yellow
    if ($url) { Start-Process $url }
    exit 1
}

$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Fail "Chưa có Python. Trang tải vừa mở — khi cài nhớ tích 'Add python.exe to PATH', xong mở lại install.bat." "https://www.python.org/downloads/"
}
$hasCli = [bool](Get-Command claude -ErrorAction SilentlyContinue)

if ($hasCli) {
    if ($Uninstall) {
        Step "Gỡ $Plugin"
        claude plugin uninstall "$Plugin@$Market"; claude plugin marketplace remove $Market
    } elseif ($Update) {
        Step "Cập nhật $Plugin"
        claude plugin marketplace update $Market
        claude plugin update "$Plugin@$Market"; if ($LASTEXITCODE -ne 0) { claude plugin install "$Plugin@$Market" }
    } else {
        if ($Source -eq "") { $Source = $Here }
        Step "Thêm nguồn plugin: $Source"
        claude plugin marketplace add $Source; if ($LASTEXITCODE -ne 0) { Step "Nguồn đã có - bỏ qua" }
        Step "Cài $Plugin"
        claude plugin install "$Plugin@$Market"
        if ($LASTEXITCODE -ne 0) { Fail "Cài plugin thất bại. Chụp màn hình này gửi team kỹ thuật." $null }
    }
} else {
    if ($Source -ne "") { Fail "Cài từ GitHub cần lệnh claude. Hãy tải zip bộ tool, giải nén rồi chạy install.bat trong đó." $null }
    Step "Cài cho Claude Desktop"
    $args2 = @("$Here\scripts\install_plugin.py"); if ($Uninstall) { $args2 += "--uninstall" }
    & python @args2
    if ($LASTEXITCODE -ne 0) { Fail "Cài thất bại. Chụp màn hình này gửi team kỹ thuật." $null }
}

Write-Host ""
Write-Host "XONG! Tắt hẳn Claude rồi mở lại. Vào tab Code và gõ:" -ForegroundColor Green
Write-Host "   /lutech-tools:make-tool   rồi kể việc bạn muốn tự động hoá"
Write-Host "   /lutech-tools:help       xem tất cả lệnh"
Write-Host "Đừng xoá hay di chuyển thư mục này - plugin chạy từ đây."
