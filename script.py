import os
import requests
from datetime import datetime

# Configuració
repo_owner = "Nayri07"
repo_name = "Random_C_Alonso_Ivan"
token = os.getenv("GITHUB_TOKEN")
tag = datetime.now().strftime("v%Y%m%d_%H%M%S")
release_name = f"Release {tag}"
executable_path = "./random"

# Headers d'autenticació
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

# 1. Crear la release
create_release_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
release_data = {
    "tag_name": tag,
    "name": release_name,
    "body": "Release automàtica generada per Jenkins",
    "draft": False,
    "prerelease": False
}

response = requests.post(create_release_url, headers=headers, json=release_data)
response.raise_for_status()
upload_url = response.json()["upload_url"].split("{")[0]

# 2. Pujar l'executable
with open(executable_path, "rb") as f:
    upload_headers = headers.copy()
    upload_headers["Content-Type"] = "application/octet-stream"
    upload_url_full = f"{upload_url}?name=random"
    upload_resp = requests.post(upload_url_full, headers=upload_headers, data=f)
    upload_resp.raise_for_status()

print(f"Release creada i executable pujat amb èxit: {release_name}")
