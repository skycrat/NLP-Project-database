-- =======================================================
-- Create Stored Procedure Template for Azure SQL Database
-- =======================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      Katia Celestino
-- Create Date: 21-09-2022
-- Description: <Description, , >
-- =============================================
CREATE PROCEDURE dbo.usp_insert_wines_data
(
    @ID_Wine INT,
	@Winery VARCHAR(100),
	@Year_ INT,
	@Rating FLOAT,
	@Num_Reviews INT,
	@Country VARCHAR(30),
	@Region VARCHAR(100),
	@Price FLOAT,
	@Acidity INT

)
AS
BEGIN
    
    SET NOCOUNT ON
	INSERT INTO dbo.Wines
	SELECT
	@ID_Wine,
	@Winery,
	@Year_,
	@Rating,
	@Num_Reviews,
	@Country,
	@Region,
	@Price,
	@Acidity
 
END
GO
