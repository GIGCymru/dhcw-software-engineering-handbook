# Follow out table design rules: schemes and indexes

You **SHOULD**:-

- Specify a schema when creating a table from a script.

- Ensure that each Primary Key comprises the column(s) that uniquely
    identify each row in the table.

- Include the index type (clustered or non-clustered) when defining
    the Primary Key.

- Choose the most suitable column(s) for a clustered index[^1].

- Use the Primary Key as the clustered index (it's the default and
    usually the prime candidate but not always!)

- Include the table name and the indexed fields (ordered as specified
    in the index definition) in the index name.

- Use the `INCLUDE` clause of non-clustered indexes to cover
    columns returned in select clauses or used to join other tables.
    This prevents the query optimizer having to perform key-lookup
    operations.

- Learn how the index column order in a multi-column index affects
    performance.

- Define any necessary Foreign Key constraints on your tables.

- Include the table name, referenced field(s) and referencing field(s)
    in the Foreign Key name.

- Create an index on a foreign key's child table columns.

- Review index reports[^2] with your support team. Remember that
    in high availability environments, such as an *Always On
    Availability Group*, the index usage is different on writable and
    read-only nodes.

You **SHOULD NOT**:-

- Create tables without defining a Primary Key or Clustered Index.

- Use GUIDs (e.g. `UNIQUEIDENTIFIER`) for clustered keys, especially
    where the primary key is defined as the clustered index. This can
    result in performance problems. Rather use an alternative datatype,
    for example `BIGINT`, or use the function `NEWSEQUENTIALID()` to generate
    a GUID. This reduces fragmentation.

- Use a column that is frequently updated in a clustered index.

- Create duplicate indexes. Remember, column order in the `INCLUDE`
    clause is *not* significant.

!!! tip "Practical tips"
    **WCP (Welsh Clinical Portal) -- Missing Microbiology Results**

    In 2015, a database reference table allowing duplicates contributed to the problem of missing electronic microbiology results.

!!! info "Further reading and information"
    [SQL Server Best Practices -- Implementation of Database Object Schemas \| Microsoft Learn](https://learn.microsoft.com/en-gb/previous-versions/sql/sql-server-2008/dd283095(v=sql.100))

    [Handling Constraint Violations and Errors in SQL Server - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/handling-constraint-violations-and-errors-in-sql-server/)

[^1]: Based on your queries and performance considerations

[^2]: For example [Brent Ozar Blitz Index](https://www.brentozar.com/blitzindex/) makes use of SQL
    Server's Missing Index Dynamic Management Views (DMVs)
