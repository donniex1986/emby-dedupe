import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

EMBY_URL = os.getenv("EMBY_URL", "").rstrip("/")
EMBY_API_KEY = os.getenv("EMBY_API_KEY", "")
EMBY_USER_ID = os.getenv("EMBY_USER_ID", "")

def emby_get(path, params=None):
    if not EMBY_URL:
        raise ValueError("EMBY_URL 未配置")
    if not EMBY_API_KEY:
        raise ValueError("EMBY_API_KEY 未配置")

    params = params or {}
    params["api_key"] = EMBY_API_KEY
    url = f"{EMBY_URL}{path}"

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def get_movies():
    params = {
        "Recursive": "true",
        "IncludeItemTypes": "Movie",
        "Fields": "Path,ProductionYear,ProviderIds"
    }

    if EMBY_USER_ID:
        data = emby_get(f"/emby/Users/{EMBY_USER_ID}/Items", params)
    else:
        data = emby_get("/emby/Items", params)

    return data.get("Items", [])

def normalize_name(name):
    return (name or "").strip().lower()

def find_duplicates(items):
    groups = {}

    for item in items:
        name = normalize_name(item.get("Name"))
        year = item.get("ProductionYear") or "unknown"
        path = item.get("Path") or ""
        provider_ids = item.get("ProviderIds") or {}

        if not name:
            continue

        key = f"{name}__{year}"

        groups.setdefault(key, []).append({
            "id": item.get("Id"),
            "name": item.get("Name"),
            "year": year,
            "path": path,
            "provider_ids": provider_ids
        })

    duplicates = [group for group in groups.values() if len(group) > 1]
    duplicates.sort(key=lambda x: ((x[0].get("name") or "").lower(), x[0].get("year")))
    return duplicates

@app.route("/")
def index():
    try:
        items = get_movies()
        duplicates = find_duplicates(items)
        return render_template(
            "index.html",
            total_movies=len(items),
            duplicate_groups=len(duplicates),
            duplicates=duplicates,
            error=None
        )
    except Exception as e:
        return render_template(
            "index.html",
            total_movies=0,
            duplicate_groups=0,
            duplicates=[],
            error=str(e)
        )

@app.route("/api/duplicates")
def api_duplicates():
    items = get_movies()
    duplicates = find_duplicates(items)
    return jsonify({
        "total_movies": len(items),
        "duplicate_groups": len(duplicates),
        "duplicates": duplicates
    })

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
