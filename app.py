from flask import Flask, request
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def telegram_gonder(mesaj):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": mesaj
            },
            timeout=10
        )

        if response.ok:
            print("Telegram mesajı gönderildi.")
        else:
            print("Telegram hatası:", response.text)

    except Exception as hata:
        print("Bağlantı hatası:", hata)


@app.route("/")
def ana_sayfa():

    ip = request.remote_addr

    tarih = datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )

    mesaj = f"""🌐 YENİ ZİYARET

📍 IP:
{ip}

🕐 Tarih:
{tarih}
"""

    telegram_gonder(mesaj)

    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>Sitem</title>

        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #111827;
                color: white;
                font-family: Arial, sans-serif;
            }

            .box {
                text-align: center;
                padding: 40px;
                background: #1f2937;
                border-radius: 20px;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>Hoş Geldiniz</h1>
            <p>Siteye giriş yaptınız.</p>
        </div>

    </body>
    </html>
    """


if __name__ == "__main__":

    telegram_gonder(
        f"""🟢 SİSTEM AKTİF

📡 Flask sunucusu başlatıldı.

🕐 {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}"""
    )

    print("🚀 Flask sunucusu başlatılıyor...")
    print("📡 Telegram bildirim sistemi aktif")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
