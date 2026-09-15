# Report content and structure

## Cover page

The report's cover page **MUST** contain the following elements: -

### Heading #1: "*digital health and care wales*"

### Heading #2: name and version of the system under test

You **SHOULD** include: -

- The acronym (in parentheses) if you intend to use it in the report.

- The version number, if applicable, prefixed with a 'v' for version
    or 'b' for build number.

### Heading #3: name of module or component

Where appropriate you **SHOULD** include the name of the module or
component.

### Heading #4: "test summary report"

### Heading #5: test phase

You **SHOULD** choose an appropriate value from those listed on pages 26
-- 30 of the Test Framework.

### Heading #6: status

This reflects the status of the document and **MUST** be 'Draft',
'Draft-Update' or 'Issued'.

!!! example "Examples of good practice"
    Welsh Immunisation System (WIS) v4.3.0.0

    Spring Boosters Campaign

    Test Summary Report

    Systems Integration Testing

    Draft

    6th March 2024

### Footer: filename

The Template's footer was inserted as Quick Parts -\> Fields -\>
FileName. When you save the first copy of the report, right-click the
footer and choose 'Update Field' to update the [filename](finishing-your-report.md#filename).

## Table of contents

You **MUST** include a Table of Contents.

## Document location

Document Location **MUST** be a hyperlink to the original document.

## Relevant documents

You **SHOULD** include links to the Test Strategy, Test Plan and
Solutions Architecture Design document. And reference the Assurance
Quality Plan and Safety Case and Readiness Report where they exist. You
**SHOULD NOT** embed documents.

!!! tip "Practical tips"
    Use external links cautiously as they may become outdated or broken over time.

## Version control

You **SHOULD** include the present version and any predecessor versions
with brief accompanying notes describing changes and reasons for the
change.

Revision History statuses **SHOULD** be limited to *Draft, Draft-Update*
or *Issued.*

## Reviews and approvals

Recording reviewers and approvers using electronic signatures is
**RECOMMENDED**, but you **MAY** instead record the name and date of the
reviewer and approver. See also [Roles & Responsibilities](introduction.md#roles-responsibilities).

## Summary of testing

The Testing summary **MUST** contain the following headings: -

| **RECOMMENDATION:** | Your recommendation based on the findings. Written in bold font. |
| --- | --- |
| **Observations and Variances:** | Any noteworthy findings, deviations from expected results, and any observed variations. It is essential to capture anything left untested together with an associated reason, for example, limitations on availability of test devices. |
| **Background:** | A brief overview of the application, the features and components under test and any relevant context. |
| **Approach:** | The testing strategy employed, including automation, manual testing, or any specific methodologies. |
| **Entry Criteria:** | Entry criteria are the specific conditions that must be met before testing can begin. Including these criteria is useful, especially if you need to explain any exceptions when proceeding. |
| **Test Phase:** | Specify the phase of testing covered in this report. Be guided by 'Test Phases' in the 'Test Framework' (pages 26 - 30). |
| **Test Types:** | Enumerate the distinct types of testing conducted. Be guided by 'Appendix 4' of the 'Test Framework' (pages 52 - 56) but you **MAY** include others. |
| **Test Environment:** | The technical setup and configurations used for testing. |
| **Dates:** | Specify the duration of the testing period and key milestones. |
| **Test Tools:** | The tools used for testing purposes. |
| **In-Scope:** | The features, components and interfaces considered during testing. |
| **Out-of-scope:** | What was explicitly excluded from the testing scope. |
| **Exit criteria:** | The predetermined conditions that must be met for testing to be considered complete and successful. |

## Test metrics

The Testing summary **SHOULD** contain the following headings :-

| **Execution Metrics:** | A snapshot of the test script execution, including pass, fail, completion status, and any deferred or not applicable scripts. |
| --- | --- |
| **Defect Metrics:** | Summarises the initial defects, total raised, closed, and currently open defects, categorised by severity. |
| **Open Defects:** | Describes the currently open defects, with their Azure DevOps ID and severity. |

## Further metrics

You **MAY** include additional metrics from sources like Extent Reports
or Azure DevOps dashboards to provide a more comprehensive perspective
on the testing process.
