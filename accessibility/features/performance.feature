Feature: Our app performs well

  Scenario: First meaningful paint is less than half a second
    Given we have valid json alert output
    When first meaningful paint section
    Then it should have an overall score under "5000.0"

  Scenario: Time To Interactive under one second
    Given we have valid json alert output
    When we find the Time To Interactive
    Then it should have an overall score under "2000.0"

  Scenario: We should avoid Optimized Images
    Given we have valid json alert output
    When we find the Unoptimized images section
    Then we should warn if its not "True"

  Scenario: We should avoid Render-blocking Stylesheets
    Given we have valid json alert output
    When we find the Render-blocking Stylesheets section
    Then we should warn if its not "True"

  Scenario: We should avoid Render-blocking scripts
    Given we have valid json alert output
    When we find the Render-blocking scripts section
    Then we should warn if its not "True"
