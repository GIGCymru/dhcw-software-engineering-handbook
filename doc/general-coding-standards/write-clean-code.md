# Write clean code

Your code **SHOULD**:

- Be concise, expressive and focused on doing one thing well.

- Use short methods (20-40 lines) with a single purpose.

- Include written tests, be self-documenting and easy to read.

- Have classes with high cohesion, containing clearly related methods that share class properties.

- Prefer using or import statements instead of fully qualified type names.

Your code **SHOULD NOT**:

- Contain unused using (Java) or import (C#) statements.

!!! tip "Practical tips"
    Use the using static directive (C#6) to ensure method names are prefixed with their class for clarity.

    Consider global using directives and implicit usings to reduce clutter and improve readability.

!!! info "Further reading and information"
    [Create readable code with conventions, whitespace, and comments in C# - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/csharp-readable-code/)

    [Welcome to C# 10 - .Net Blog (Microsoft.com)](https://devblogs.microsoft.com/dotnet/welcome-to-csharp-10/)
