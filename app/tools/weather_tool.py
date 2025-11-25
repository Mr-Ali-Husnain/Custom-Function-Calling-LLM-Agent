import requests

def tool_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=3"
        r = requests.get(url, timeout=8)
        return r.text
    except Exception:
        return "Weather API error."
