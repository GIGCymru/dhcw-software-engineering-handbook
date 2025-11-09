# Stored procedures

You **SHOULD: -**

- Use meaningful names to indicate the purpose of procedures &
    parameters. Be verbose if needed.

- Match parameter datatypes to the underlying data to avoid implicit
    conversion.

- Include a comment header to indicate the procedure's purpose and
    use. Include an example call if possible.

- Enclose procedures with `BEGIN END` blocks after the `AS`
    keyword.

- Add the `SET NOCOUNT ON` statement before any Data Manipulation
    Language statements unless you have good reason for not doing so.

- Use `SET XACT_ABORT ON`. It terminates and rollbacks the entire
    transaction when a T-SQL statement raises a run-time error.

- Declare variables, table variables and temp tables at the start of
    a procedure[^1].

- Use `BEGIN` and `END` after `IF`, even if only one statement
    is covered. This makes the code clearer and avoids errors if further
    statements are added to the `IF` block later.

- Use table variables for transitory tables with *less* than 1000
    rows.

- Use temporary tables for transitory tables with *more* than 1000
    rows.

- Use explicit transactions when updating data.

- Use SavePoints within a transaction. The use of SavePoint can
    allow you to rollback a series of statements within a transaction.

- Pass parameters explicitly to Stored Procedures and `EXECUTE`
    statements wherever possible.

You **SHOULD NOT**:-

- Set the `ANSI_NULLS` option. It should normally be set to `ON` and
    is deprecated by Microsoft and not supported for certain indexes.

- Set the `QUOTED_IDENTIFIER` option. It has no effect and should
    normally be set to `ON`.

- Declare **variables** you never use.

- Use `CURSOR` *s* and `WHILE` clauses.

- Use Table Variables, Temporary Tables, Common Table Expressions and
    Subqueries without understanding their impact on performance.

- Use nested transactions. A `ROLLBACK` of a nested transaction
    can affect more than just the statements executed.

- Return multiple result sets.

- Supply stored procedures with a wide range of data parameters. SQL
    Server compiles these to a single query plan.

!!! info "Further reading and information"
    [Discontinued database engine functionality - SQL Server \| Microsoft Learn](https://learn.microsoft.com/en-gb/sql/database-engine/discontinued-database-engine-functionality-in-sql-server?view=sql-server-ver16)

    [Temporary Tables in SQL Server - Simple Talk (red-gate.com )](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/temporary-tables-in-sql-server/)

[^1]: **Note**: This is contrary to the general coding standards. But
    Redgate discourages interweaving Data Definition Language (e.g.
    `CREATE TABLE`) and Data Manipulation Language statements (e.g.
    `SELECT`).
