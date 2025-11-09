# How do you test for lost updates

Rick and Liz call for a review into the application's safety. This leads
to a software change to prevent lost updates. How would you test it?

In a web app, you might mimic each user by opening a new browser tab.
Using Google Chrome's incognito mode for example. Or you might run the
application on two machines. How robust would these tests be?

And what if the *users* were software threads rather than people.
Triggered to send almost simultaneous database updates? You would need a
different test.

Use this guide to test such scenarios. It is a response to
recommendations found in a 2018 report.

!!! tip "Practical tips"
    **Welsh Admin Portal -- Root Cause Analysis**

    An investigation into why some patients were not assigned to waiting lists in the Welsh Patient Administration System concluded that;

    'The design and implementation did not account for (or handle) the potential for concurrency conflicts...Routine testing did not identify the issue'

!!! info "Further reading and information"
    RPT-231026APRIL18 -WAP Redirect RCA.docx
