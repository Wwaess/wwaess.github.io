For **UNIT 2**
```
Read the Behaviour Driven Development (2020) pages and then use the Gherkin language to create a Gherkin sequence that addresses ONE of the following examples:

Using a new coffee making machine.
Interfacing with a new SatNav system.
Using a computer running the Linux operating system.
Getting familiar with a new vehicle.
Creating a batch or shell script.
Your response should consist of at least three scenarios describing different roles such as administrator, user, driver and so on. Be prepared to share your scenarios at this week's seminar. You can test your Gherkin scripts in the Behave engine.
```

```feature
# -- FILE: features/gherkin-intro.feature
Feature: Using a new SatNav system

    Scenario: The User plans a route
        Given the SatNav is powered on
        And the User has entered a destination
        When the User confirms the route
        Then the SatNav should display the route and estimated travel time on the screen

    Scenario: The Administrator updates the map database
        Given the Administrator has access to the System Settings
        When the Administrator uploads a new map database
        Then the SatNav should confirm a successful installation
        And the SatNav should restart with the new maps

    Scenario: The Driver receives a traffic alert
        Given the Driver is driving along a planned route
        And the SatNav is displaying that route
        When the SatNav receives nearby traffic data
        Then the SatNav should display this info to the Driver
```

Running `behave features/gherkin-intro.feature` outputs the following: 
```

USING RUNNER: behave.runner:Runner
Feature: Using a new SatNav system # features/gherkin-intro.feature:2

    Given the SatNav is powered on                                                   # Noneures/gherkin-intro.feature:4
    And the User has entered a destination                                           # None
    When the User confirms the route                                                 # None
    Then the SatNav should display the route and estimated travel time on the screen # None

  Scenario: The Administrator updates the map database        # features/gherkin-intro.feature:10
    Given the Administrator has access to the System Settings # None
    When the Administrator uploads a new map database         # None
    Then the SatNav should confirm a successful installation  # None
    And the SatNav should restart with the new maps           # None

  Scenario: The Driver receives a traffic alert            # features/gherkin-intro.feature:16
    Given the Driver is driving along a planned route      # None
    And the SatNav is displaying that route                # None
    When the SatNav receives nearby traffic data           # None
    Then the SatNav should display this info to the Driver # None


Errored scenarios:
  features/gherkin-intro.feature:4  The User plans a route
  features/gherkin-intro.feature:10  The Administrator updates the map database
  features/gherkin-intro.feature:16  The Driver receives a traffic alert

0 features passed, 0 failed, 1 error, 0 skipped
0 scenarios passed, 0 failed, 3 error, 0 skipped
0 steps passed, 0 failed, 0 skipped, 12 undefined
Took 0min 0.000s

You can implement step definitions for undefined steps with these snippets:

from behave.api.pending_step import StepNotImplementedError
@given(u'the SatNav is powered on')
def step_impl(context):
    raise StepNotImplementedError(u'Given the SatNav is powered on')


@given(u'the User has entered a destination')
def step_impl(context):
    raise StepNotImplementedError(u'Given the User has entered a destination')


@when(u'the User confirms the route')
def step_impl(context):
    raise StepNotImplementedError(u'When the User confirms the route')


@then(u'the SatNav should display the route and estimated travel time on the screen')
def step_impl(context):
    raise StepNotImplementedError(u'Then the SatNav should display the route and estimated travel time on the screen')


@given(u'the Administrator has access to the System Settings')
def step_impl(context):
    raise StepNotImplementedError(u'Given the Administrator has access to the System Settings')


@when(u'the Administrator uploads a new map database')
def step_impl(context):
    raise StepNotImplementedError(u'When the Administrator uploads a new map database')


@then(u'the SatNav should confirm a successful installation')
def step_impl(context):
    raise StepNotImplementedError(u'Then the SatNav should confirm a successful installation')


@then(u'the SatNav should restart with the new maps')
def step_impl(context):
    raise StepNotImplementedError(u'Then the SatNav should restart with the new maps')


@given(u'the Driver is driving along a planned route')
def step_impl(context):
    raise StepNotImplementedError(u'Given the Driver is driving along a planned route')


@given(u'the SatNav is displaying that route')
def step_impl(context):
    raise StepNotImplementedError(u'Given the SatNav is displaying that route')


@when(u'the SatNav receives nearby traffic data')
def step_impl(context):
    raise StepNotImplementedError(u'When the SatNav receives nearby traffic data')


@then(u'the SatNav should display this info to the Driver')
def step_impl(context):
    raise StepNotImplementedError(u'Then the SatNav should display this info to the Driver')
```