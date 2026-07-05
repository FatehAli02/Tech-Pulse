import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

def send_digest_email(html_content):

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    if not sender_email or not sender_password:
        logger.error("Email credentials missing! Check your .env file.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Tech Pulse: Your Curated Daily Digest"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    part = MIMEText(html_content, "html")
    msg.attach(part)

    try:
        logger.info("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() 
        
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        
        logger.success("Email digest sent successfully!")
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False