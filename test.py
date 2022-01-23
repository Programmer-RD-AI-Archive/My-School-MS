import random

import requests
from tqdm import tqdm

from API.db.azure_sql import *
from API.db.azure_storage import *

# asql = Azure_SQL()
# print(asql.create_new_table())
# print(asql.insert_to_table())
# print(asql.select_table())
# print(asql.get_tables())
# print(asql.close_connection())
astorage = Azure_Storage("account")
# info = str("gergergre")
# info = bytes(info, encoding="utf-8")  # open("./requirements.txt", "rb")
print(astorage.create_file("info", "requirements.txt"))
# print(astorage.download_file("requirements.txt"))
# print(
#     requests.get(
#         "http://127.0.0.1:5000/api/azure/storage",
#         {
#             "Container Name": "account",
#             "blob_name": "test.txt",
#             "file_rb": "grwegreg",
#             "Type": "Create File",
#         },
#     ).json()
# )


class Create_Multiple:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    @staticmethod
    def accounts(
        email=random.choice(
            requests.get(
                "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10"
            ).json()),
        password=random.choice(
            requests.get(
                f"https://random-word-api.herokuapp.com/word?number={random.randint(23,56)}&swear=0"
            ).json()),
        user_name=random.choice(
            requests.get(
                f"https://random-word-api.herokuapp.com/word?number={random.randint(59,85)}&swear=0"
            ).json()),
    ):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        iter.set_description("Getting")
        iter.set_description("Getting Payment Id Info")
        payment_id_info = {"info": "test.py"}
        iter.set_description("Init Azure SQL")
        asql = Azure_SQL()
        iter.set_description("Init Azure Storage")
        astorage = Azure_Storage("account")
        iter.set_description("Select *")
        accounts = asql.select_table("""SELECT * FROM [Accounts]""")
        iter.set_description("Iter")
        ids_of_accounts = []
        for account in accounts:
            ids_of_accounts.append(account)
        if ids_of_accounts == []:
            ids_of_accounts = [[0]]
        id_new = ids_of_accounts[-1][0]
        id_new += 1
        info = str(payment_id_info)
        info = bytes(info, encoding="utf-8")
        astorage.create_file(
            file_name_in_the_cloud=f"{id_new}-payment-details.json",
            file_rb=info)
        asql.insert_to_table(
            f"""INSERT INTO [Accounts]( [Rank],[Email], [User_Name], [Password], [payment_id_info] ) VALUES ( 1,'{email}', '{user_name}', '{password}','{id_new}-info.txt')"""
        )
        newaccounts = []
        accounts = asql.select_table("""SELECT * FROM [Accounts]""")
        for account in accounts:
            newaccounts.append(list(account))


print("SELECT admin FROM users WHERE username = %s'", ("username", ))
