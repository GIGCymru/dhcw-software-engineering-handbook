# Views

You **SHOULD NOT**:-

- Define nested views. Views that call or join to other views can
    result in complex query plans.

- Use wildcards in view definitions as it can result in unexpected
    behaviour[^1].

- Use `ORDER BY` in views. Use the `ORDER BY` clause only in the outermost
    query.

[^1]: This is caused because SQL Server caches the view's output
    metadata but doesn't update the cache when underlying objects
    change.
