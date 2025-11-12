# Follow these rules when using an object relational mapper (orm)

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
