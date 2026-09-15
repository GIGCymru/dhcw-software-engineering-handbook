# Follow our folder and file conventions

## Use physical folders

Typically, a legacy .NET application relies on visual studio solution
folders. These virtual folders don't represent the physical structure on
disk.

With no folders to look at, the reader is reliant on our understanding
of the project names without opening the solution. To overcome this, you
**SHOULD** follow our first convention and use physical folders and folder
names.

## Create a root folder for your solution

You **SHOULD** place your solution file in a root folder (`./<rootfoldername>`).
Doing so makes it easy for others to clone a repo and open the file to get
started. The rest of the software project lives within this root folder.

Provide a sensible name, using the name of the git repo or the solution
file.

!!! tip "Practical tips"
    If the RootFolderName does not describe the project, replace it with something more accurate and understandable.

    Do this before you commit to source control. In doing so you avoid the need for communicating a change and making source control work overtime after the initial commit.

## Provide a readme file

You **SHOULD** provide a README file (`./<rootfoldername>/readme.md`) in the
root folder as a common way of helping others learn about your software.

As a minimum, it **SHOULD** instruct others on how to build and deploy
your software. Typically, you **SHOULD** also include guidelines on how
to contribute to your project -- how to fix bugs or correct typos, for
example.

!!! tip "Practical tips"
    - Use [Microsoft's Writing Style Guide](https://docs.microsoft.com/en-gb/style-guide/welcome/) to maintain a consistent and familiar style

    - Using Markdown makes it easier to format text and include links & images

    - Describe your assurance processes (such as code reviews or gated check-ins) in a separate CONTRIBUTING.md file, saved to the root folder

    - Consider your audience. What would others find useful?

!!! info "Further reading and information"
    [Create a readme for your Git repo - Azure Repos \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/repos/git/create-a-readme?view=azure-devops)

    [About READMEs - GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

    [Welcome - Microsoft Style Guide \| Microsoft Learn](https://learn.microsoft.com/en-gb/style-guide/welcome/)

## Create a .editorconfig file

You **SHOULD** share your configuration by adding an. editorconfig file
to the root of your solution, making sure to add it to source control.
For more details, see our *General coding standard* (v4 or later).

## Use sub-folders within Visual Studio projects

You **SHOULD** use sub-folders within each project to reflect
namespacing and separate dependency layers. Doing so helps remind you
that the solution is becoming more complex as this tree grows. And
proves useful when refactoring or extending the project.

You **SHOULD** use parent names in solution subfolder names.

!!! tip "Practical tips"
    Follow SOLID principles to refactor out exposed complexities. This helps to reduce each project to its simplest form.

## Use existing conventions for project types

Some project types require you to work with a different convention.
Typically, these include web projects, MVC, web forms, APIs, or razor
pages. For example, MVC structures projects for path conventions,
whereas razor pages use folder hierarchy.

However, the project type determines this - not the software team. And
you **SHOULD** follow the namespace convention described above for any
additional folders you add to these project types.
