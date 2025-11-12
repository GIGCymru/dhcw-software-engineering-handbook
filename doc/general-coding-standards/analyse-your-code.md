# Analyse your code

## Create a plan

You **MUST** conduct code analysis and address the issues you find.
Doing this in both your IDE and build & integration pipelines will
improve your code, making it easier to maintain, faster, and more
secure.

Code analysis can be complex, but this section outlines the steps you
**SHOULD** follow. Create a tailored plan for your team that you
regularly review and improve.

!!! tip "Practical tips"
    Use Redgate SQL Prompt to evaluate T-SQL. See the T-SQL coding standard for help.

!!! info "Further reading and information"
    [T-SQL Coding Standard](../t-sql-coding-standard/introduction.md)

    [What is Static Analysis? An Explanation for Everyone - NDepend](https://blog.ndepend.com/static-analysis-explanation-everyone/)

    [Enabling High-Quality Code in .NET \| Milan Milanović (milanovic.org)](https://milan.milanovic.org/post/enabling-high-code-quality-in-net/)

## Calculate code metrics to spot problems

Calculate code metrics for each project in your solution and address any
that exceed acceptable limits. The table below shows **RECOMMENDED**
levels for each metric.

|  | **Maintainability Index** | **Cyclomatic Complexity** | **Depth of Imheritance** | **Class Coupling** | **Lines of Executable code** |
| --- | --- | --- | --- | --- | --- |
|  | 20 - 100 | < 7 | < 5 | < 9 | < 40 |

## Calculate code coverage

Calculate test coverage and use the results to identify areas for
improvement.

Generate and publish a code coverage report in your pipelines.

!!! tip "Practical tips"
    Aim to cover a large portion of your code with tests. But prioritise integration tests for areas prone to regressions. This may prove more effective than having unit tests for every method.

    Note: Visual Studio's code coverage feature is available only in the Enterprise edition.

!!! info "Further reading and information"
    [Calculate code metrics - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/code-quality/code-metrics-values?view=vs-2022)

    [Selective Unit Testing -- Costs and Benefits (stevensanderson.com)](http://blog.stevensanderson.com/2009/11/04/selective-unit-testing-costs-and-benefits/)

    [Use code coverage for unit testing - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/core/testing/unit-testing-code-coverage?tabs=windows)

    [Code coverage testing - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/test/using-code-coverage-to-determine-how-much-code-is-being-tested?view=vs-2022&tabs=csharp)

    [Publish Code Coverage Results task - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/tasks/test/publish-code-coverage-results?view=azure-devops)

    [Exercise - Perform code coverage testing - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/run-quality-tests-build-pipeline/6-perform-code-coverage)

## Check code for style and quality

Ensure your code follows the style ([naming](follow-microsofts-coding-conventions.md#naming),
[layout](follow-microsofts-coding-conventions.md), [language](follow-microsofts-coding-conventions.md))
and quality conventions described or referenced in this document.

### Code Style Options and Analyser Rules

Visual Studio offers a code style options box and Roslyn analyser code
style rules. With newer versions of Visual Studio and the .NET SDK, you
can run these rules at build time.

Use the dotnet format tool in your build and integration pipelines to
check for code style. See later in this section for details.

## Use roslyn analysers to ensure .NET code quality

Use Roslyn compiler analysers to check .NET code for style, quality,
maintainability and other issues. They are available from Microsoft and
third-party providers.

**How Roslyn Analysers work**:

- **Design-Time Analysis**: Analysers run on open files in the IDE,
    providing immediate feedback.

- **Build-Time Analysis**: Can be configured to run during builds to
    enforce consistent standards.

Use NuGet packages to integrate analysers directly in your code. Avoid
relying solely on IDE-specific tools like Visual Studio extensions,
ReSharper and SonarQube.

### Default Analysers in .NET SDKs

The latest .NET SDKs include many Roslyn analysers pre-installed. The
image below shows the analysers available when creating an ASP.NET
project targeting .NET 8.0 in Visual Studio.

If using older SDKs, add analysers like
Microsoft.CodeAnalysis.NetAnalyzers NuGet package.

Figure 1 Use Roslyn analysers to check your code

> {IMAGE PLACEHOLDER}

### Third-party Analysers

Include a security analyser, such as SonarAnalyzer.CSharp or
SecurityCodeScan.VS2019. For assistance, ask the Software Development
Manager or Cyber Security team.

### Enabling Rules

Roslyn analysers allow you to configure specific rules. In a .NET 6.0+
project, created with Visual Studio, only a few rules are enabled by
default. Enable all relevant rules, disabling only those that produce
false positives or are not relevant.

!!! tip "Practical tips"
    **Introducing Code Analysis**: Enabling code analysis with all rules on a large codebase can be overwhelming. Start with a few rules and gradually add more until all are enabled.

    **Important:** Code analysis may slow down your development environment. Balance error detection with productivity. Consider running resource-intensive analysis in build or integration pipelines.

!!! info "Further reading and information"
    [Seven reasons that Roslyn-based Code Analysers are awesome \| Tom Wrights Code (tdwright.co.uk)](https://blog.tdwright.co.uk/2018/12/10/seven-reasons-that-roslyn-based-code-analysers-are-awesome/?preview=true)

    [The .NET Compiler Platform SDK (Roslyn APIs) \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/roslyn-sdk/)

    [Code analysis documentation - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/code-quality/?view=vs-2022)

    [Code analysers for .NET Framework \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/framework/code-analyzers#main)

    [Legacy analysis for managed code - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/code-quality/static-code-analysis-for-managed-code-overview?view=vs-2022)

    [Retrofitting code analysis to legacy projects -- (tdwright.co.uk)](https://blog.tdwright.co.uk/2018/12/13/retrofitting-code-analysis-to-legacy-projects-my-4-step-strategy-for-long-term-success/)

    [Understanding the impact of Roslyn Analysers on build time - Meziantou's blog](https://www.meziantou.net/understanding-the-impact-of-roslyn-analyzers-on-the-build-time.htm)

    [Favourite code analysis tools for .NET Core devs on Azure (zimmergren.net)](https://zimmergren.net/code-analysis-tools-for-azure-developers-coding-dotnet-core/)

    **Roslyn Team analysers**

    [NuGet Gallery \| Microsoft.CodeAnalysis.NetAnalyzers 9.0.0](https://www.nuget.org/packages/Microsoft.CodeAnalysis.NetAnalyzers#dependencies-body-tab)

    [NuGet Gallery \| Roslyn Team](https://www.nuget.org/profiles/RoslynTeam)

    **Roslynator**

    [NuGet Gallery \| Roslynator.Analyzers 4 .12.10](https://www.nuget.org/packages/Roslynator.Analyzers/)

    **xUnit**

    [NuGet Gallery \| xunit.analyzers 1.19.0](https://www.nuget.org/packages/xunit.analyzers/)

    **Style Cop**

    [NuGet Gallery \| StyleCop.Analyzers 1.1.118](https://www.nuget.org/packages/StyleCop.Analyzers/)

    **Security source code analysers**

    [NuGet Gallery \| SonarAnalyzer.CSharp 10.5.0. 109200](https://www.nuget.org/packages/SonarAnalyzer.CSharp/)

    [Static analysers - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/static-analyzers/)

    [NuGet Gallery \| SecurityCodeScan.VS2019 5.6.7](https://www.nuget.org/packages/SecurityCodeScan.VS2019/)

    [Source Code Security Analysers \| NIST](https://www.nist.gov/itl/ssd/software-quality-group/source-code-security-analyzers)

    [Source Code Analysis Tools \| OWASP Foundation](https://owasp.org/www-community/Source_Code_Analysis_Tools)

    [Code analysis \| ReSharper (jetbrains.com)](https://www.jetbrains.com/help/resharper/Code_Analysis__Index.html) **ASP.NET analysers**

    [Code analysis in ASP.NET Core apps \| Microsoft Learn](https://learn.microsoft.com/en-gb/aspnet/core/diagnostics/code-analysis?view=aspnetcore-6.0)

    [Analysers for ASP.NET Core in .NET 6 (andrewlock.net)](https://andrewlock.net/exploring-dotnet-6-part-7-analyzers-for-minimal-apis/)

    **ReSharper**

    [Code analysis \| ReSharper (jetbrains.com)](https://www.jetbrains.com/help/resharper/Code_Analysis__Index.html)

## Configure code analysis rules

Follow these steps when configuring code analysis:

| **CONFIGURATION STEP** | **Details** |
| --- | --- |
| **ADD AN .editorconfig FILE** | Place in the root of your solution and commit to source control to ensure consistent settings across the team. |
| **SET-UP INITIAL RULES** | Generate settings using Visual Studio's code style options or a template (see further reading). Adjust rules to align with team or organisational conventions. |
| **DEFINE RULE SEVERITY** | Set critical rules to *error* to ensure violations fail the build. Configure the Directory.build.props or .csproj files (SDK-style projects) to enable style and quality checks during builds. |
| **ENFORCE CODE STYLE** | Enforce code style checks during builds where your .NET version supports it. |
| **APPLY GOOD PRACTICE** | Treat warnings as errors to promote higher code quality. |

!!! tip "Practical tips"
    Be mindful of the challenges with .editorconfig, including known Visual Studio UI limitations. Read this blog before you start! --

    [C# code style by EditorConfig in .NET 5 SDK and beyond \| Mews Developers](https://developers.mews.com/c-code-style-by-editorconfig-in-net-5-sdk-and-beyond/)

You **MAY** develop team-specific styles if the provided conventions
don't meet your needs.

!!! note ".editorconfig"
    [How to enforce a consistent coding style in your projects - Meziantou's blog](https://www.meziantou.net/how-to-enforce-a-consistent-coding-style-in-your-projects.htm)

    [EditorConfig](https://editorconfig.org/)

    [Code style options and code cleanup - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/ide/code-styles-and-code-cleanup?view=vs-2019)

    [Enforce code style rules - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/ide/csharp-developer-productivity?source=recommendations&view=vs-2022#enforce-code-style-rules)

    [.NET code style rule options - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/fundamentals/code-analysis/code-style-rule-options)

    [C# editor formatting options - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/ide/reference/options-text-editor-csharp-formatting?view=vs-2022)

!!! note ".editorconfig templates"
    [EditorConfig settings - Visual Studio (Windows) \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/ide/create-portable-custom-editor-options?view=vs-2022)

    [project-system/.editorconfig at main · dotnet/project-system · GitHub](https://github.com/dotnet/project-system/blob/main/.editorconfig)

    [roslyn/.editorconfig at main · dotnet/roslyn · GitHub](https://github.com/dotnet/roslyn/blob/main/.editorconfig)

!!! note ".csproj config"
    [Code Analysis: MSBuild properties for Microsoft.NET.Sdk - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/core/project-sdk/msbuild-props#code-analysis-properties)

    [Enable NET Analyzers: MSBuild properties for Microsoft.NET.Sdk - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/core/project-sdk/msbuild-props#enablenetanalyzers)

    [C# Compiler Options - errors and warnings \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/language-reference/compiler-options/errors-warnings#treatwarningsaserrors)

## Run code analysis in your pipelines as well as the IDE

Run code analysis during builds catch issues early, using tools
like **MSBuild** & **dotnet format**.

!!! info "Further reading and information"
    [Enforce .NET code style in CI with dotnet format - Meziantou's blog](https://www.meziantou.net/enforce-dotnet-code-style-in-ci-with-dotnet-format.htm#azure-pipelines)

## Check third-party packages

Check for vulnerabilities and licence issues in third-party dependencies
by integrating tools like **GitHub Advanced Security for Azure DevOps**.

!!! info "Further reading and information"
    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [Software Composition Analysis - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/software-composition-analysis/)

## Publish and review metrics

Track code health by publishing metrics from analysis tasks to server
dashboards.

Regularly review these metrics and address problem areas to maintain
quality.

!!! info "Further reading and information"
    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [Generate code metrics from the IDE or command line - Visual Studio (Windows) \| Microsoft Learn ](https://learn.microsoft.com/en-gb/visualstudio/code-quality/how-to-generate-code-metrics-data?view=vs-2022)

    [Publish Code Coverage Results task - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/tasks/test/publish-code-coverage-results?view=azure-devops)

    [Exercise - Perform code coverage testing - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/run-quality-tests-build-pipeline/6-perform-code-coverage)

## Recap

!!! note "Recap: Analyse your code"
    1. Create a plan.

    2. Calculate code metrics.

    3. Calculate code coverage.

    4. Check for code style and quality.

    5. Use Roslyn analysers.

    6. Configure code analysis rules.

    7. Run code analysis in your build pipelines.

    8. Check third party packages.

    9. Publish metrics.
