# Email configs --------------------------------------
# Usar local-settings para actualizar estos valores
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lalal@gmail.com'
EMAIL_HOST_PASSWORD = '111222233344'
# ------------------------------------------------------

# **************************************************************
# Python email
# **************************************************************
import smtplib

sender = EMAIL_HOST_USER
receiver = "elconta@eugeniovazquez.com.ar"
password = EMAIL_HOST_PASSWORD
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
