# Always deploy from source control

You **MUST** ensure all deployments originate from source control to
maintain traceability. Use Git tags or branches to track and manage
deployments.

You **MUST NOT** manually copy changes between environments.

!!! tip "Practical tips"
    **WPRS -- Prioritisation incident**

    In 2016, a clinical incident review (ref. 58337) found a missing table alias in a SQL Select statement as the root cause of certain referrals which had been missed for assessment.

    It found that had the code been deployed from source control, the risk of not spotting the error before going live would have reduced.
