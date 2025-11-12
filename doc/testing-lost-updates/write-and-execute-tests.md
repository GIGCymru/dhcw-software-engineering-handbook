# Write and execute tests

Use the table below, together with your own expertise, to determine the
types of tests you need.

| **TEST TYPE** | **TYPE OF WORK PERFORMED** |
| --- | --- |
| Functional GUI testing | Often manual tests. For example, to check locking behaviour or determine what happens when a user logs in many times. The next page lists some authentic examples. |
| Functional Data testing | Using tools like SQL Server Management Studio, to check for accuracy as we load and save data in the GUI. For example, some tests on the next page check a table called *FunctionLock* to verify the lock requested in the user interface exists in the database. Combined with functional GUI testing, functional data testing is highly effective. But it has limitations. Consider the first 10 steps of [9045 Test Requesting](https://dev.azure.com/NHS-Wales-Digital/WCP/_workitems/edit/9045) What happens if both *User A* and *User B* choose the same patient at the same time? Can you be sure who gets the lock? Both? How do you guarantee the database commands execute concurrently to make sure both users are not allowed to lock the same patient record? For fine grained control you execute your functional data tests with code walk-throughs, debugging and unit tests. |
| Code walk-throughs and debugging | Ask developers to walk you through their tests and include these in your strategy and plans. |
| Non-functional stress tests | The techniques above go a long way to providing confidence. But also consider using stress tests, particularly when writing an automated software process. They need not be too involved. Developers can write simple tests using T-SQL -- see [FURTHER READING](further-reading.md). Again, include them in your strategy and plans. |
| Monitoring and surveillance | Post deployment monitoring and surveillance is beyond the scope of this guide. But teams should continue to test for lost updates and deadlocks after deployment. |
