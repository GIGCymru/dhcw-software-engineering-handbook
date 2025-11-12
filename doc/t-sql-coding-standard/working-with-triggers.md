# Working with triggers

You **SHOULD NOT**:-

- Use triggers. They can affect performance and hide business logic.
    Consider moving the required logic to another part of the
    application. It makes support and maintenance easier!

- Return data from a trigger using either `SELECT` or `PRINT`.

!!! info "Further reading and information"
    [Triggers: Threat or Menace? - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/triggers-threat-menace/)
