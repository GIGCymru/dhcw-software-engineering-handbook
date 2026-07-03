# Contributing to the Digital Health and Care Wales (DHCW) Software Engineering Handbook

Thanks for taking the time to improve the handbook.

This repository is a public-facing handbook for DHCW developers and other technical staff. We welcome improvements from DHCW colleagues, partners, and external contributors.

## Before you start

Please read:

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [README](README.md)

If you are unsure whether a change belongs here, open an issue and a maintainer will help.

## What belongs in this repository

This handbook is for practical software engineering guidance that is suitable for open publication.

Please contribute:

- fixes to existing pages
- clearer wording and better examples
- missing guidance that can be shared publicly
- links to useful public references
- accessibility improvements
- typo fixes, formatting fixes, and broken links

Please do not add:

- confidential or internal-only DHCW information
- content that belongs in the private DHCW Cloud Engineering Reference
- credentials, secrets, personal data, or sensitive operational details

For cloud architecture, platform design, and infrastructure delivery guidance, the private DHCW Cloud Engineering Reference is the authoritative source. If a suggestion overlaps with that material, please keep the public handbook high level and public-safe.

## How to contribute

We use GitHub Issues and Pull Requests for changes.

### 1. Open an issue

For most changes, start by opening the issue form in this repository.

There is one issue form:

- **Suggest a change** — use this for ideas, questions, proposed updates, or anything that is not yet ready for a pull request

For very small fixes — a typo, a broken link, or a formatting error — you can skip the issue and go straight to a pull request.

If you're not sure where to start, look for issues labelled [good first issue](https://github.com/GIGCymru/dhcw-software-engineering-handbook/labels/good%20first%20issue).

Use the issue to explain:

- what you want to change
- why the change is needed
- which page or section it affects
- any relevant links or context

### 2. Make your change

Keep changes small and focused where possible.

**If you're a DHCW colleague (GIGCymru org member),** clone the repository directly and create a feature branch:

```
git clone https://github.com/GIGCymru/dhcw-software-engineering-handbook.git

git checkout -b feature/your-change-description
```
If you don't yet have access to the GIGCymru GitHub organisation, contact the Head of Software Engineering to request it.

**If you're an external contributor,** fork the repository on GitHub first, then clone your fork and create a feature branch.

### 3. Check it locally

The handbook repository README explains how to run the site locally.

Please use that local setup to check:

- the site builds successfully
- your page renders as expected
- internal links and anchors still work
- that formatting looks right
- that headings and navigation make sense
- any changed examples are accurate

### 4. Open a pull request

When your change is ready, open a pull request and link the related issue if there is one.

In your pull request description, please include:

- a short summary of the change
- why it is needed
- any screenshots or preview links, if useful
- anything reviewers should know

## Pull request expectations

Please make sure your pull request:

- is easy to review
- only contains the changes needed for that task
- has clear commit messages
- follows the style of the surrounding content
- does not introduce confidential content

Maintainers may ask for changes before merging. This is normal and helps keep the handbook consistent and safe to publish.

## Documentation standards

Please write in plain English.

Aim for content that is:

- clear and practical
- accurate and up to date
- easy to scan
- consistent with the rest of the handbook
- suitable for a public audience

Please prefer:

- short paragraphs
- clear headings
- examples where they help
- links to authoritative sources

Please avoid:

- jargon where simple wording will do
- long, repetitive explanations
- personal opinions presented as policy
- internal process details that are not relevant to readers

## Use of AI tools

We welcome contributions where AI tools have helped with drafting or editing content.

You're responsible for reviewing and validating everything in your pull request. Don't submit AI-generated content without reading and checking it yourself first.

## Accessibility and inclusive language

Please make content accessible to everyone.

That means:

- use descriptive headings and link text
- avoid unnecessary acronyms
- write inclusive, respectful language
- use plain language where possible
- avoid colour-only instructions
- check that examples and images are understandable without extra context

## Maintainers

Maintainers are responsible for:

- reviewing contributions
- keeping the handbook aligned with DHCW standards
- checking that public content is safe to publish
- coordinating updates where changes affect multiple pages

If you are a DHCW colleague and want to propose a broader update, please use the issue form first so maintainers can help shape the change.

## Review process

Maintainers will review pull requests for:

- correctness
- clarity
- consistency
- accessibility
- public-safety and confidentiality

A pull request may be merged once it has the necessary approvals and checks.

## Security issues

For security vulnerabilities, please see [SECURITY.md](SECURITY.md).

## Thank you

Every improvement helps make the handbook clearer and more useful for everyone.
