# General good practice

You **MUST** store T-SQL scripts and database code in source control as a
'single source of truth.'

You **SHOULD**: -

- Check your SQL application is performant. You may find your
    support team or Database Administrator (DBA) may be able to help.

- Review your code to address any issues, such as performance and
    security considerations.

- Share code using code snippets and a common repository.

- Conform to ANSI standards wherever possible.

- Prefer `CAST` to `CONVERT`

- Prefer `SET` to `SELECT` when assigning variables.

- Prefer `COALESCE` to `ISNULL`

- Format and analyse your code using SQL Prompt before checking into
    source control.

- Configure SQL Prompt using our config files. See [SQL Prompt
    configuration](sql-prompt-configuration.md) for help.

You **SHOULD NOT**:-

- Use deprecated features.

- Use dynamic SQL. If you cannot avoid this then call it using
    `sp_executesql` rather than the `EXECUTE` statement.

- Expect your DBA to performance tune your queries but do ask them for
    advice. Particularly what tools to use.

- Use undocumented stored procedures.

- Create objects that flout the single responsibility pattern. Such
    as: -

1. Entity-attribute-value tables.

2. Generic stored procedures with no specific (or multiple) use cases.

3. Using a single table to hold all lookup values, metadata, and domain or reference data.

!!! tip "Practical tips"
    **WPRS -- Prioritisation incident**

    In 2016, a failure to run SQL code analysis checks and deploy from source control prevented referrals including those for urgent suspected cancer being actioned.

    WPRS -- WPAS (Welsh Patient Administration System) delayed Urgent Suspected Cancer referral.

    In 2017, a failure to deploy the correct stored procedure led to a delay in referring a patient with urgent suspected cancer.

!!! info "Further reading and information"
    [How to Think Like the SQL Server Engine - Brent Ozar Unlimited®](https://www.brentozar.com/training/think-like-sql-server-engine/)

    [SQL Code Smells - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/sql-code-smells/)

    [Discontinued database engine functionality - SQL Server \| Microsoft Learn](https://learn.microsoft.com/en-gb/sql/database-engine/discontinued-database-engine-functionality-in-sql-server?view=sql-server-ver16)

## Avoid using T-SQL to execute business logic

As a rule, you **SHOULD NOT** place business logic in the database.

!!! info "Further reading and information"
    [Should we use stored procedures or queries built in the app? - Brent Ozar Unlimited®](https://www.brentozar.com/archive/2019/03/should-we-use-stored-procedures-or-queries-built-in-the-app/)

## Follow these rules when using an object relational mapper (ORM)

You **MUST** consider this standard when using an Object-relational
mapping (ORM) tool such as Microsoft's Entity Framework. And to achieve
the best performance from your database: -

- You **SHOULD** use stored procedures for data access. Support tools
    (such as those used for SQL Migrations) cannot identify issues with
    code that is not stored in the database.

- You **SHOULD** follow good practice if working with ORMS. See ORM
    tips, below.

- You **SHOULD NOT** use Entity Framework's code first approach to
    create and maintain database schemas.

!!! info "Further reading and information"
    [45 Database Performance Tips for Developers \| Redgate (red-gate.com)](https://www.red-gate.com/library/45-database-performance-tips-for-developers) ORM Tips (pages 4 & 5)
