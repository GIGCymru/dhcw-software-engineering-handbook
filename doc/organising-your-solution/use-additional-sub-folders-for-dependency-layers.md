# Use additional sub-folders for dependency layers (/src/<dependencylayer\>)

You **SHOULD** create immediate sub-folders to separate the dependency
layers of your solution, such as data access, user interface, domain
logic or service layers. This reminds you that the layers exist and to
test them.

Including the parent's name in the sub folder name may appear
repetitive, but it adds context. And it can prove useful when
referencing it from another location or when searching for a file or
folder.

We leave naming the sub folders underneath ***src*** and **test** to
your discretion but you **SHOULD :-**

- use Pascal casing when naming folders.

- Follow [Microsoft's naming advice](https://docs.microsoft.com/en-gb/windows/desktop/fileio/naming-a-file)
    when developing for Windows systems.

You **SHOULD NOT** use special characters or abbreviations longer than
two letters in folder names.

!!! example "Examples of good practice"
    > {IMAGE PLACEHOLDER}
    Figure 1 An example.NET Solution with dependency layers

!!! info "Further reading and information"
    [Naming Files, Paths, and Namespaces - Win32 apps \| Microsoft Learn](https://learn.microsoft.com/en-gb/windows/win32/fileio/naming-a-file)
