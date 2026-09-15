# Exceptions and good practice checklist

## Exceptions

While there may be reasons to deviate from this guide, exceptions should
be rare and carefully considered.

!!! tip "Practical tips"
    Discuss with colleagues and hold code reviews to ensure a shared understanding of our standards.

!!! info "Further reading and information"
    [Giving code a good name - Kevlin Henney - YouTu be](https://www.youtube.com/watch?v=CzJ94TMPcD8)

    [Clean Coders Hate What Happens to Your Code When You Use These Enterprise Programming Tricks - YouTu be](https://www.youtube.com/watch?v=FyCYva9DhsI)

    [Seven ineffective coding habits of many programmers - Kevlin Henney - YouTu be](https://www.youtube.com/watch?v=oyyFKHpzL0Q)

    [Uses and misuses of implicit typing \| Microsoft Learn](https://learn.microsoft.com/en-gb/archive/blogs/ericlippert/uses-and-misuses-of-implicit-typing)

## Essential good practice checklist

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 1 | Your code is terse, expressive and underpinned with coded tests. | ☐ | [Write clean code](write-clean-code.md) | \- |
| 2 | Classes follow SOLID principles. | ☐ | [Follow SOLID principles](follow-solid-principles.md) | \- |
| 3 | You follow Microsoft's C# coding conventions and Framework Design Guidelines. | ☐ | [Follow Microsoft's coding conventions](follow-microsofts-coding-conventions.md) | *Unless you have agreed to follow a local coding standard.* |
| 4 | You handle exceptions and use defensive coding techniques. | ☐ | [Exception handling and defensive coding](follow-microsofts-coding-conventions.md) | \- |
| 5 | You calculate code metrics. | ☐ | [Calculate code metrics](analyse-your-code.md) |  |
| 6 | You calculate code coverage. | ☐ | [Calculate code coverage](analyse-your-code.md) |  |
| 7 | You analyse code for style and quality. | ☐ | [Check code for style and quality](analyse-your-code.md) |  |
| 8 | You analyse code for security vulnerabilities. | ☐ | [Analyse your code](analyse-your-code.md) |  |
| 9 | You share your analysis rules in source control. | ☐ | [Analyse your code](analyse-your-code.md) |  |
| 10 | You perform code analysis in build pipelines. | ☐ | [Run code analysis in your pipelines](analyse-your-code.md#run-code-analysis-in-your-pipelines-as-well-as-the-ide) |  |
| 11 | You check third party dependencies for security vulnerabilities. | ☐ | [Check third-party packages](analyse-your-code.md) |  |
| 12 | You publish metrics to your dashboards. | ☐ | [Publish and review ,metrics](analyse-your-code.md) |  |
