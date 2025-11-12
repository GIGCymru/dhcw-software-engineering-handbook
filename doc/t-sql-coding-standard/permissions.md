# Permissions

You ****SHOULD**:-

- Define database roles for the specific type of database access
    required.

- Grant database object permissions *only* to database roles.

- Grant database access to Active Directory groups and service
    accounts via membership of database roles.

- Record information about the accounts you create and the permissions
    you assign them in each environment.

You **SHOULD NOT**:-

- Instinctively grant database owner (dbo) permissions.

- Use SQL Server logins, unless working with a 3rd party application
    that specifically requires their use.

- Grant database access to individual user accounts.
