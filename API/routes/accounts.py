from API import *

hp = Help_Funcs()
accounts_request_parser = reqparse.RequestParser()
accounts_request_parser.add_argument("""email""",
                                     type=str,
                                     help="""email is required""",
                                     required=True)
accounts_request_parser.add_argument("""password""",
                                     type=str,
                                     help="""Password is required""",
                                     required=True)
accounts_request_parser.add_argument("""user_name""",
                                     type=str,
                                     help="""user name is required""",
                                     required=True)
# accounts_request_parser.add_argument("""password_hash""", type=str, required=True)
accounts_request_parser.add_argument(
    """payment_id_info""",
    type=str,
    help="""payment_id_info is required""",
    required=True,
)


class Accounts(Resource):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def get(self) -> dict:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        asql = Azure_SQL()

        hp.table_exists_or_not(
            """Accounts""",
            """CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max), payment_id_info varchar(max))""",
        )
        newaccounts = []
        accounts = asql.select_table("""SELECT * FROM [Accounts]""")
        for account in accounts:
            newaccounts.append(list(account))
        return {"""message""": newaccounts}

    def post(self) -> dict:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        args = accounts_request_parser.parse_args()
        asql = Azure_SQL()
        astorage = Azure_Storage("account")
        ids_of_accounts = []
        for account in accounts:
            ids_of_accounts.append(account)
        if ids_of_accounts == []:
            ids_of_accounts = [[0]]
        id_new = ids_of_accounts[-1][0]
        id_new += 1
        info = str(args["payment_id_info"])
        info = bytes(info, encoding="utf-8")
        astorage.create_file(file_name_in_the_cloud=f"{id_new}-info.txt",
                             file_rb=info)
        hp.table_exists_or_not(
            """Accounts""",
            """CREATE TABLE Accounts (ID int IDENTITY(1,1), Rank INT(max), Email varchar(max),User_Name varchar(max), Password varchar(max), payment_id_info varchar(max))""",
        )
        asql.insert_to_table(
            f"""INSERT INTO [Accounts]( [Rank],[Email], [User_Name], [Password], [payment_id_info] ) VALUES ( 1,'{args['email']}', '{args['user_name']}', '{args['password']}','{id_new}-info.txt')"""
        )
        newaccounts = []
        accounts = asql.select_table("""SELECT * FROM [Accounts]""")
        for account in accounts:
            newaccounts.append(list(account))
        accounts = asql.select_table("SELECT * FROM Accounts")
        return {"""message""": newaccounts}


api.add_resource(Accounts, """/api/Accounts""")
