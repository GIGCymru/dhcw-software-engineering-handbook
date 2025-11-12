# Handling exceptions

You **SHOULD**:-

- Manage exceptions in each stored procedure, but you **SHOULD NOT**
    mask the error from the calling application.

- Use the `TRY ... CATCH` construct to handle errors in T-SQL.

- Use a log table to record errors handled. It helps with support
    and maintenance.

- Favour `THROW` over `RAISERROR` wherever possible (i.e. in database
    compatibility SQL 2012 and later.)

- Return a result code.
