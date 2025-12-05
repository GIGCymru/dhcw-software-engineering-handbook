# Examples

## Insert statement

In this example we make sure to

- Qualify table names with the schema name.

- Specify `INSERT` columns.

!!! warning "Practices to avoid"
    ```sql
        INSERT INTO SubscribingConsultant
        VALUES ('7A5', 'C1234567');
    ```

!!! example "Examples of good practice"
    ```sql
        [INSERT INTO dbo.SubscribingConsultant(Organisation, ConsultantId)]
        [VALUES('7A5', 'C1234567\');]
    ```

## Select statement

In this example we make sure to

- Qualify table names with the schema name.

- Add a meaningful table alias name.

- Use the field name in the `ORDER BY` clause rather than a constant.

!!! warning "Practices to avoid"
    ```sql
        SELECT Report.Id, Report.SubjectGivenName AS FirstName, Report.SubjectFamilyName AS LastName
        FROM Report
        ORDER BY 1 ASC;
    ```

!!! example "Examples of good practice"
    ```sql
        SELECT Report.Id, Report.SubjectGivenName AS FirstName, Report.SubjectFamilyName AS LastName
        FROM dbo.Report AS Report
        ORDER BY Report.Id ASC;
    ```

## Queries

In this next example, we will step through a query making sure to: -

1. Expand wildcards searches.

2. Qualify table names with the schema name.

3. Add a meaningful table alias name.

4. Qualify column names with table alias.

5. Add a meaningful column alias name[^1].

6. Alias the column name using the AS convention.

7. Add the semi colon terminator.

!!! warning "Practices to avoid"
    ```sql
        SELECT * FROM Report

        SELECT Report.Id, SubjectGivenName f, Report.SubjectFamilyName
        FROM Report

        SELECT Report.Id, SubjectGivenName f, Report.SubjectFamilyName
        FROM dbo.Report

        SELECT Report.Id, SubjectGivenName f, Report.SubjectFamilyName
        FROM dbo.Report AS Report

        SELECT Report.Id, Report.SubjectGivenName f, Report.SubjectFamilyName
        FROM dbo.Report AS Report
        
        SELECT Report.Id, Report.SubjectGivenName FirstName, Report.SubjectFamilyName
        FROM dbo.Report AS Report

        SELECT Report.Id, Report.SubjectGivenName AS FirstName, Report.SubjectFamilyName
        FROM dbo.Report AS Report
    ```

!!! example "Examples of good practice"
    ```sql
        SELECT Report.Id, Report.SubjectGivenName AS FirstName, Report.SubjectFamilyName
        FROM dbo.Report AS Report;
    ```

## Dates #1

In this example, we ensure that a query against a date field can use the
index.

!!! warning "Practices to avoid"
    ```sql
        SELECT ObservationRequest.ReportId FROM dbo.ObservationRequest ObservationRequest
        WHERE CONVERT(VARCHAR(10), ObservationRequest.AuthorisedDateTime, 112) = '2018-12-12';
    ```

!!! example "Examples of good practice"
    ```sql
        SELECT ObservationRequest.ReportId
        FROM dbo.ObservationRequest ObservationRequest
        WHERE CAST(ObservationRequest.AuthorisedDateTime AS DATE) = '2018-12-12';
    ```

## Dates #2

We step through the next example ensuring to

1. Eliminate the `DATEDIFF` operator.

2. Eliminate arithmetic operators against date fields.

!!! warning "Practices to avoid"
    ```sql
        SELECT ObservationRequest.ReportId
        FROM dbo.ObservationRequest ObservationRequest
        WHERE > DATEDIFF(DAY,ObservationRequest.AuthorisedDateTime,GETDATE())<=30;

        SELECT ObservationRequest.ReportId
        FROM dbo.ObservationRequest > ObservationRequest
        WHERE CAST(ObservationRequest.AuthorisedDateTime AS DATE) > GETDATE()-30;
    ```

!!! example "Examples of good practice"
    ```sql
        SELECT COUNT(DISTINCT ObservationRequest.ReportId)
        FROM dbo.ObservationRequest ObservationRequest
        WHERE CAST(ObservationRequest.AuthorisedDateTime AS DATE) >= DATEADD(DAY,-30,CAST(GETDATE() AS > DATE));
    ```

## Stored procedures #1

In this next example, we will step through a stored procedure making
sure to:

1. Qualify the procedure name with the schema.

2. Add `BEGIN` and `END` statements.

3. `SET NOCOUNT ON`

4. Return a value.

!!! warning "Practices to avoid"
    ```sql
        CREATE PROCEDURE prGetReportMasterId @Id BIGINT
        AS
            SELECT
                Report.Id
            , Report.MasterReportId
            FROM
                dbo.Report AS Report
                WHERE Report.Id = @Id;

        CREATE PROCEDURE dbo.prGetReportMasterId @Id BIGINT
        AS
            SELECT
                Report.Id
            , Report.MasterReportId
            FROM
                dbo.Report AS Report
                WHERE Report.Id = @Id;

        CREATE PROCEDURE dbo.prGetReportMasterId @Id BIGINT
        AS
        BEGIN
            SELECT
                Report.Id
            , Report.MasterReportId
            FROM
                dbo.Report AS Report
                WHERE Report.Id = @Id;
        END;

        CREATE PROCEDURE dbo.prGetReportMasterId @Id BIGINT
        AS
        BEGIN
            SET NOCOUNT ON;
            SELECT
                Report.Id
            , Report.MasterReportId
            FROM
                dbo.Report AS Report
                WHERE Report.Id = @Id;
        END;
    ```

!!! example "Examples of good practice"
    ```sql
        CREATE PROCEDURE dbo.prGetReportMasterId @Id BIGINT
        AS
        BEGIN
            SET NOCOUNT ON;
            SELECT
                Report.Id
            , Report.MasterReportId
            FROM
                dbo.Report AS Report
                WHERE Report.Id = @Id;
            RETURN 0;
        END;
    ```

## Stored procedures #2

In the following example, we will step through a stored procedure making
sure to:

1. Specify length for `VARCHAR` parameters.

2. Specify columns for `INSERT` statements.

3. `SET NOCOUNT ON`, `SET XACT_ABORT ON`

4. Add implicit transaction using `BEGIN TRANSACTION` and `COMMIT`

5. Add Error Handling using `TRY ... CATCH` blocks.

!!! warning "Practices to avoid"
    ```sql
        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR
            , @Rubric                VARCHAR
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            INSERT dbo.ReferenceDataValue
            VALUES
                (
                    @ReferenceDataDomainId
                    , @Code
                    , @Rubric
                    , GETDATE()
                    , @Active
                    , @ParentId
                );
        RETURN 0;
        END;

        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR(50)
            , @Rubric                VARCHAR(200)
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            INSERT dbo.ReferenceDataValue
            VALUES
                (
                    @ReferenceDataDomainId
                    , @Code
                    , @Rubric
                    , GETDATE()
                    , @Active
                    , @ParentId
                );
        RETURN 0;
        END;

        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR(50)
            , @Rubric                VARCHAR(200)
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            INSERT dbo.ReferenceDataValue
                (
                    Id
                , ReferenceDataDomainId
                , Code
                , Rubric
                , DateTimeCreated
                , Active
                , ParentId
                )
            VALUES
                (
                    @ReferenceDataDomainId
                    , @Code
                    , @Rubric
                    , GETDATE()
                    , @Active
                    , @ParentId
                );
        RETURN 0;
        END;

        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR(50)
            , @Rubric                VARCHAR(200)
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            SET NOCOUNT ON;
            SET XACT_ABORT ON;
            INSERT dbo.ReferenceDataValue
                (
                    Id
                , ReferenceDataDomainId
                , Code
                , Rubric
                , DateTimeCreated
                , Active
                , ParentId
                )
            VALUES
                (
                    @ReferenceDataDomainId
                    , @Code
                    , @Rubric
                    , GETDATE()
                    , @Active
                    , @ParentId
                );
        RETURN 0;
        END;
        
        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR(50)
            , @Rubric                VARCHAR(200)
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            SET NOCOUNT ON;
            SET XACT_ABORT ON;
            BEGIN TRANSACTION
            INSERT dbo.ReferenceDataValue
                (
                    Id
                , ReferenceDataDomainId
                , Code
                , Rubric
                , DateTimeCreated
                , Active
                , ParentId
                )
            VALUES
                (
                    @ReferenceDataDomainId
                    , @Code
                    , @Rubric
                    , GETDATE()
                    , @Active
                    , @ParentId
                );
            COMMIT
        RETURN 0;
        END;    
    ```

!!! example "Examples of good practice"
    ```sql
        CREATE PROCEDURE dbo.InsertReferenceDataValue
              @ReferenceDataDomainId INT
            , @Code                  VARCHAR(50)
            , @Rubric                VARCHAR(200)
            , @Active                BIT
            , @ParentId              INT = NULL
        AS
        BEGIN
            SET NOCOUNT ON;
            SET XACT_ABORT ON;
            BEGIN TRY
                BEGIN TRANSACTION
                INSERT dbo.ReferenceDataValue
                    (
                        Id
                    , ReferenceDataDomainId
                    , Code
                    , Rubric
                    , DateTimeCreated
                    , Active
                    , ParentId
                    )
                VALUES
                    (
                        @ReferenceDataDomainId
                        , @Code
                        , @Rubric
                        , GETDATE()
                        , @Active
                        , @ParentId
                    );
                COMMIT
            END TRY
            BEGIN CATCH
                DECLARE @ErrorMsg VARCHAR(4000);
                SET @ErrorMsg = ERROR_MESSAGE();
                -- Rollback our transaction
                IF @@TRANCOUNT>0
                    ROLLBACK;
                --Re-raise the error to our application;
                RAISERROR(@ErrorMsg, 16, 1);
            END CATCH;
        RETURN 0;
        END;
    ```

## Naming

In our last example, we contrast a simple database query that does not
conform to our rules with one that does. The conformant query assumes
there is a constraint preventing any changes to the underlying database
schema.

The conformant query implements the following rules: -

- Names are descriptive and singular.

- Pascal Casing applied.

- Prefixes and underscores removed.

- All Keywords are uppercase.

- Meaningful table alias name applied.

- Columns qualified with Table alias and meaningful column alias
    applied.

- Meaningful column alias and name applied.

- SQL Prompt formatting style rule applied.

!!! warning "Practices to avoid"
    ```sql
        SELECT SubjectGivenName, SubjectFamilyName, [Hospital Ward]
        FROM tblPatients WHERE ID = @int_ID
        AND SubjectGivenName =  @str_param2;
    ```

!!! example "Examples of good practice"
    ```sql
        SELECT
            Patient.SubjectGivenName AS FirstName
            , Patient.SubjectFamilyName AS LastName
            , Patient.[Hospital Ward] AS HospitalWard
        FROM
            dbo.tblPatients AS Patient
        WHERE
            Patient.ID = @PatientId
            AND Patient.SubjectGivenName = @FirstName;
    ```

[^1]: <https://documentation.red-gate.com/codeanalysis/code-analysis-for-sql-server/style-rules/st010>
