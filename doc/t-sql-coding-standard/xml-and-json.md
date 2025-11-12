# XML and JSON

You **SHOULD** use SQL Server XML and JSON functions & methods[^1] to
build and consume XML and JSON data.

You **SHOULD NOT**:-

- Build XML or JSON by concatenating strings. The loop construct
    hinders performance and can provide data in an invalid data format.

- Use XML or JSON data type methods and functions in a `WHERE`
    or `JOIN` clause, except when working with small result sets in
    a temporary table or table variable.

[^1]: Available in SQL Server 2016 onwards
