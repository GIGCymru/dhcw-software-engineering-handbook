# Top (n) and order by

You **SHOULD** try to order result sets in the application layer.
Because qualifying statements with `ORDER BY` are expensive in SQL!

You **SHOULD NOT**:-

- Use `SET ROWCOUNT`. Prefer the `TOP(N)` syntax of the `SELECT`
    statement.

- Use `TOP` in a `SELECT` list without using `ORDER BY`
     It's clear and returns consistent results.

- Use constants in an `ORDER BY` clause; It's deprecated and makes
    code hard to read.

!!! info "Further reading and information"
    [Avoid using constants in an ORDER BY clause \| Redgate (red-gate.com)](https://www.red-gate.com/hub/product-learning/sql-prompt/avoid-using-constants-in-an-order-by-clause)
