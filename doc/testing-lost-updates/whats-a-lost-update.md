# What's a lost update

A lost update can occur when two or more *users* change a shared piece
of data at the same time. A *user* is a person or automated process.
Consider this hypothetical example:

1. Dr Rick Dagless loads patient X's data onto a web form, to record
    their allergy to penicillin.

2. Meanwhile, Dr Liz Asher also loads patient X's data. She clicks a
    checkbox to record that the patient lives alone and immediately
    saves her changes.

3. Rick saves his changes with *lives alone* unchecked. In doing so he
    unknowingly overwrites Liz's change.

We call the action of loading and saving changes to data a
*transaction*. When the result of one transaction is dependent on the
sequence or timing of another, it's called a *concurrency conflict* or
*race condition*.

In our example, the result is the loss of a lasting record that the
patient lives alone. And this is a patient safety concern - imagine if
the checkbox indicated the need to refer the patient for urgent
treatment!
