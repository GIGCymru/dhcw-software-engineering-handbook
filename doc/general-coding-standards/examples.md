# Examples

## Unnecessary using statements

!!! danger "Examples of practices to avoid"
    ```csharp
        namespace Example
        {
            using System;
            using System.Collections.Generic;

            internal class BadClass
            {
                static void Main(string[] args)
                {
                    Console.WriteLine(“I'm using statements unnecessarily!”);
                    Console.WriteLine(“I'm bad, shamone!”);
                }
            }
        }
    ```

| **Rule ID** | **Rule Title** |
| --- | --- |
| [IDE0005](https://learn.microsoft.com/en-gb/dotnet/fundamentals/code-analysis/style-rules/ide0005) | Using directive is unnecessary. |

## Use our namespace conventions

!!! example "Examples of good practice"
    `NhsWales.Wcp.Portal`

!!! danger "Examples of practices to avoid"
    `DHCW.Wis.Reports`

## Consider your use of var

!!! example "Examples of good practice"
    ```csharp
        var patient = new Patient();

        Patient myPatient = new Patient();
    ```

!!! danger "Examples of practices to avoid"
    `#!csharp var patientCount = Ward.getPatientCount();`

!!! example "Examples of good practice"
    `#!csharp int patientCount = Ward.getPatientCount();`

!!! danger "Examples of practices to avoid"
    `#!csharp var myPatient = Demographics.getPerson(NHSNumber);`

!!! example "Examples of good practice"
    `#!csharp Person myPatient = Demographics.getPerson(NHSNumber);`

## Name parameters

!!! example "Examples of good practice"
    `#!csharp var permissions = getUsersAccessPermissions("ge000001", isLoggedIn: true);`

!!! danger "Examples of practices to avoid"
    `#!csharp var permissions = getUsersAccessPermissions("ge000001", true);`

!!! tip "Practical tips"
    Enable Visual Studio's inline parameter hints to show argument names before function call arguments

## Prioritise readability over brevity

!!! danger "Examples of practices to avoid"
    `#!csharp SearchOnUserName(string id);`
    `#!csharp SearchOnUsersFullName(string nadexID);`

!!! example "Examples of good practice"
    `#!csharp SearchOnUsersFullName(string activeDirectoryUserId);`

## Use underscores only in unit test names

!!! example "Examples of good practice"
    `#!csharp SearchOnUsersFullName_ValidActiveDirectoryUserIdProvided\_ReturnsUsersFullName()`

!!! danger "Examples of practices to avoid"
    `#!csharp Search_On_UsersFullName(string activeDirectoryUserId);`

## Ensure boolean names are phrased as questions

!!! example "Examples of good practice"
    `#!csharp bool IsTrue;`

!!! danger "Examples of practices to avoid"
    `#!csharp bool conditionChecker;`

!!! example "Examples of good practice"
    `#!csharp bool IsOpen;`

!!! danger "Examples of practices to avoid"
    `#!csharp bool open;`

!!! example "Examples of good practice"
    `#!csharp bool IsActive;`

!!! danger "Examples of practices to avoid"
    `#!csharp bool status;`

## Use prefixes and suffixes only when specified by conventions

!!! danger "Examples of practices to avoid"
    ```csharp
        string strActiveDirectoryUserId;

        int iPatientCount;

        var iPatientCount;

        GetUsersFullName(string p_activeDirectoryUserId);
    ```

!!! example "Examples of good practice"
    | **Prefix** | **Usage** | **Language** |
    |--- | --- | --- |
    | **I** | **Interface** definitions | *C#* |
    | **T** | Generic **Type** definitions. Simply use T if only one Type is defined. | *C#* |
    | **T** | Type definitions | *Delphi* |
    | **P** | **Pointers** to *Type* definitions | *Delphi* |
    | **A** | Use to distinguish parameters with the same name as private member variables. | *Delphi* |

## Using braces

!!! danger "Examples of practices to avoid"
    ```csharp
        if (isLoggedIn)
            DisplayHomePage();

        if (isLoggedIn) DisplayHomePage();
    ```
    
!!! example "Examples of good practice"
    ```csharp
        if (isLoggedIn)
        {
            DisplayHomePage();
        }

        if (isLoggedIn) { DisplayHomePage(); }
    ```

| **Rule ID** | **Rule Title** |
| --- | --- |
| [IDE0011](https://learn.microsoft.com/en-gb/dotnet/fundamentals/code-analysis/style-rules/ide0011) | Add braces to 'if' statement. |

## Code comments

> {IMAGE PLACEHOLDER}
