# SQL prompt configuration

## SQL prompt settings file

### How to import the settings

1. Download the *`NWIS_STANDARD_SQLPROMPT_SETTINGS`* file to a local
    directory.

> You can find the file from the *Software Development Standards* git
> repo under the *Software Development Standards* project on Application
> Development & Support's Azure DevOps instance.

1. Open SQL Server Management Studio with Redgate SQL Prompt v9 or
    later installed and choose ***SQL Prompt > Options.***

> Select ***Import*** to load the
> *`NWIS_STANDARD_SQLPROMPT_SETTINGS.settings`* file.

### The settings file explained

| **Suggestions** |  |
| --- | --- |
| Behaviour | Uses default settings |
| Connections | Uses default settings with the following exceptions: Unchecks the ***Load suggestions for linked servers*** & ***Load suggestions for synonyms*** options. Note: This is done to improve performance. Specifying the databases to  load may further improve performance, but this will vary between teams. |
| Join Conditions | Unchecks ***Columns with matching names (not case-sensitive)***. Checks ***Individual columns in multiple-column foreign keys*** |
| Snippets | Uses default settings |
| Warnings & highlighting | Checks all options other than '*Show warnings for DROP statements*' |

| **Inserted Code** |  |
| --- | --- |
| Objects and statements | Uses default settings |
| Qualification | Checks all options |
| Aliases | Checks **Assign aliases**. Note: Custom aliases should be used to provide consistency across an application, but these cannot be defined here. |
| Special characters | Uses default settings |

| **Format** |  |
| --- | --- |
| Styles | For formatting styles see [SQL Prompt formatting style file](#sql-prompt-formatting-style-file). In addition to default settings checks. ***Expand wildcards***, ***Qualify object names***, ***Insert semicolons***, ***Apply column alias style***, ***Column AS alias***, ***Add/remove square brackets***, ***Remove unnecessary brackets***, ***Add/remove AS keyword on alias definition for tables and views***, ***Add AS keyword*** |

| **Tabs** |  |
| --- | --- |
| History | Sets ***Maximum number of tabs to restore:*** to **5**. Unchecks ***Automatically reconnect restored tabs*** |
| Color | Uses default settings. Note: Colour can be used to differentiate environments. However, separate credentials (e.g. `NatTd`, `GIGNWI`) should be used to connect to development and production environments; these accounts can support their own SQL Prompt settings. |

## SQL prompt formatting style file

### How to import the style

1. Download the *`NWIS_STANDARD_SQLPROMPT_SETTINGS`* file to a local
    directory.

> You can find the file from the *Software Development Standards* git
> repo under the *Software Development Standards* project on Application
> Development & Support's Azure DevOps instance.

1. You have a choice of two versions. If using SQL Prompt v10.5 or
    later, choose the newer *`.json`* file extension. If using an earlier
    version, choose the *`.sqlpromptstylev2`* file type.

1. With the correct style file selected, save it to "*`<Insert Drive Letter>:\Users\<Insert Test-Dev-NADEX-ID>\AppData\Local\Red Gate\SQL Prompt <Version>\StylesV2`" or *
    "`<Insert Drive Letter>:\Users\<Insert Test-Dev-NADEX-ID>\AppData\Local\Red Gate\SQL Prompt <Version>\Styles`*[^1]

1. Open SQL Server Management Studio with Redgate SQL Prompt v9 or
    later installed.

1. From the menu choose ***SQL Prompt > Active Styles > Edit Formatting Styles***

1. Under ***Your styles*** (top right), select the vertical ellipsis
    next to ***NWIS_Custom style indented, commas before*** and choose
    ***Set as active.***

### The style file explained

Uses Redgate's ***Indented defaults*** as its base style with the
following customisations applied: -

| **GLOBAL** |  |
| --- | --- |
| Whitespace | ***Wrapping***: Sets ***Wrap lines longer than*** to **160 characters** |
| Lists | ***Commas***: Checks ***Place commas before items***. Sets ***Comma alignment*** to **Before item**. Checks ***Add a space after comma*** |
| Casing | Sets ***Global variables*** to **UPPERCASE** |

| **EXPRESSIONS** |  |
| --- | --- |
| CASE | Unchecks ***Place expressions on new line***. ***WHEN***: Sets ***Place first WHEN on new line*** to **If there's an input expression**; Sets ***WHEN alignment*** to **Indented from CASE**. **THEN expressions**: Unchecks ***Place THEN on new line***. **ELSE**: Checks ***Place ELSE on new line***; Checks ***Align ELSE to WHEN***. **END**: Checks ***Place END on new line***; Sets ***End alignment*** to *To CASE*. **Short CASE expressions**: Unchecks ***Collapse CASE expressions shorter than n characters*** |

### Notes & explanation

Commas before: -

- clearly define a new column.

- help identify when a comma is missing.

- make it easier to comment out additional fields during development.

Indentation aids readability. However, long expressions may appear
distorted when wrapped. See the section [Exceptions prove the
rule](exceptions-prove-the-rule.md).

[^1]: E.g. `D:\\Users\\NatTD_ge080206\\*AppData\\Local\\Red Gate\\SQL Prompt 9\\StylesV2*`
