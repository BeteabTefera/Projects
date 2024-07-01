import smtplib

SENDER_EMAIL = 'graynoodles@outlook.com'
SENDERPASSWORD = 'ZABlon9900!@#$'

def send_email(reciever_email, subject, body):
    message = f'Subject:{subject}\n\n{body}'
    with smtplib.SMTP('smtp-mail.outlook.com',587) as server:
        server.starttls()
        server.login(SENDER_EMAIL,SENDERPASSWORD)
        server.sendmail(SENDER_EMAIL,reciever_email,message)

send_email('bebidems08@gmail.com','Hello',
           'JOB HAS FINISHED')