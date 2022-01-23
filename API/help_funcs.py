import warnings
import base64
import smtplib
from email.mime.text import MIMEText
import random
import datetime
from twilio.rest import Client
import requests
from API.db.azure_sql import *
from API.db.azure_storage import *


class Help_Funcs:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        "Checking if email is valid or real"
        response = requests.get(
            "https://isitarealemail.com/api/email/validate", params={"email": email}
        )  # validating if a email is valid
        status = response.json()["status"]  # getting the response
        return status == "valid"

    @staticmethod
    def log_ip_address(url_trying_to_access: str, ip_address: str) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        respond = requests.post(
            "",
            {
                "ip_address": ip_address,
                "url_trying_to_access": url_trying_to_access,
                "time": datetime.datetime.now(),
            },
        )
        return respond.json()

    def two_fac_auth(self, user_name: str, email: str, phone_number: str) -> list:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
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
        email_random = random.randint(0, 10000000)
        sms_random = random.randint(0, 10000000)
        requests.post(
            "",
            {
                email: email_random,
                phone_number: sms_random,
                "user_name": user_name,
                "time": time,
            },
        )
        self.send_sms(
            f"{sms_random} - EmoPro Code for 2Auth \n\n\n\n\n Only for 5 Min",
            "+" + str(self.decode(phone_number)),
        )
        self.send_email(
            f"EmoPro 2Auth Code",
            self.decode(email),
            f"{email_random} EmoPro Code for 2Auth \n\n\n\n\n Only for 5 Min",
        )
        return [sms_random, email_random]

    @staticmethod
    def encode(message: str) -> bytes:
        "Encode string for privacy and encryption."
        msg_bytes = message.encode("latin-1")
        string_bytes = base64.b64encode(msg_bytes)
        string = string_bytes.decode("latin-1")
        return string

    @staticmethod
    def decode(message: str) -> bytes:
        "Decode string for privacy and encryption."
        msg_bytes = message.encode("latin-1")
        string_bytes = base64.b64decode(msg_bytes)
        string = string_bytes.decode("latin-1")
        return string

    @staticmethod
    def send_email(subject: str, email_to: str, body: str) -> None:
        "Send Emails for 2 fac auth and other notifications"
        EmailAdd = "ranugagamage@gmail.com"
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
        return None

    @staticmethod
    def send_sms(msg: str, number: int) -> str:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        account_sid = "ACbeeb34a0326adf707ec9a68902be68dc"
        auth_token = "09aee4b52484eb7218008642c35388f3"
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=msg, from_="+13132468800", to=number)
        return message.sid
        # return "Testing"

    @staticmethod
    def table_exists_or_not(table_name: str, query: str) -> bool:
        """sumary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        try:
            asql = Azure_SQL()
            tables = asql.get_tables()
            if table_name not in tables:
                asql.create_new_table(query)
            return True
        except Exception as e:
            warnings.filterwarnings(e)
            return False
