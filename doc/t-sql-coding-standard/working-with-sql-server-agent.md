# Working with SQL server agent

You **SHOULD**:-

- Define job steps that call stored procedures.

- Make sure jobs exist across all your high-availability SQL instances
    (e.g., both side of the mirror, availability group nodes.)

- Add an initial step to jobs on mirrors to allow the job to stop with
    a warning rather than error.

- Make use of the job categories

- Use job categories or the description field to track temporarily
    disabled and retired jobs.

You **SHOULD NOT** define job steps with ad-hoc SQL; It hides
application logic, and you are unable to manage it using SQL Source
Control.
