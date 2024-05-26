import smtplib, time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_mail(email_address, subject, file_path = False, filename = "file.csv"):
    """
    Function to send report to target mail adress.
    Uses mail template 'template.html' if available in project folder.
    email_adress: Can either be string or list of e-mail adresses the mail shall be sent to.
    subject: Mail subject
    file_path: Optional, path to e-mail attachement file.
    """

    # Constants for SMTP Server
    host = "" # add your host
    port = 25
    sender_mail = "" # add the sender adress
    user = "" # add username
    pw = # add password

    # Create a MIMEMultipart object
    msg = MIMEMultipart()

    # Set the sender and receiver email addresses
    if isinstance(email_address, str):
        receiver = email_address
    else:
        receiver = ", ".join(email_address)
    msg['From'] = sender_mail
    msg['To'] = receiver

    # Set the subject and message body
    msg['Subject'] = Header(subject, 'utf-8')

    # Attach the file to the email
    if file_path:
        with open(file_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), 'base64')
            attachment['Content-Disposition'] = 'attachment; filename=filename'
            msg.attach(attachment)

    # Send the email
    with smtplib.SMTP(host, port) as smtp:
        smtp.connect(host, port)
        smtp.ehlo()
        smtp.login(user, pw)
        print("smtp login success")
        smtp.sendmail(sender_mail, email_address, msg.as_string())
        print('sending mail succeeded')
        time.sleep(5)
        smtp.quit()
