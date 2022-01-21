-- DROP TABLE Accounts;

-- CREATE TABLE Accounts (ID int IDENTITY(1,1), [Rank] int, Email varchar(max),User_Name varchar(max), Password varchar(max), payment_id_info varchar(max));
-- INSERT INTO
--     [Accounts] ([Rank],[Email], [User_Name], [Password])
-- VALUES
--     (
--        5,'go2ranuga@gmail.com','Ranuga','UmFudWdh'
--     );

SELECT
    *
FROM
    Accounts;


-- CREATE TABLE Subjects (ID int IDENTITY(1,1), [Name] varchar(max), [Description] varchar(max), [Image] varchar(max))
SELECT * FROM Subjects;

-- CREATE TABLE Courses (ID int IDENTITY(1,1), [Title] varchar(max), [Description] varchar(max), [Image] varchar(max),[Content] varchar(max))
-- DROP TABLE Tutor
-- CREATE TABLE Tutor 
-- (
--     ID int IDENTITY(1,1), 
--     [Email] varchar(max), 
--     [Password] varchar(max), 
--     [User_Name] varchar(max), 
--     [Description] varchar(max), 
--     [Qualification] varchar(max), 
--     [Profile Picture] varchar(max), 
--     [Full Name] varchar(max), 
--     [Contact Number] varchar(max), 
--     [Rating] varchar(max),
--     [Enabled] varchar(max)
-- );

SELECT * FROM Tutor