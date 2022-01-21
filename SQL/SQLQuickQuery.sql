-- DROP TABLE Accounts;

-- CREATE TABLE Accounts (ID int IDENTITY(1,1), [Rank] int, Email varchar(max),User_Name varchar(max), Password varchar(max), payment_id_info varchar(max));
-- INSERT INTO
--     [Accounts] ([Rank],[Email], [User_Name], [Password])
-- VALUES
--     (
--        5,'go2ranuga@gmail.com','Ranuga','UmFudWdh'
--     );

-- SELECT
--     *
-- FROM
--     Accounts;


-- CREATE TABLE Subjects (ID int IDENTITY(1,1), [Name] varchar(max), [Description] varchar(max), [Image] varchar(max))
-- SELECT * FROM Subjects;
-- DROP TABLE Courses;
-- CREATE TABLE Courses
-- (
--     [ID] int IDENTITY(1,1),
--     [Whole_Content] varchar(max),
--     [Info] varchar(max),
--     [Image] varchar(max),
--     [Name] varchar(max),
--     [Marks] varchar(max),
--     [Description] varchar(max),
--     [Subject] varchar(max)
-- )
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

-- SELECT * FROM Tutor;

-- DROP TABLE Courses
-- CREATE TABLE Courses
-- (
--     [ID] int IDENTITY(1,1),
--     [Whole_Content] varchar(max),
--     [Info] varchar(max),
--     [Image] varchar(max),
--     [Name] varchar(max),
--     [Marks] varchar(max),
--     [Description] varchar(max)
-- );
-- SELECT * FROM Courses;

-- SELECT * FROM Questions;

-- SELECT * FROM Resources;

CREATE TABLE Enrolled (
    [ID] int IDENTITY(1,1)
)