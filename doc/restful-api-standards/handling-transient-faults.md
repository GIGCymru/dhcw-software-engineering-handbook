# Handling transient faults

APIs **MUST** be designed to handle transient faults caused by temporary
network issues, timeouts, or service disruptions. Clients **SHOULD**
implement retry strategies to maintain reliability without overwhelming
the system.

## Identifying transient faults

The API **MUST** clearly define transient faults and distinguish them
from permanent failures.

The API **MUST** specify which [HTTP status
codes](http-implementation.md) indicate transient faults that are
safe to retry:

- 5xx errors (e.g. 500 Internal Server Error) indicate server-side
    faults.

- Some 4xx errors **MAY** also be transient and safe to retry, such as:

  - 429 Too Many Requests (after respecting Retry-After).

  - 408 Request Timeout, if caused by temporary network issues.

  - 409 Conflict, if due to a temporary resource state.

## Retry strategies

Clients **MUST** ensure retries do not introduce unintended side
effects. APIs **MUST** be *idempotent* where possible.

If an API returns Retry-After, clients **MUST** wait before retrying.

Clients **SHOULD** use *exponential backoff* with *jitter* to avoid
spikes in retry traffic.

The API **SHOULD** document:

- The *maximum number of retry attempts* before a failure is
    considered permanent.

- *Recommended wait times* between retries.

- *Rate limits* to avoid excessive retries.

Additional **RECOMMENDATIONS**:

- APIs **SHOULD** use *circuit breakers* to prevent repeated calls
    when a service remains unavailable.

- Clients **SHOULD** *randomise retries* to prevent simultaneous retry bursts.

- If the API is deployed on Apigee, it **MUST** integrate with
    Apigee's transient fault handling features.
