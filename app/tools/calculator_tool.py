import re

def tool_calculator(expression: str):
    try:
        if not re.match(r'^[0-9+\-*/(). ]+$', expression.strip()):
            return "Invalid math expression."
        # eval used here — input is pre-validated by regex above
        result = eval(expression)
        return f"Answer: {result}"
    except Exception:
        return "Math error. Try something like: 25*5/2"
