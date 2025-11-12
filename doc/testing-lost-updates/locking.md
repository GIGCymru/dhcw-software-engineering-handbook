# Locking

Locking prevents concurrency conflict, eliminating the potential for
lost updates. Locking designs take into consideration the chance of a
conflict occurring and the scope to which we should apply the lock.

## Pessimistic or optimistic

***Pessimistic locks*** expect conflict, so they block access to one
user at a time. Whether you apply the lock on *View* or *Edit* depends
on the requirements. But other users must wait for the lock to release.

Applying *pessimistic* locking in our example means Liz must wait for
Rik to save changes before she can edit.

By contrast, ***Optimistic locking*** does not block access because
it does not expect a conflict to occur. But it does stop a user from
saving changes if the data has changed.

Applying this to our example, Rik is forced to reload the data (with
Liz's changes) and start again.

## Coarse or fine grained

Based on requirements, locks may apply to the entire patient record -
spanning many data entry forms. Or they may apply to a specific field or
fields[^1] - on an active part of a form for example.

Any locking strategy must also ensure data integrity. A locking strategy
that allows users to assign an invalid combination of GP and GP Practice
is still wrong!

## No locking, but validation checks

Rather than locking, applications may check updates are consistent with
existing data. Serializing database access and updating only the fields
that change is one approach.

## No concurrency controls

Typically the system under test will need to manage concurrency
conflicts. But it may not always be necessary. Make sure to find out!

!!! tip "Practical tips"
    Even if a requirements specification omits concurrency control it does not necessarily mean it is not needed. Encourage your business analysts, architects and developers to record it in their documentation!

[^1]: Although locking at field level is unlikely to be practical for Pessimistic locking.
