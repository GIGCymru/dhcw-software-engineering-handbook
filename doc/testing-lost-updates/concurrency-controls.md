# Concurrency controls

The table shown below describes common approaches to concurrency
control.

|  | **Pessimistic or Optimistic?** | **Coarse grained or Fine grained?** |
| --- | --- | --- |
| **Locking** | *Pessimistic* - locks on View/Edit. *Optimistic* - Blocks on save - not really a lock. | *Coarse grained* -- locks the entire record. *Fine grained* -- locks the active field(s). |
| **Validation checks** | Users may unknowingly overwrite changes with their own, but validity is assured. |  |
| **No control** | The specification limits access to a single user per record at a time. |  |
