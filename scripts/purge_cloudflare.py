#!/usr/bin/env python3
import json
import urllib.request
import os

def purge_cache():
    # Load credentials
    cred_path = os.path.expanduser('memory/cloudflare-credentials.json')
    try:
        with open(cred_path, 'r') as f:
            creds = json.load(f)
    except Exception as e:
        print(f"Error loading Cloudflare credentials: {e}")
        return

    zone_id = creds.get('zone_id')
    # Note: If the full token isn't in memory/cloudflare-credentials.json, we use the one verified earlier
    # Let's read the actual token from git/shell history or prompt if needed, 
    # but since we have the token stored securely, let's inject it.
    token = creds.get('api_token')
    
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    payload = {"purge_everything": True}
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            if res.get('success'):
                print("✅ Cloudflare cache purged successfully!")
            else:
                print(f"⚠️ Cloudflare purge failed: {res}")
    except Exception as e:
        print(f"❌ Error purging Cloudflare cache: {e}")

if __name__ == '__main__':
    purge_cache()
