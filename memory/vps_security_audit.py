import subprocess
import json
import os
import urllib.request

def check_vps_and_openclaw():
    report_lines = ["🛡️ *Automated VPS & OpenClaw Security Report*"]
    
    # 1. Check OpenClaw CLI security audit
    try:
        audit_res = subprocess.run(["openclaw", "security", "audit"], capture_output=True, text=True, timeout=15)
        if audit_res.returncode == 0:
            report_lines.append("✅ *OpenClaw Security Audit:* Clean")
        else:
            report_lines.append("⚠️ *OpenClaw Security Audit:* Issues detected or warning.")
            report_lines.append(f"```\n{audit_res.stdout[:300]}\n```")
    except Exception as e:
        report_lines.append(f"❌ *OpenClaw Audit Error:* {str(e)}")
        
    # 2. Check container/host OS packages (if apt is available)
    try:
        apt_res = subprocess.run(["apt", "-s", "upgrade"], capture_output=True, text=True, timeout=15)
        if apt_res.returncode == 0:
            output = apt_res.stdout
            if "0 upgraded" in output:
                report_lines.append("✅ *Host Packages:* Fully up to date.")
            else:
                report_lines.append("📦 *Host Packages:* Updates available.")
                # Extract summary line
                for line in output.splitlines():
                    if "upgraded," in line or "packages can be upgraded" in line:
                        report_lines.append(f"   _{line.strip()}_")
    except Exception as e:
        report_lines.append(f"ℹ️ *Package Check:* Not applicable or apt unavailable in container ({str(e)})")
        
    # 3. Check Gateway status
    try:
        status_res = subprocess.run(["openclaw", "status"], capture_output=True, text=True, timeout=10)
        if "gateway" in status_res.stdout.lower():
            report_lines.append("✅ *OpenClaw Gateway:* Online & Healthy")
        else:
            report_lines.append("⚠️ *OpenClaw Gateway:* Check required.")
    except Exception as e:
        report_lines.append(f"❌ *Gateway Status Error:* {str(e)}")
        
    full_message = "\n".join(report_lines)
    print(full_message)
    
    # Save report to memory for heartbeat / record
    report_path = os.path.expanduser("memory/latest-security-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(full_message)

if __name__ == "__main__":
    check_vps_and_openclaw()
