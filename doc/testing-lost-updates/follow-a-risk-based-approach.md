# Follow a risk based approach

When preparing your tests, identify when and where failure is most
likely to occur and where impact will be most severe. The system under
test will have some potential for concurrency conflicts it *must*
manage. But what else should you consider?

While **not** an exhaustive list, nor a replacement for
your own expertise, this table sets out questions and tasks to consider.

| **Considerations** | **Tasks** |
| --- | --- |
| **Is the code multi-threaded?** Most applications rely on multi-threading even before the developer starts coding. But code that creates its own threads, poses a particular risk. Especially when writing an automated process that creates high numbers of transactions. | Ask the developers to walk you through their stress tests |
| **How many *users* and *concurrent users* do you expect?** The potential for concurrency conflicts grows with the number of *users*, particularly *concurrent* *users*. | Ask Business Analysts to walk you through the non-functional requirements. Make sure to record acceptance criteria in user stories, requirements specifications or the team's definition of done. |
| **How complicated is the approach?** We call the design to handle concurrency conflicts *concurrency control*. While there are common ways to approach this, some are more difficult to reason about and put in place. | Ask the developer or architect to walk you through the solution architecture. |
| **How mature is the implementation?** You may have already implemented concurrency control. If so, there may be less risk of it failing for a new feature.[^1] | Ask the developers to walk you through their tests. Check the team's *definition of done*. |
| **How much support does the development framework provide?** Some frameworks provide much of the heavy lifting to deal with concurrency conflicts. Oracle Forms, although now deprecated, is a good example. Entity Framework's optimistic locking another. These frameworks are tried and tested and can reduce the amount of testing required. | Ask developers how much bespoke code they have written and which framework they use. |

[^1]: For example, you may follow the *implicit lock pattern,* making it
    easier to add locks to new features.
