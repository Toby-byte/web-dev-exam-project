import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_email(receiver_email, verification_code):
    sender_email = "skroyer09@gmail.com"  # Replace with your Gmail address
    password = "vkxq xwhj yaxn rqjs"         # Replace with the app password you generated
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Verify your email"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    text = f"""\
    Hi,
    Please verify your email by using the following code: {verification_code}
    """
    html = f"""\
    <html>
      <body>
        <p>Hi,<br>
           Please verify your email by clicking the link below:<br>
           <a href="http://0.0.0.0/verify?code={verification_code}">Verify Email</a>
        </p>
      </body>
    </html>
    """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    message.attach(part1)
    message.attach(part2)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
