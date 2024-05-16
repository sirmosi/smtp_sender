import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import getpass

def send_email(sender_email, recipient_email, smtp_server, smtp_port, sender_password, repeat_count, subject="Hello", content="Welcome to our mail provider company!"):
    try:
        # Create a MIMEText object with the content
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add the content to the email
        message.attach(MIMEText(content, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security
        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        for _ in range(repeat_count):
            server.sendmail(sender_email, recipient_email, message.as_string())
            logging.info(f"Email sent successfully from {sender_email} to {recipient_email}")

        # Quit the server
        server.quit()
    except Exception as e:
        logging.error(f"Error occurred: {e}")

# Configure logging
log_filename = f"mail_sender_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Accept input from stdin
sender_email = input("Enter sender email address: ")
sender_password = getpass.getpass(prompt="Enter sender password: ")
recipient_email = input("Enter recipient email address: ")
smtp_server = input("Enter SMTP server address: ")
smtp_port = int(input("Enter SMTP port number: "))
repeat_count = int(input("Enter number of times to repeat sending the email: "))
subject = input("Enter email subject (press Enter for default 'Hello'): ") or "Hello"
content = input("Enter email content (press Enter for default message): ") or "Welcome to Touca mail Service!"

send_email(sender_email, recipient_email, smtp_server, smtp_port, sender_password, repeat_count, subject, content)