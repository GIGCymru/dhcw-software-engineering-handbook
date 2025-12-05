# Organise your solution to accord with our conventions

You **SHOULD** organise your solution according to our standards. They
follow those used by many language ecosystems, including the .NET source
code itself. Note that they differ from the typical Visual Studio *File
New* defaults.

There are two choices, as shown below. This document describes the
first, which suits a Behavioural Driven Development \[BDD\] approach.
But they are very similar and equally valid.

Organizing your software solution - option #1 (suits a BDD approach):

!!! example "Examples of good practice"
    ```sh
        └──{RootFolderName}/        # Root folder for your entire software solution
            ├── deploy/             # Any infrastructure provisioning scripts
            ├── build/              # Any published build outputs
            │   └── scripts/        # Build scripts and CI scripts not required in the root
            ├── examples/           # Samples and demos on how to build or consume your app
            ├── specs/              # Container folder for tests and documentation
            │   ├── docs/           # Diagrams, specifications and documentation
            │   └── test/           # Automated tests and feature files
            ├── src/                # Source code separated by dependency layer subfolders
            ├── README.md           # Starting point for anyone building or using your software
            ├── .editorconfig       # Enforces a consistent coding style for your project
            └── {SolutionName}.sln  # Solution file
    ```

Organizing your software project - option #2:

!!! example "Examples of good practice"
    ```sh
        └──{RootFolderName}/        # Root folder for your entire software solution
            ├── deploy/             # Any infrastructure provisioning scripts
            ├── build/              # Any published build outputs
            │   └── scripts/        # Build scripts and CI scripts not required in the root
            ├── docs/               # Diagrams, specifications and documentation
            ├── examples/           # Samples and demos on how to build or consume your app
            ├── src/                # Source code separated by dependency layer subfolders
            ├── test/               # Automated tests
            ├── README.md           # Starting point for anyone building or using your software
            ├── .editorconfig       # Enforces a consistent coding style for your project
            └── {SolutionName}.sln  # Solution file
    ```

An Example .Net Solution which follows our conventions:

> {IMAGE PLACEHOLDER}

!!! tip "Practical tips"
    - Use the approach that best matches your needs

    - In later versions of .NET use C:\\> dotnet new gitignore to generate a .gitignore file

    - Clone our example project structure from the Software Development Standards project in Azure DevOps.

!!! info "Further reading and information"
    [An Opinionated Approach to ASP.NET Core - Scott Allen - YouT ube](https://www.youtube.com/watch?app=desktop&v=6Fi5dRVxOvc)

    [.NET Core Opinion #1 - Structuring a Repository (odetocode.com)](https://odetocode.com/blogs/scott/archive/2018/08/28/net-core-opinion-1-structuring-a-repository.aspx)

    [.NET Core Opinion #2 - Managing a Repository Structure (odetocode .com)](https://odetocode.com/blogs/scott/archive/2018/09/06/net-core-opinion-2-ndash-managing-a-repository-structure.aspx)

    [.NET Core Opinion #3 - Other Folders to Include in the Source Repository (odetocode.com)](https://odetocode.com/blogs/scott/archive/2018/09/13/net-core-opinion-3-ndash-other-folders-to-include.aspx)

    [Create .NET Projects Using Standard Practices \| Toptal](https://www.toptal.com/dot-net/bootstrap-and-create-dot-net-projects)

    [Common web application architectures \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures)

    [Behaviour-Driven Development - Cucumber Documentation](https://cucumber.io/docs/bdd/)

    [.NET project structure · Gi tHub](https://gist.github.com/davidfowl/ed7564297c61fe9ab814)

    [GitHub - github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore)
