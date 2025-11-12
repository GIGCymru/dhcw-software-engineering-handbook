# Secrets and certificate management

You **SHOULD NOT** store secrets in clear-text storage.

Secrets and API keys **MUST** be stored and encrypted in a secrets
manager. Where secrets are injected from a secrets manager into a CI-CD
pipeline, they **MUST NOT** be logged.
