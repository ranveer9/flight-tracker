import smtplib
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "XXXXXXXXXXXX"
TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXX"
TWILIO_MOBILE_NUMBER = "XXXXXXXXXXXXXXXXX"

MY_EMAIL = "XXXXXXXXXXXXXXXXXXXXX"
MY_EMAIL_PASSWORD = "XXXXXXXXXXXXXXXXX"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # def send_sms(self, message_body):
    #     message = self.client.messages.create(
    #         from_=TWILIO_MOBILE_NUMBER,
    #         body=message_body,
    #         to="XXXXXXXXXXXXXXXXX"
    #     )
    #     print(message.sid)

    # whatsapp sandbox
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f"whatsapp: {TWILIO_MOBILE_NUMBER}",
            body=message_body,
            to=f"whatsapp:{"XXXXXXXXXXXXXXX"}"
        )
        print(message.sid)


    # def send_email(self, email_list, email_body):
    #     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
    #         for email in email_list:
    #             connection.sendmail(from_addr=MY_EMAIL,
    #                                 to_addrs=email,
    #                                 msg=f"Subject:Flight offers at lowest price!\n\n{email_body}".encode("utf-8"))