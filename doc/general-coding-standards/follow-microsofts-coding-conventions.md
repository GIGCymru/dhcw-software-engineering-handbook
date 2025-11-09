# Follow microsoft's coding conventions

Follow Microsoft's [C# coding
conventions](https://learn.microsoft.com/en-gb/dotnet/csharp/fundamentals/coding-style/coding-conventions)
and [Framework Design
Guidelines](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/).
There are a couple of exceptions, but we make these clear.

!!! tip "Practical tips"
    If the conventions described here do not meet your team's needs and you want to create your own, please speak to the Software Development Manager.

## Naming

You **SHOULD**:

- Follow Microsoft's naming conventions, considering our additional
    guidance.

- Use Attribute and Exception suffixes only when they clarify intent.

- Apply Roy Osherove's naming convention for tests, allowing
    underscores. See our [examples](examples.md).

- Use NhsWales for the company name in namespaces. See [examples](examples.md).

- Name booleans to reflect true/false questions. See [examples](examples.md).

You **SHOULD NOT**:

- Use "And", "Or" or generic terms like "Util" or "Common" in
    class names.

- Add prefixes or suffixes except where standard conventions apply.
      See our [examples](examples.md).

!!! info "Further reading and information"
    [C# Naming Conventions \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/fundamentals/coding-style/coding-conventions#naming-conventions)

    [Naming Guidelines - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/naming-guidelines)

    [Capitalisation Conventions - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/capitalization-conventions)

    [General Naming Conventions - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/general-naming-conventions)

    [Names of Assemblies and DLLs - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/names-of-assemblies-and-dlls)

    [Names of Namespaces - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/names-of-namespaces)

    [Names of Classes, Structs, and Interfaces - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/names-of-classes-structs-and-interfaces)

    [Names of Type Members - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/names-of-type-members)

    [Naming Parameters - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/naming-parameters)

    [Naming Resources - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/naming-resources)

## Layout

You **SHOULD:**

- Follow Microsoft's layout conventions.

- Use continuation lines to avoid excessive scrolling and indent with
    four spaces.

- Indent wrapped statements to keep logically related segments
    aligned.

- Use whitespace effectively to enhance readability.

- Insert empty lines to separate code blocks.

- Align curly braces vertically.

For C#, place each curly brace on a new line, aligned with the start of
the code block.

For JavaScript and Razor, place the opening curly brace on the same line
as the construct to prevent issues with automatic semicolon insertion.
Exceptions apply in specific cases.

You **SHOULD NOT:**

- Use unnecessary vertical whitespace -- and so prevent extra
    scrolling.

- Overuse indentation.

- Omit optional curly braces, as this increases error risk. Use them
      judiciously when it improves readability. See [examples](examples.md).

!!! info "Further reading and information"
    [C# Layout Conventions \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/fundamentals/coding-style/coding-conventions#layout-conventions)

## Comments

You **SHOULD**:

- Follow Microsoft's commenting conventions.

- Use comments to explain the problem your code solves, not the code
      itself.

- Write expressive, readable code.

- Prefer automated tests rather than rely on code comments or
      excessive documentation.

- Remove unused code instead of commenting it out. See
      [examples](../t-sql-coding-standard/code-comments.md).

- Add comments to code commits, following the Conventional Commits
      specification.

- Use well-named automated tests as part of your documentation (see
      [naming](../restful-api-standards/naming.md) guidelines).

- Use enumerations to self-document code and make it searchable in
      Visual Studio.

- Ensure comments are grammatically correct and properly punctuated.

You **SHOULD NOT**:

- Comment to explain how C# or the .NET Class Library works.

- Add unnecessary or redundant comments. For example, at the top of
      methods or classes. Provide a concise summary instead.

!!! info "Further reading and information"
    [.NET Coding Conventions - C# - comment style \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/fundamentals/coding-style/coding-conventions#comment-style)

    [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

## Variables and parameters

You **SHOULD**:

- Declare C# variables close to where they are used.

- Initialize variables at the point of declaration, when possible.

- Declare JavaScript variables at the top of their scope and consider
      using 'strict mode' to prevent hoisting.

- Order parameters consistently.

- Use named parameters to improve code readability. See [examples](examples.md).

- Avoid methods with more than three parameters.

You **SHOULD NOT**:

- Declare all variables at the beginning of a class out of habit.

!!! info "Further reading and information"
    [Member Design Guidelines - Framework Design Guidelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/design-guidelines/member)

    [Understanding Hoisting in JavaScript \| DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-hoisting-in-javascript)

## Conditionals and control flow statements

You **SHOULD:**

- Define conditionals in the positive (see examples).

- Prefer constants or enumerations over hard-coded numerical values
    ('magic numbers'). Use named constants to improve readability.

- Order case/switch statements logically and always include a default
    statement.

- Ensure conditionals are clear and easy to understand.

- Minimise nested conditionals where possible.

!!! tip "Practical tips"
    Where practical, place enumerations in a namespace in their own code file.

!!! info "Further reading and information"
    [C# static code analysis- Magic numbers should not be used](https://rules.sonarsource.com/csharp/RSPEC-109/)

## Exception handling and defensive coding

You **SHOULD**:

- Implement a global exception handler.

- Move complex code out of try blocks into separate methods.

- Handle exceptions locally, when possible, but avoid catching
    unresolvable exceptions -- let them bubble up to the global handler.

- Log exceptions with relevant details, including stack trace and
    context.

- Use guard clauses to validate inputs early.

- Use multiple return statements to avoid deep indentation.

- Avoid silent exceptions -- always log or rethrow as needed.

- Catch specific, rather than generic, exceptions for precise
    handling.

- Test exception handling to ensure proper behaviour, especially in edge cases.

!!! info "Further reading and information"
    [Best Practices for exceptions - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/exceptions/best-practices-for-exceptions)
