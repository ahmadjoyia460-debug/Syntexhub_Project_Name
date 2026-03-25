import smtplib
import csv
import json
import time
import logging
from email.message import EmailMessage

logging.basicConfig(filename='email_log.txt', level=logging.INFO)

EMAIL_ADDRESS = "ahmadjoyia460@gmail.com"
APP_PASSWORD = "ahmad"  

def send_email(to_email, name):
    msg = EmailMessage()
    msg['Subject'] = "Hello from Python Bot"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    msg.set_content(f"Hello {name},\n\nThis is a test email sent using Python.\n\nRegards,\nAhmad")

    try:
        with open("sample.pdf", "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename="sample.pdf")
    except FileNotFoundError:
        print("No attachment found, skipping...")

    for attempt in range(3):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
                smtp.send_message(msg)

            print(f"Email sent to {to_email}")
            logging.info(f"SUCCESS: {to_email}")
            return

        except Exception as e:
            print(f"Error sending to {to_email}, retrying...")
            logging.error(f"FAILED: {to_email} | Error: {e}")
            time.sleep(2)

# ---------- CSV ----------
def send_from_csv():
    try:
        with open("recipients.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                send_email(row['email'], row['name'])
    except FileNotFoundError:
        print("CSV file not found!")

# ---------- JSON ----------
def send_from_json():
    try:
        with open("recipients.json") as file:
            data = json.load(file)
            for user in data:
                send_email(user['drsaif@443gmail.com'], user['saif'])
    except FileNotFoundError:
        print("JSON file not found!")

# ---------- MAIN ----------
print("1. Send from CSV")
print("2. Send from JSON")

choice = input("Enter choice: ")

if choice == "1":
    send_from_csv()

elif choice == "2":
    send_from_json()

else:
    print("Invalid choice")