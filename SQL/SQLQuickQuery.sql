-- DROP TABLE Accounts;

-- CREATE TABLE Accounts (ID int IDENTITY(1,1), [Rank] int, Email varchar(max),User_Name varchar(max), Password varchar(max), payment_id_info varchar(max));
INSERT INTO
    [Accounts] ([Rank],[Email], [User_Name], [Password])
VALUES
    (
       5,'go2ranuga@gmail.com','Ranuga','UmFudWdh'
    );

SELECT
    *
FROM
    Accounts;

