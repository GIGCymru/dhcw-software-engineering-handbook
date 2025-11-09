# Follow our naming rules (see also table design rules)

You **SHOULD**:-

- Use descriptive names, favouring readability over brevity.

- Favour singular nouns over plurals for table names views and
    scalars (columns, parameters and variables.) The use of a
    collective name is best.

- Use a mix of verbs and nouns in the present tense for functions
    and stored procedure names[^1].

- Use uppercase for all *Keywords, Built-in functions, built-in
    datatypes* and *Global Variables*[^2].

- Use Pascal Casing (with the first letter and each subsequent
    concatenated word capitalized) consistently for all other
    names[^3].

- Use capitalization where common abbreviations[^4] are used.

- Use prefixes and underscores for the following common naming
    conventions (next page).

You **SHOULD NOT**:-

- Rely on system generated named objects such as constraints or
    indexes.

- Use abbreviations, spaces, or non-standard characters and reserved
    words. Doing so avoids the need to use square brackets.

- Prefix stored procedures with sp\_ Doing so impedes
    performance because SQL Server searches the master database first.

- Use prefixes (Hungarian notation), suffixes and underscores except
    where specific naming conventions exist (see the next page.)

| **Prefix** | **Usage** | **Example** | **Notes** |
| --- | --- | --- | --- |
| **pr**| Stored Procedure | pr GetReportIDAndIdentifiers | Optional, but use must be consistent within a database |
| **fn**| F unction | fnSaveNewPassword |  |
| **tr**| Trigger | trAuditChangeToNHSNumber |  |
| **CIX**| Clustered Index | CIX_Report_Id | Table name and indexes are also separated by an underscore. |
| **PK**| Primary Key | PK_Report | Table name |
| **IX**| Index | IX_Report_SubjectDoBFamilyNameGivenNameId_includes | Table name and indexes are also separated by an underscore. Use "includes" showing the index has included columns[^5]. |
| **FK**| Foreign Key | FK_ReferenceDataValue_ID_PlacerID | Table name, referenced field(s) and referencing field(s) also separated by an underscore |
| **DF**| Default constraint |  |  |
| **CK**| Check constraint |  |  |
| **UQ**| Unique constraint |  |  |

!!! info "Further reading and information"
    [Publicly Available Standards (iso.org)](https://standards.iso.org/ittf/PubliclyAvailableStandards/c060341_ISO_IEC_11179-5_2015.zip)

    [Reserved Keywords (Transact-SQL) - SQL Server \| Microsoft Learn](https://learn.microsoft.com/en-gb/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver16)

    [The 9 Most Common Database Design Errors \| Vertabelo Database Modeler](https://vertabelo.com/blog/the-9-most-common-database-design-errors/) (No. #4)

    [Ten Common Database Design Mistakes - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/database-administration-sql-server/ten-common-database-design-mistakes/)

[^1]: But beware of situations where this is counterproductive. For
    example, having many procedures prefixed with 'Get' makes any
    specific stored procedure difficult to spot. See the section
    '[Exceptions prove the rule'](exceptions-prove-the-rule.md).

[^2]: This rule raised the concern that we could end up with differing
    coding standards based on language and technology and we will.
    However, SQL is a set-based language -- it's acceptable that
    different rules apply.

[^3]: Be aware that Redgate SQL prompts adds aliases in lower case
    based on the leading letters in a camel case table name.

[^4]: Use abbreviations only when there can be no doubt as to their meaning.

[^5]: Included columns prevent a key-lookup in the query plan and so aid performance.
