# Provide a test folder (.*/<rootfoldername\>/*specs*/*test)

As the name suggests, this is where you **SHOULD** store your tests. As
with the *src* folder, you **SHOULD** place test projects in sub
folders, mapping the name of the sub folder to the name of the project.

Names **SHOULD** correspond to those of your dependency layers, with the
*.Tests* suffix added.

When writing the tests, you **SHOULD:-**

- Prioritise output testing over testing that assures modules.

- Adopt Behavioural Driven Development as your approach.

- Balance the benefits and drawbacks of adding extensive testing to
    your solution.

- Consider You Aren't Gonna Need It (YAGNI) rules when deciding what
    to test.

- Consider the testing requirements described in your Definition of
    Done (DOD).

Consider wider assurance needs when deciding what tests to write. Integration and smoke tests often provide the greatest benefit Consider You Aren't Gonna Need It (YAGNI) and carefully balance the time and effort of an extensive testing approach with the benefit it provides

!!! info "Further reading and information"
    [Selective Unit Testing -- Costs and Benefits (stevensanderson.com)](http://blog.stevensanderson.com/2009/11/04/selective-unit-testing-costs-and-benefits/)
