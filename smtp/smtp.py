import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "dogancankoseoglu@gmail.com"
receiver_email = "ertusmertus@gmail.com"
password = "vyraftpnrgggchiq"

# Create the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email with TLS"

# Email body
body = "This is a test email sent using Python with TLS."
msg.attach(MIMEText(body, 'plain'))


def send_mail():
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        print("Connected to smtp server")

        server.login(sender_email, password)
        print("Login to smtp server")

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email has been sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Fail to send mail: {e}")
    finally:
        server.quit()
