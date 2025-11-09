# Provide a scripts folder (.*/<rootfoldername\>/*build/scripts)

You **SHOULD** store any scripts needed to assist with the build[^1], by
placing them in a '*scripts'* subfolder. This offers a standard location
for any others wishing to build your solution.

As well as build scripts, use the folder to store artefacts related to
your continuous integration (CI) processes. While some CI systems
require you place build artefacts in the root, placing other supporting
files in the scripts folder avoids excessive cluttering.

When storing scripts, you **SHOULD** keep your scripts clean and with
comments.

You **SHOULD** prefer using scripted solutions over build events
whenever possible.

You **SHOULD NOT** break published conventions without considering how
this impacts others.

!!! example "Examples of good practice"
    > {IMAGE PLACEHOLDER}
    Figure 3 An example.NET Solution with a build and scripts folder

!!! info "Further reading and information"
    [.NET Core Opinion #4 - Increase Productivity with Dev Scripts (odetocod e.com)](https://odetocode.com/blogs/scott/archive/2018/09/21/net-core-opinion-4-ndash-increase-productivity-with-dev.aspx)

    [.NET Core Opinion #5 - Deployment Scripts and Templates (odet ocode.com)](https://odetocode.com/blogs/scott/archive/2018/10/17/net-core-opinion-5-deployment-scripts-and-templates.aspx)

[^1]: .*exe, .ps1 .sql* and .*cmd* files for example.
