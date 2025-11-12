# Follow our table rules: columns and datatypes

You **SHOULD**:-

- Specify the nullability on columns.

- Define column data types (such as `VARCHAR` and `CHAR`)
    appropriately.

- Specify the length of a character column, even if you want it to
    be one. This rule applies when also declaring or casting variable
    datatypes.

- Use fixed-length datatypes rather than declaring variables as
    variable length of length 1 or 2.

- Include the precision and scale (when supported) when specifying
    numeric types. This prevents you being bound to the default
    values.

- Follow good database design practices. And if you consider yourself
    an 'Accidental DBA' be sure to read the 'Accidental DBA guide'!

You **SHOULD NOT**:-

- Use the `CHAR` or `NCHAR` data type for columns that permit
    `NULL` values.

- Use `VARCHAR(MAX)` when unnecessary.

- Use the `TEXT` or `NTEXT` datatypes.

- Declare variables without a datatype length. For example, `DECLARE`
    `@MyVar VARCHAR;` is to be avoided.

- Use inappropriate datatypes. For example, storing numbers or dates
    as `VARCHAR`.

!!! info "Further reading and information"
    [How to Get NULLs Horribly Wrong in SQL Server - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/how-to-get-nulls-horribly-wrong-in-sql-server/)

    [Troubleshooting SQL Server: A Guide for Accidental DBAs \| Redgate (red-gate.com)](https://www.red-gate.com/library/troubleshooting-sql-server-a-guide-for-accidental-dbas)
