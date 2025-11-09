# Working with user defined functions (UDF)

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
