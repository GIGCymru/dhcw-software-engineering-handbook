# Adopt trunk-based development and continuous integration

Trunk-Based Development simplifies source control by deploying directly
from the trunk branch (e.g., main or master). You **SHOULD** adopt this
approach where feasible, as it minimises the complexity of managing
long-lived branches.

**RECOMMENDATIONS**:

- Write a comprehensive suite of automated tests to keep branches
    deployable.

- Aim for continuous integration and frequent deployments from the
    trunk.

**When to Consider Alternatives**:

If your project requires extensive experimentation or long-term feature
development, ensure robust practices for merging changes from feature
branches.

!!! info "Further reading and information"
    [It's Not Continuous Delivery If You Can't Deploy Right Now - YouTube](https://www.youtube.com/watch?v=po712VIZZ7M)

    [Git patterns and anti-patterns for successful developers - YouTube](https://www.youtube.com/watch?v=t_4lLR6F_yk)
