# Working with database objects: views, functions, triggers, jobs and permissions

## Views

You **SHOULD NOT**:-

- Define nested views. Views that call or join to other views can
    result in complex query plans.

- Use wildcards in view definitions as it can result in unexpected
    behaviour[^1].

- Use `ORDER BY` in views. Use the `ORDER BY` clause only in the outermost
    query.

## Working with user defined functions (UDF)

You **SHOULD**:-

- Use inline table valued functions instead of scalar functions
    where possible.

- Use WITH SCHEMABINDING for non-data accessing scalar user
    defined functions. It forces SQL server to check data access is
    occurring at design time. Thus, preventing the need to do so during
    execution.

You **SHOULD NOT**:-

- Use multi-statement table valued functions; these can impede
    performance.

- Use side-effecting operators within a user defined function, for
    example `SELECT`, `PRINT`, `INSERT`, `UPDATE`, `TRY`, `CATCH`

!!! info "Further reading and information"
    [TSQL User-Defined Functions: Ten Questions You Were Too Shy to Ask - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/learn/tsql-user-defined-functions-ten-questions-you-were-too-shy-to-ask/)

## Working with triggers

You **SHOULD NOT**:-

- Use triggers. They can affect performance and hide business logic.
    Consider moving the required logic to another part of the
    application. It makes support and maintenance easier!

- Return data from a trigger using either `SELECT` or `PRINT`.

!!! info "Further reading and information"
    [Triggers: Threat or Menace? - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/triggers-threat-menace/)

## Working with SQL server agent

You **SHOULD**:-

- Define job steps that call stored procedures.

- Make sure jobs exist across all your high-availability SQL instances
    (e.g., both side of the mirror, availability group nodes.)

- Add an initial step to jobs on mirrors to allow the job to stop with
    a warning rather than error.

- Make use of the job categories

- Use job categories or the description field to track temporarily
    disabled and retired jobs.

You **SHOULD NOT** define job steps with ad-hoc SQL; It hides
application logic, and you are unable to manage it using SQL Source
Control.

## Permissions

You ****SHOULD**:-

- Define database roles for the specific type of database access
    required.

- Grant database object permissions *only* to database roles.

- Grant database access to Active Directory groups and service
    accounts via membership of database roles.

- Record information about the accounts you create and the permissions
    you assign them in each environment.

You **SHOULD NOT**:-

- Instinctively grant database owner (dbo) permissions.

- Use SQL Server logins, unless working with a 3rd party application
    that specifically requires their use.

- Grant database access to individual user accounts.

[^1]: This is caused because SQL Server caches the view's output
    metadata but doesn't update the cache when underlying objects
    change.
