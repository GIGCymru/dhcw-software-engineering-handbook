# Enabling GitHub advanced security

Enabling **GitHub Advanced Security** helps you find & fix security
issues in your code but does incur extra costs. So, check with your line
manager or Organisation Owner before enabling it.

The following practices are **RECOMMENDED**:

- **Block Secrets on Push:** Enable the "*Block secrets on push*"
    setting to prevent accidental exposure of secrets in your code.

- **Review and Resolve Flagged Secrets:** Address other secrets
    flagged by Azure DevOps (even if not blocked). E.g. by moving them
    to secure storage like Azure Key Vault.

- **Conducting Dependency Scanning:** Add the Dependency Scanning task
    to your Azure Pipelines to identify vulnerabilities in third-party
    libraries.

- **Code Scanning with CodeQL:** Add the CodeQL scanning task to your
    pipelines to identify security vulnerabilities and code quality
    issues.

- **Microsoft Security DevOps Extension:** Install this to use static
    analysis tools like *ESLint*, *Checkov*, and *Terrascan* to scan for
    vulnerabilities in Azure Pipelines.

!!! tip "Practical tips"
    Security tools may flag valid code (false positives) or miss vulnerabilities (false negatives).

!!! info "Further reading and information"
    [Configure GitHub Advanced Security for Azure DevOps features - Azure Repos \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops&tabs=yaml)

    [Implementing GitHub Advanced Security for Azure DevOps (youtube.com)](https://www.youtube.com/watch?v=Rdlo33QYvXk)
