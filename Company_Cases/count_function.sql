USE [AdventureWorks2012]
GO

/****** Object:  UserDefinedFunction [dbo].[count]    Script Date: 10/10/2014 11:08:20 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,Dorothy H. Sanchez>
-- Create date: <Create Date, 10/10/2014,>
-- Description:	<Description,allow counting the occurrence of a character ,>
-- =============================================
CREATE FUNCTION [dbo].[count]
( @pInput VARCHAR(1000), @pSearchString VARCHAR(100) )
RETURNS INT
BEGIN

    RETURN (LEN(@pInput) - 
            LEN(REPLACE(@pInput, @pSearchString, ''))) /
            LEN(@pSearchString)

END

GO

