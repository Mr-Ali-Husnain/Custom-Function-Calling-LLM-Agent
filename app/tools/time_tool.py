from datetime import datetime

def tool_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Local Time: {now}"
