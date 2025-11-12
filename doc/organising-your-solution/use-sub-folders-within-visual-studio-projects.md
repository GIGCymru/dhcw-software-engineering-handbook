# Use sub-folders within visual studio projects

You **SHOULD** use sub-folders within each project to reflect
namespacing and separate dependency layers. Doing so helps remind you
that the solution is becoming more complex as this tree grows. And
proves useful when refactoring or extending the project.

You **SHOULD** use parent names in solution subfolder names.

!!! tip "Practical tips"
    Follow SOLID principles to refactor out exposed complexities. This helps to reduce each project to its simplest form.
