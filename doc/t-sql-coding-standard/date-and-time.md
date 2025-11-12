# Date and time

You **SHOULD**: -

- Use a suitable date / time datatype. Their precision differs and
    affects the performance of your queries accordingly.

- Express dates in ISO format to remove ambiguity. For example,
    12/04/2017 may be interpreted as 12th April or 4th December
    depending on your configuration.

!!! example "Examples of good practice"
    Use year, month day yyyymmdd format for a date alone (e.g., 20171204)

    Use year, month, day and time format yyyy-MM-ddThh:mm:ss.xxx for a date & time (e.g. 2017-12-04T14:24:30.123)

- Cast `DATETIME` or `SMALLDATETIME` fields to `DATE` if
    you're interested only in the date part. SQL Server supports this.

You **SHOULD NOT**:-

- Use `DATEDIFF` when searching date ranges. As with other functions,
    this prevents the database engine making use of any indexes.

- Use `BETWEEN` for searching datetime ranges. The start and end of the
    range can appear ambiguous. Use the operators \>*,* <*,* \>=*,*
    <=*,* = instead.

- Use the *+* or *--* operators on date/time fields; It is unclear
    what unit is being applied. For example, it's not clear that
    `GETDATE()+1` will return this time tomorrow. Newer datatypes such as
    `DATE`, `DATETIME2` and `DATETIMEOFFSET` throw errors when used in this
    way.

!!! info "Further reading and information"
    [How to Get SQL Server Dates and Times Horribly Wrong - Simple Talk (red-gate.com)](https://www.red-gate.com/simple-talk/databases/sql-server/t-sql-programming-sql-server/how-to-get-sql-server-dates-and-times-horribly-wrong/)
