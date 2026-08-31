#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    # 1. Run standard git push
    print("🚀 Pushing to GitHub (master & main)...")
    res1 = subprocess.run(["git", "push", "origin", "master"])
    if res1.returncode != 0:
        sys.exit(res1.returncode)
    
    res2 = subprocess.run(["git", "push", "origin", "master:main"])
    if res2.returncode != 0:
        sys.exit(res2.returncode)

    # 2. Purge Cloudflare Cache
    print("🧹 Purging Cloudflare cache for studiobykaz.com...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    purge_script = os.path.join(script_dir, "purge_cloudflare.py")
    subprocess.run(["python3", purge_script])

    print("✨ Deployment and cache purge complete!")

if __name__ == '__main__':
    main()
