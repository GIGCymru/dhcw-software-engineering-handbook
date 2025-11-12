# Apply code analysis rules

You **SHOULD**: -

- Specify column names when using `INSERT`, even when inserting data
    into all columns.

- Expand the asterisk wildcard to explicitly define all columns.

- Qualify object names. Prefix each reference to a table with its
    schema (but not the database name) and each column to its parent
    table (or alias) in `SELECT` statements.

- Terminate all statements with a semi-colon and with no leading
    whitespace.

- Favour `EXISTS` or table joins over `IN` or `COUNT` where it's sensible to
    do so.

- Include an `ELSE` block with each `CASE` expression.

- Prefer the use of `SCOPE_IDENTITY()` to `@@IDENTITY`.

- Use Common Table Expressions (CTEs) instead of non-correlated
    subqueries. A `CTE` is easier to read than a subquery and offers the
    same performance.

- Use functions like `ISNULL`, `IS NULL`, `ISNUMERIC`, `TRY_CONVERT`, `COALESCE` and** `CAST` correctly.

You **SHOULD NOT**:-

- Use `INSERT INTO` *<table\>* with an `ORDER BY` clause. The order
    depends on the clustered index if one is defined.

- Use `DELETE` without a `WHERE` or `INNER JOIN` clause

- Use `UPDATE` without a `WHERE` or `INNER JOIN` clause

- Use correlated sub-queries. (The exception to this is the use of
    `EXISTS`.)

- Define `JOIN` conditions in the `WHERE` clause. Include the
    `JOIN` condition in the `ON` clause.

- Include `WHERE` clauses in `SELECT` statements[^1] to
    prevent defining Cartesian joins.

- Use `ISNULL` in a `WHERE` or `JOIN` clause. Expressions need
    to use `IS NOT NULL` and the `COALESCE` function to handle
    `NULL` values appropriately.

- Use comparison operators against a `NULL` value.

- Use `DISTINCT` where it is not required. Use a `GROUP BY` clause
    where possible and check `JOIN` conditions to eliminate duplicate
    rows.

- Use wildcards (such as %) at the start of `LIKE` in `WHERE` clauses.
    Indexes *cannot* support wildcard queries at the start of a `LIKE`
    expression.

- Reference columns that do not have indexes in a `WHERE`, `JOIN`
    or `ORDER BY` clause.

- Use system or user-defined scalar functions in a `WHERE` or
    `JOIN` clause. Functions are evaluated for each row in the result
    set. Any indexes cannot be used on the column the function is being
    performed on.

- Use the `NOLOCK` hint. It's safer to specify the correct isolation
    level instead.

!!! tip "Practical tips"
    Use Redgate SQL Prompt to help you implement code analysis rules. See [Follow our code layout rules](follow-our-code-layout-rules.md)

!!! info "Further reading and information"
    [Code Analysis - Product Documentation (re d-gate.com)](https://documentation.red-gate.com/codeanalysis)

    [How to Get NULLs Horribly Wrong in SQL Server - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/how-to-get-nulls-horribly-wrong-in-sql-server/)

    [SQL Server Common Table Expression (CTE) Basics - Simple Talk (red -gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/sql-server-cte-basics/)

    [Lookup Table Madness -- SQLServerCentral](https://www.sqlservercentral.com/articles/lookup-table-madness)

[^1]: If you need to perform a Cartesian join, use the newer syntax
    `CROSS APPLY` -- most likely when shredding XML/JSON data.
