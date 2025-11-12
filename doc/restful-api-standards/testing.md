# Testing

This section provides help for creating your API Test strategy and
plans.

## Shift left

Test early in the API lifecycle and continue testing at every stage.
This 'shift left' approach challenges you to develop T-shaped skills.
For testers, this may involve writing code for automated tests. For
developers, it means recognising that testing is a shared
responsibility.

!!! info "Further reading and information"
    [What is Shifting Left Testing? \| Shift Left Meaning in Software Testing](https://smartbear.com/learn/automated-testing/shifting-left-in-testing/)

## Automate as much as you can

Test automation is crucial for shifting left and you **SHOULD** execute
tests as part of your CI/CD pipelines. This practice helps identify and
fix issues as they are introduced.

!!! tip "Practical tips"
    Consider automating tests for stories with frequent execution, critical functionality, stable requirements and variable data.

## Validate the OpenAPI specification

Check the [OpenAPI specification](open-api-specification.md) for structure
and format to ensure the contract is correct. Use the *out-of-the-box*
rules provided by linting tools like *Spectral* or *Postman Linter* to
verify proper JSON and YAML formatting.

It is **RECOMMENDED** you write a custom ruleset to enforce the rules
described in this document.

You **SHOULD** Inspect the API contract for the following, adding these
checks to your CI/CD pipeline.

- Endpoints are named correctly.

- Resources and their types are accurate.

- Relationships between resources are properly defined.

- No functionality is missing or duplicated.

!!! info "Further reading and information"
    [API linting with Spectral \| What is it and how does it work?](https://blog.axway.com/learning-center/apis/api-design/api-linting-with-spectral#:~:text=Spectral%20allows%20automating%20some%20of,APIs%20follow%20the%20given%20rules.)

## Unit tests

Write unit tests as you build your API to catch issues early. Start with
minimal tests and expand as necessary -- do not overcomplicate matters.

You **SHOULD** add these tests to your CI/CD pipeline and publish code
coverage metrics in a [Test Summary report](testing.md).

## Functional tests

Functional tests **SHOULD** verify that:

- The correct HTTP headers and [HTTP status
    codes](http-implementation.md) are returned.

- The media type and its payload are correct, with appropriate field
    names, types and values.

- Endpoints behave according to the specified business logic and
    requirements.

### Test for failure

Functional testing **SHOULD** include negative tests and check for valid
error responses. These **SHOULD** cover scenarios for handling transient
faults.

### Behaviour driven development (bdd)

Automate validation by incorporating BDD executable scenarios into your
functional tests. For example:

!!! example "Examples of good practice"
    Scenario: Verify Successful Patient Retrieval

    Given the API endpoint for retrieving patient data

    When a GET request is made with a valid patient ID

    Then the API should return a 200 OK status code

    And the response should include correct patient information

## Security tests

Plan security testing with the API platform and cyber security teams.
While many tests are executed against the proxy, you **SHOULD** also
test the backend API for common vulnerabilities.

Refer to the [Security](security-headers.md) section when planning your
tests. Examples of common security tests include:

- Input validation tests to prevent SQL injection attacks.

- Verifying that only authorised users can access patient data.

- Data encryption checks to confirm that data is transmitted over
    HTTPS.

- Rate limiting tests to detect and mitigate potential brute-force
    attacks.

## Performance tests

You **MUST** check the [maximum response
time](performance-and-response-times.md).

You **SHOULD** consider whether to conduct, baseline, load, stress, soak
and scalability tests.

!!! tip "Practical tips"
    Keep in mind that setting up the right environment can be challenging and that repeating tests consistently may be difficult due to network variations.

## Usability tests

You **SHOULD** test the entire API consumer journey including
documentation, authentication and code examples, to ensure usability for
users without prior knowledge of our systems.

## Keep tests organised

Tests **MUST** be organised and named according to our coding standards.

!!! info "Further reading and information"
    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

    [General Coding Standards](../general-coding-standards/introduction.md)

## Test summary report

You **SHOULD** write a Test Summary report for every major, minor or
patch version of your API. The content **MAY** vary depending on the
version but you **SHOULD** consider including each of the following
headings.

!!! note
    1. Static Analysis results (e.g. Spectral tests)

    2. Code Metrics (e.g. code coverage based on results from automated tests)

    3. Functional Tests

    4. Security Tests (including references to any external pen test reports)

    5. Performance Tests

    6. Usability Tests

!!! tip "Practical tips"
    Some headings **MAY** be marked as "N/A" if not applicable for the version tested.

!!! info "Further reading and information"
    [How to write a Test Summary Report](../test-summary-report/introduction.md)

    SDS-TEM-5 Test Summary Report Template

## Test environment

You **SHOULD** deploy APIs to a sandbox environment to allow client
testing. Contact the platform team for further assistance.
