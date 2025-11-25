import qrcode
from PIL import Image

def tool_qr(text: str, filename: str = "qr.png"):
    try:
        # QR Generate
        img = qrcode.make(text)
        img.save(filename)

        # Auto-open image using PIL
        Image.open(filename).show()

        return f"QR created successfully and saved as {filename}"
    except Exception as e:
        return f"QR generation failed: {str(e)}"
