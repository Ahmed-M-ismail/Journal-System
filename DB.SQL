
-- --------------------------------------------------
-- Entity Designer DDL Script for SQL Server 2005, 2008, 2012 and Azure
-- --------------------------------------------------
-- Date Created: 05/03/2016 13:08:49
-- Generated from EDMX file: G:\Project_IA (1)\Project_IA (1)\Project_IA (1)\Project_IA\Project_IA\Movies_journal.edmx
-- --------------------------------------------------

SET QUOTED_IDENTIFIER OFF;
GO
USE [Movies_journal];
GO
IF SCHEMA_ID(N'dbo') IS NULL EXECUTE(N'CREATE SCHEMA [dbo]');
GO

-- --------------------------------------------------
-- Dropping existing FOREIGN KEY constraints
-- --------------------------------------------------

IF OBJECT_ID(N'[dbo].[FK_Advertisment_Person]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Advertisments] DROP CONSTRAINT [FK_Advertisment_Person];
GO
IF OBJECT_ID(N'[dbo].[FK_Answer_Person]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Answers] DROP CONSTRAINT [FK_Answer_Person];
GO
IF OBJECT_ID(N'[dbo].[FK_Answer_Question]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Answers] DROP CONSTRAINT [FK_Answer_Question];
GO
IF OBJECT_ID(N'[dbo].[FK_Article_Category]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Articles] DROP CONSTRAINT [FK_Article_Category];
GO
IF OBJECT_ID(N'[dbo].[FK_Article_Person]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Articles] DROP CONSTRAINT [FK_Article_Person];
GO
IF OBJECT_ID(N'[dbo].[FK_Comment_Articles]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Comment] DROP CONSTRAINT [FK_Comment_Articles];
GO
IF OBJECT_ID(N'[dbo].[FK_Person_User_Type]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Persons] DROP CONSTRAINT [FK_Person_User_Type];
GO
IF OBJECT_ID(N'[dbo].[FK_Question_Person]', 'F') IS NOT NULL
    ALTER TABLE [dbo].[Questions] DROP CONSTRAINT [FK_Question_Person];
GO

-- --------------------------------------------------
-- Dropping existing tables
-- --------------------------------------------------

IF OBJECT_ID(N'[dbo].[Advertisments]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Advertisments];
GO
IF OBJECT_ID(N'[dbo].[Answers]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Answers];
GO
IF OBJECT_ID(N'[dbo].[Articles]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Articles];
GO
IF OBJECT_ID(N'[dbo].[Categories]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Categories];
GO
IF OBJECT_ID(N'[dbo].[Comment]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Comment];
GO
IF OBJECT_ID(N'[dbo].[Persons]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Persons];
GO
IF OBJECT_ID(N'[dbo].[Questions]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Questions];
GO
IF OBJECT_ID(N'[dbo].[Subscrs]', 'U') IS NOT NULL
    DROP TABLE [dbo].[Subscrs];
GO
IF OBJECT_ID(N'[dbo].[sysdiagrams]', 'U') IS NOT NULL
    DROP TABLE [dbo].[sysdiagrams];
GO
IF OBJECT_ID(N'[dbo].[User_Type]', 'U') IS NOT NULL
    DROP TABLE [dbo].[User_Type];
GO

-- --------------------------------------------------
-- Creating all tables
-- --------------------------------------------------

-- Creating table 'Advertisments'
CREATE TABLE [dbo].[Advertisments] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [adv_name] varchar(50)  NOT NULL,
    [adv_content] varchar(500)  NOT NULL,
    [user_id] int  NOT NULL,
    [active] int  NOT NULL,
    [adv_pic] varbinary(max)  NOT NULL,
    [adv_brand] varchar(50)  NOT NULL,
    [review] int  NOT NULL
);
GO

-- Creating table 'Answers'
CREATE TABLE [dbo].[Answers] (
    [id] int IDENTITY(1,1) NOT NULL,
    [question_id] int  NOT NULL,
    [user_id] int  NOT NULL,
    [answer1] varchar(500)  NOT NULL
);
GO

-- Creating table 'Articles'
CREATE TABLE [dbo].[Articles] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [art_name] varchar(50)  NOT NULL,
    [art_content] varchar(500)  NOT NULL,
    [user_id] int  NOT NULL,
    [category_id] int  NOT NULL,
    [num_views] int  NOT NULL,
    [active] int  NOT NULL,
    [review] int  NOT NULL,
    [DOA] datetime  NOT NULL,
    [art_pic] varbinary(max)  NOT NULL
);
GO

-- Creating table 'Categories'
CREATE TABLE [dbo].[Categories] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [name] varchar(50)  NOT NULL
);
GO

-- Creating table 'Comments'
CREATE TABLE [dbo].[Comments] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [user_name] varchar(50)  NOT NULL,
    [comment1] varchar(500)  NOT NULL,
    [article_id] int  NOT NULL
);
GO

-- Creating table 'Persons'
CREATE TABLE [dbo].[Persons] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [Name] varchar(50)  NOT NULL,
    [Adress] varchar(50)  NOT NULL,
    [Phone] int  NOT NULL,
    [Mail] varchar(50)  NOT NULL,
    [Password] varchar(50)  NOT NULL,
    [User_Type_ID] int  NOT NULL,
    [Profile_Pic] varbinary(max)  NULL,
    [Active] int  NOT NULL
);
GO

-- Creating table 'Questions'
CREATE TABLE [dbo].[Questions] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [user_id] int  NOT NULL,
    [question1] varchar(500)  NOT NULL,
    [answered] int  NOT NULL
);
GO

-- Creating table 'Subscrs'
CREATE TABLE [dbo].[Subscrs] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [name] nvarchar(50)  NOT NULL,
    [Mail] nvarchar(60)  NOT NULL
);
GO

-- Creating table 'sysdiagrams'
CREATE TABLE [dbo].[sysdiagrams] (
    [name] nvarchar(128)  NOT NULL,
    [principal_id] int  NOT NULL,
    [diagram_id] int IDENTITY(1,1) NOT NULL,
    [version] int  NULL,
    [definition] varbinary(max)  NULL
);
GO

-- Creating table 'User_Type'
CREATE TABLE [dbo].[User_Type] (
    [ID] int IDENTITY(1,1) NOT NULL,
    [Role] varchar(50)  NOT NULL
);
GO

-- --------------------------------------------------
-- Creating all PRIMARY KEY constraints
-- --------------------------------------------------

-- Creating primary key on [ID] in table 'Advertisments'
ALTER TABLE [dbo].[Advertisments]
ADD CONSTRAINT [PK_Advertisments]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [id] in table 'Answers'
ALTER TABLE [dbo].[Answers]
ADD CONSTRAINT [PK_Answers]
    PRIMARY KEY CLUSTERED ([id] ASC);
GO

-- Creating primary key on [ID] in table 'Articles'
ALTER TABLE [dbo].[Articles]
ADD CONSTRAINT [PK_Articles]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [ID] in table 'Categories'
ALTER TABLE [dbo].[Categories]
ADD CONSTRAINT [PK_Categories]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [ID] in table 'Comments'
ALTER TABLE [dbo].[Comments]
ADD CONSTRAINT [PK_Comments]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [ID] in table 'Persons'
ALTER TABLE [dbo].[Persons]
ADD CONSTRAINT [PK_Persons]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [ID] in table 'Questions'
ALTER TABLE [dbo].[Questions]
ADD CONSTRAINT [PK_Questions]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [ID] in table 'Subscrs'
ALTER TABLE [dbo].[Subscrs]
ADD CONSTRAINT [PK_Subscrs]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- Creating primary key on [diagram_id] in table 'sysdiagrams'
ALTER TABLE [dbo].[sysdiagrams]
ADD CONSTRAINT [PK_sysdiagrams]
    PRIMARY KEY CLUSTERED ([diagram_id] ASC);
GO

-- Creating primary key on [ID] in table 'User_Type'
ALTER TABLE [dbo].[User_Type]
ADD CONSTRAINT [PK_User_Type]
    PRIMARY KEY CLUSTERED ([ID] ASC);
GO

-- --------------------------------------------------
-- Creating all FOREIGN KEY constraints
-- --------------------------------------------------

-- Creating foreign key on [user_id] in table 'Advertisments'
ALTER TABLE [dbo].[Advertisments]
ADD CONSTRAINT [FK_Advertisment_Person]
    FOREIGN KEY ([user_id])
    REFERENCES [dbo].[Persons]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Advertisment_Person'
CREATE INDEX [IX_FK_Advertisment_Person]
ON [dbo].[Advertisments]
    ([user_id]);
GO

-- Creating foreign key on [user_id] in table 'Answers'
ALTER TABLE [dbo].[Answers]
ADD CONSTRAINT [FK_Answer_Person]
    FOREIGN KEY ([user_id])
    REFERENCES [dbo].[Persons]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Answer_Person'
CREATE INDEX [IX_FK_Answer_Person]
ON [dbo].[Answers]
    ([user_id]);
GO

-- Creating foreign key on [user_id] in table 'Answers'
ALTER TABLE [dbo].[Answers]
ADD CONSTRAINT [FK_Answer_Question]
    FOREIGN KEY ([user_id])
    REFERENCES [dbo].[Persons]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Answer_Question'
CREATE INDEX [IX_FK_Answer_Question]
ON [dbo].[Answers]
    ([user_id]);
GO

-- Creating foreign key on [category_id] in table 'Articles'
ALTER TABLE [dbo].[Articles]
ADD CONSTRAINT [FK_Article_Category]
    FOREIGN KEY ([category_id])
    REFERENCES [dbo].[Categories]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Article_Category'
CREATE INDEX [IX_FK_Article_Category]
ON [dbo].[Articles]
    ([category_id]);
GO

-- Creating foreign key on [user_id] in table 'Articles'
ALTER TABLE [dbo].[Articles]
ADD CONSTRAINT [FK_Article_Person]
    FOREIGN KEY ([user_id])
    REFERENCES [dbo].[Persons]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Article_Person'
CREATE INDEX [IX_FK_Article_Person]
ON [dbo].[Articles]
    ([user_id]);
GO

-- Creating foreign key on [article_id] in table 'Comments'
ALTER TABLE [dbo].[Comments]
ADD CONSTRAINT [FK_Comment_Articles]
    FOREIGN KEY ([article_id])
    REFERENCES [dbo].[Articles]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Comment_Articles'
CREATE INDEX [IX_FK_Comment_Articles]
ON [dbo].[Comments]
    ([article_id]);
GO

-- Creating foreign key on [User_Type_ID] in table 'Persons'
ALTER TABLE [dbo].[Persons]
ADD CONSTRAINT [FK_Person_User_Type]
    FOREIGN KEY ([User_Type_ID])
    REFERENCES [dbo].[User_Type]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Person_User_Type'
CREATE INDEX [IX_FK_Person_User_Type]
ON [dbo].[Persons]
    ([User_Type_ID]);
GO

-- Creating foreign key on [user_id] in table 'Questions'
ALTER TABLE [dbo].[Questions]
ADD CONSTRAINT [FK_Question_Person]
    FOREIGN KEY ([user_id])
    REFERENCES [dbo].[Persons]
        ([ID])
    ON DELETE NO ACTION ON UPDATE NO ACTION;
GO

-- Creating non-clustered index for FOREIGN KEY 'FK_Question_Person'
CREATE INDEX [IX_FK_Question_Person]
ON [dbo].[Questions]
    ([user_id]);
GO

-- --------------------------------------------------
-- Script has ended
-- --------------------------------------------------