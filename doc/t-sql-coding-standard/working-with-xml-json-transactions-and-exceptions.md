# Working with XML, JSON, transactions and exceptions

## XML and JSON

You **SHOULD** use SQL Server XML and JSON functions & methods[^1] to
build and consume XML and JSON data.

You **SHOULD NOT**:-

- Build XML or JSON by concatenating strings. The loop construct
    hinders performance and can provide data in an invalid data format.

- Use XML or JSON data type methods and functions in a `WHERE`
    or `JOIN` clause, except when working with small result sets in
    a temporary table or table variable.

## Working with transactions

You **SHOULD** pair each `BEGIN` `TRANSACTION` with a `COMMIT` **or**
`ROLLBACK` `TRANSACTION` (and vice versa.) Open transactions can cause
applications to fail if left unchecked.

You **SHOULD NOT**:-

- Perform cross database transactions even where SQL Server supports
    them.

- Perform cross server queries (using linked servers or `OPENQUERY`[^2].)

- Perform cross database queries in mirrored environments. They will
    fail should database failover occur[^3].

!!! info "Further reading and information"
    [Transactions: availability groups & database mirroring - SQL Server Always On \| Microsoft Learn](https://learn.microsoft.com/en-GB/sql/database-engine/availability-groups/windows/transactions-always-on-availability-and-database-mirroring?view=sql-server-ver16)

## Handling exceptions

You **SHOULD**:-

- Manage exceptions in each stored procedure, but you **SHOULD NOT**
    mask the error from the calling application.

- Use the `TRY ... CATCH` construct to handle errors in T-SQL.

- Use a log table to record errors handled. It helps with support
    and maintenance.

- Favour `THROW` over `RAISERROR` wherever possible (i.e. in database
    compatibility SQL 2012 and later.)

- Return a result code.

[^1]: Available in SQL Server 2016 onwards

[^2]: This should be resolved in the application design.

[^3]: Although you may consider this an acceptable risk.
