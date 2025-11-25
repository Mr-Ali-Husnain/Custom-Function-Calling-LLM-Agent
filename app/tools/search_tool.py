import requests

def tool_search(query: str):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1"
        r = requests.get(url, timeout=8)
        data = r.json()
        if data.get("AbstractText"):
            return data["AbstractText"]
        related = data.get("RelatedTopics", [])
        for item in related:
            # item might be dict or list
            if isinstance(item, dict) and "Text" in item:
                return item["Text"]
        return "No search results found."
    except Exception:
        return "Search API error."
