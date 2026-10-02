import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

CURRYS_URL = "https://www.currys.co.uk/appliances/air-conditioners"

# -----------------------------
# EMAIL SETTINGS — EDIT THESE
# -----------------------------
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"   # Use an app password, not your real login
# -----------------------------

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)

def check_stock():
    print("Checking Currys stock…")

 response = requests.get(CURRYS_URL, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="product")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    if products:
        subject = "Air Conditioners IN STOCK at Currys!"
        body = f"Stock found at {timestamp}\n\nVisit: {CURRYS_URL}"
        send_email(subject, body)
        print("Stock found — email sent.")
    else:
        print(f"No stock at {timestamp}")

if __name__ == "__main__":
    check_stock()
