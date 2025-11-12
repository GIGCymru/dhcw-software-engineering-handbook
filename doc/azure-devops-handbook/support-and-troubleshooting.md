# Support and troubleshooting

Azure DevOps requires minimal support, but issues can still arise.
Follow these steps to get help:

## General support

- **Check Service Notifications**: For updates about issues or
    disruptions.

- **Check Microsoft Service Status**: Visit [Azure DevOps - Status](https://status.dev.azure.com/) for service updates.

- **Monitor the Developer Channel**: Check the [Visual Studio Developer Azure DevOps Channel](https://developercommunity.visualstudio.com/AzureDevOps) to
    upvote relevant issues.

- **Ask a Project Admin**: Contact your Project Administrator if you
    need further help.

- **Contact the Organisation Owner**: For help with unresolved issues,
    speak to the Organisation Owner who can raise a support request with
    Microsoft.

- **Log a Service Request:** If the Organisation Owner is unavailable
    or your query is urgent, raise a service request (addressed to the
    *Corporate Application* team). This option is only available to
    users of the *NHS-Wales-Digital* Organisation.

!!! info "Further reading and information"
    [Find or lookup the organisation owner - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops)

    [Look up a project collection administrator - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-project-collection-administrators?view=azure-devops)

## Unable to clone large Git repos

Raise a service request to join the *NWI_Zscaler_Allow_AzureDevops Entra group*
If you need to clone large repos. On approval, choose *Update Policy* in your
zscaler desktop application.

In the meantime, work around the issue using these commands:

```sh
    mkdir *<Repo Name>*

    cd *<Repo Name>*

    git init

    git remote add origin *<Your repo URL>*

    git pull # results in curl 56 failure.

    git pull # succeeds.
```

## Fixing issues with SSL certificates

Errors may occur if Git isn't configured to use the Windows Certificate
Store for SSL verification:

fatal: unable to access 'https://<your-repo-url\>': SSL certificate
problem: unable to get local issuer certificate

fatal: unable to access 'https://<your-repo-url\>': schannel
CertGetCertificateChain trust error CERT_TRUST_IS_PARTIAL_CHAIN

To fix them, run the following command in Git Bash. Alternatively, if
you're using Visual Studio set the *cryptographic network provider* to
*schannel* in the Git settings:

`git config --global http.sslBackend schannel`
