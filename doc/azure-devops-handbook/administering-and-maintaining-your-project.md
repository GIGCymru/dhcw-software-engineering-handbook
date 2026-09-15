# Administering and maintaining your project

## Managing user settings

Update your profile and interface preferences via the User settings icon
in the top right corner. You can also access preview features to stay up
to date.

!!! tip "Practical tips"
    Set your time zone to ***(UTC+00:00) Dublin, Edinburgh, Lisbon, London*** in *User Settings > Time and Locale* to ensure consistency.

## Using wikis

You **MAY** use Azure DevOps Wikis to record project information and
decisions, but you **MUST NOT** use them for information that should be
stored in a controlled document.

!!! info "Further reading and information"
    [Create a project wiki to share information - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/project/wiki/wiki-create-repo?view=azure-devops&tabs=browser)

    [Share knowledge within teams - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/share-knowledge-within-teams/)

## Creating and managing dashboards

Use dashboards to monitor key metrics like test results, build quality,
code coverage and burn-down rates. The following layout is
**RECOMMENDED**:

- **Top row:** Display build metrics for quick visibility of build
    status.

- **Middle row:** Show test results and code quality metrics to track
    code health.

- **Bottom row**: Reserve for sprint and team performance metrics.

> {IMAGE PLACEHOLDER}

!!! info "Further reading and information"
    [Understand dashboards, charts, reports, and widgets - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/report/dashboards/overview?view=azure-devops)

## Project housekeeping tasks

Follow these **RECOMMENDED** practices to keep projects clean and
well-organised:

- **Set artifact retention policies** Keep only the **latest**,
    **previous** and **active** releases versions to minimise storage
    costs.

- **Pipeline run retention:** Retain only recent, relevant runs for
    debugging. Set retention policies to delete pipeline runs after
    **30 days**.

- **Delete obsolete branches**. Remove inactive or redundant branches
    to remove clutter.

- **Clean agent pools**: Clean stale directories and repositories on
    self-hosted agents **weekly** to avoid disk space issues.

- **Keep agents updated**: Enable automatic updates for minor version
    changes and manually upgrade for major updates.

## Managing costs

To control and optimise costs Organisation Owners **SHOULD:**

- **Monitor Azure DevOps costs**: Review consumption costs against
    your Azure subscription **weekly** to spot unexpected charges early.

- **Downgrade or remove inactive users**: Downgrade inactive users to
    Stakeholder after **8 weeks.** Remove users who haven't used Azure
    DevOps for **6 months.**

- **Set a monthly cost threshold:** Set alerts for when costs exceed a
    threshold and review cost breakdowns in the \"*Cost Management +
    Billing*\" section of the Azure portal.

!!! info "Further reading and information"
    [Manage paid access for users - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/billing/buy-basic-access-add-users?view=azure-devops)

    [Billing FAQs (Frequently Asked Questions) - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/billing/billing-faq?view=azure-devops)

## Data privacy and availability

Azure DevOps Services includes strong data protection, availability and
features:

- **Data Availability:** Continuous access through data redundancy,
    even during failures.

- **Service Availability:** High uptime with built-in availability
    mechanisms.

- **Service Security**: Protection against threats and
    vulnerabilities.

- **Data Privacy:** Compliance with privacy laws and best practices

!!! info "Further reading and information"
    [Data protection overview - Azure DevOps Services \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/data-protection?view=azure-devops)

!!! tip "Practical tips"
    YOU **MUST NOT** store Personal Identifiable information (PII) in Azure DevOps!

## Connecting Defender for Cloud DevOps

Connecting Azure DevOps to Microsoft Defender for Cloud helps identify
and fix security issues. Check with your Organisation Owner and Cyber
Security team about potential costs first.

The following practices are **RECOMMENDED**:

- **Connect to Defender for Cloud**: Organisation Owners **MAY** link
      Azure DevOps to Defender for Cloud for security insights. This
      will also install the *Defender for DevOps Container Mapping*
      extension to protect containerized applications.

- **Enable Pull Request Annotations**: Turn on annotations to
      highlight security issues in pull requests, so they can be fixed
      before merging.

- **Review Alerts and Recommendations**: Regularly review Defender for
    Cloud alerts and follow recommendations to reduce risks.

!!! info "Further reading and information"
    [Microsoft Defender for Cloud DevOps Security Benefits \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/defender-for-cloud/defender-for-devops-introduction)

    [Connect Azure DevOps to Defender for Cloud \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/defender-for-cloud/quickstart-onboard-devops)

    [Configure the Security DevOps Extension \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/defender-for-cloud/azure-devops-extension)

    [Microsoft Security DevOps Extension for Azure DevOps \| GitHub](https://github.com/microsoft/security-devops-azdevops?tab=readme-ov-file)

    [Enable Pull Request Annotations \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/defender-for-cloud/enable-pull-request-annotations)
