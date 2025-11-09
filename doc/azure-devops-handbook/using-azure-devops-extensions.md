# Using Azure DevOps extensions

Extensions add extra capabilities but require careful management. Follow
these practices to manage them safely:

- **Evaluate First:** Before requesting an extension, evaluate it
    using Microsoft's criteria as extensions impact all users once
    installed.

- **Request Approval:** Consult the Organisation Owner before
    requesting a new extension.

- **Avoid Dependency:** Do not build critical workflows around
    extensions. They are unsupported and may be removed at any time,
    even if from Microsoft.

- **Cybersecurity Approval:** Obtain approval from Cyber Security for
    extensions accessing code repos or exporting telemetry.

- **Disable telemetry:** Turn off telemetry and intrusive features.

- **Audit Regularly:** Periodically review extensions to ensure
      compliance with privacy and security policies.

!!! tip "Practical tips"
    The Organisation Owner may notify you of new extensions via banner notifications.

!!! info "Further reading and information"
    [Extensions overview - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/extend/overview?toc=%2Fazure%2Fdevops%2Fmarketplace-extensibility%2Ftoc.json&view=azure-devops)

    [Extensions for Visual Studio family of products \| Visual Studio Marketplace](https://marketplace.visualstudio.com/azuredevops)

    [Find or look up the organisation owner - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops)
