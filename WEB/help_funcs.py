import base64
import smtplib
from email.mime.text import MIMEText
import random
import datetime
from twilio.rest import Client
import requests
from pymongo import *

cluster = MongoClient(
    "mongodb://ranuga:ranuga@ms-shard-00-00.xrgdr.mongodb.net:27017,ms-shard-00-01.xrgdr.mongodb.net:27017,ms-shard-00-02.xrgdr.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-fwaf6t-shard-0&authSource=admin&retryWrites=true&w=majority"
)


class Help_Funcs:
    def validate_email(self, email: str) -> bool:
        """
        Checking if email is valid or real
        """
        response = requests.get(
            "https://isitarealemail.com/api/email/validate", params={"email": email}
        )  # validating if a email is valid
        status = response.json()["status"]  # getting the response
        return status == "valid"

    def log_ip_address(self, url_trying_to_access: str, ip_address: str) -> None:
        respond = requests.post(
            "",
            {
                "ip_address": ip_address,
                "url_trying_to_access": url_trying_to_access,
                "time": datetime.datetime.now(),
            },
        )
        return respond.json()

    def two_fac_auth(self, user_name: str, email: str, phone_numer: str) -> list:
        time = (
            str(datetime.datetime.now().year)
            + " "
            + str(datetime.datetime.now().month)
            + " "
            + str(datetime.datetime.now().day)
            + " "
            + str(datetime.datetime.now().hour)
            + " "
            + str(datetime.datetime.now().minute)
        )
        db = cluster["2FACAUTH"]
        collection = db["2FACAUTH"]
        email_random = random.randint(0, 10000000)
        sms_random = random.randint(0, 10000000)
        collection.insert_one(
            {
                str(email): str(email_random),
                str(phone_numer): str(sms_random),
                "user_name": str(user_name),
                "time": time,
            }
        )
        self.send_sms(
            f"{sms_random} - My-School Code for 2Auth \n\n\n\n\n Only for 5 Min",
            # "+" + str(self.decode(phone_numer)),
            "+" + str(phone_numer),
        )  # TODO
        self.send_email(
            f"EmoPro 2Auth Code",
            email,
            f"{email_random} My-School Code for 2Auth \n\n\n\n\n Only for 5 Min",
        )
        return [sms_random, email_random]

    def encode(self, message: str) -> bytes:
        """
        Encode string for privacy and encryption.
        """
        msg_bytes = message.encode("latin-1")
        string_bytes = base64.b64encode(msg_bytes)
        string = string_bytes.decode("latin-1")
        return string

    def decode(self, message: str) -> bytes:
        """
        Decode string for privacy and encryption.
        """
        msg_bytes = message.encode("latin-1")
        string_bytes = base64.b64decode(msg_bytes)
        string = string_bytes.decode("latin-1")
        return string

    def send_email(self, subject: str, email_to: str, body: str) -> None:
        """
        Send Emails for 2 fac auth and other notifications
        """
        EmailAdd = "helpyoulearnstuff@gmail.com"
        Pass = "Ranuga D 2008"
        msg = MIMEText(body, "html")
        msg["Subject"] = subject
        msg["From"] = EmailAdd
        msg["To"] = email_to
        try:
            s = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
            s.login(user=EmailAdd, password=Pass)
            s.sendmail(EmailAdd, email_to, msg.as_string())
            s.quit()
        except:
            server = smtplib.SMTP_SSL("smtp.googlemail.com", 465)
            server.login(EmailAdd, Pass)
            server.sendemail(EmailAdd, email_to, msg.as_string())
        # msg = EmailMessage()
        # msg["Subject"] = subject
        # msg["From"] = EmailAdd
        # msg["To"] = email_to
        # msg.set_content(body)
        # try:
        #     with smtplib.SMTP_SSL("smtp.mail.com", 587) as smtp:
        #         smtp.login(EmailAdd, Pass)
        #         smtp.send_message(msg)
        # except:
        #     with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
        #         smtp.login(EmailAdd, Pass)
        #         smtp.send_message(msg)

    def send_sms(self, msg: str, number: int) -> str:
        account_sid = "ACb80fbc1d1d4c8e254c1c6160662fe399"
        auth_token = "f1964f9a1961ac6a9275f76e9849b5f6"
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=msg, from_="+16065352864", to=number)
        return message.sid
        # return "Testing"
