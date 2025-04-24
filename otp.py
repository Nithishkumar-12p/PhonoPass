import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def otp(to_email):
    generated_otp = random.randint(1000, 9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "nithishkumarbollapelli@gmail.com"  # Your Gmail
    password = "isyyvhfcovnddjzs"      # App password with NO SPACES

    from_email = username
    subject = "Your OTP for Verification"
    body = f"Your OTP is: {generated_otp}"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        print("OTP sent successfully to", to_email)

        # Prompt for user input
        votp = int(input("Enter the OTP received: "))
        if votp == generated_otp:
            print("✅ Verification Successful!")
        else:
            print("❌ Verification Failed.")
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check your Gmail ID or App Password.")
    except Exception as e:
        print("❌ Error occurred:", str(e))
