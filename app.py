from flask import Flask
import os  # برای دریافت پورت از محیط اجرا

app = Flask(__name__)

@app.route('/')
def home():
    return "سلام مازوت! رباتت روی Render زنده شد!"

if __name__ == '__main__':
    # دریافت پورت از محیط اجرا؛ اگر نبود، پیش‌فرض 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
