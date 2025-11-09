# Compound collection operations

When paging, filtering & sorting operations are performed together, the
evaluation order **MUST** be:

1. **Filtering:** All filtering expressions, including range queries,
    **MUST** be applied using an AND operation.

2. **Sorting:** The filtered list **MUST** be sorted according to the
    specified sort criteria.

3. **Paging:** The sorted, filtered list **MUST** then be paged. This
    applies to both token-based and client-driven paging.
