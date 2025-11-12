# Working with transactions

You **SHOULD** pair each `BEGIN` `TRANSACTION` with a `COMMIT` **or**
`ROLLBACK` `TRANSACTION` (and vice versa.) Open transactions can cause
applications to fail if left unchecked.

You **SHOULD NOT**:-

- Perform cross database transactions even where SQL Server supports
    them.

- Perform cross server queries (using linked servers or `OPENQUERY`[^1].)

- Perform cross database queries in mirrored environments. They will
    fail should database failover occur[^2].

!!! info "Further reading and information"
    [Transactions: availability groups & database mirroring - SQL Server Always On \| Microsoft Learn](https://learn.microsoft.com/en-GB/sql/database-engine/availability-groups/windows/transactions-always-on-availability-and-database-mirroring?view=sql-server-ver16)

[^1]: This should be resolved in the application design.

[^2]: Although you may consider this an acceptable risk.
