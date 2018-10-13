Feature: Our app follows performance recommendations

  @minor
  Scenario: First meaningful paint is less than half a second
    Given we have valid json alert output
    When first meaningful paint section
    Then we should warn if score is below "5000"


  @minor
  Scenario: Time To Interactive under one second
    Given we have valid json alert output
    When we find the Time To Interactive
    Then we should warn if score is below "2000"


  @warn @normal
  Scenario: We should avoid Optimized Images
    Given we have valid json alert output
    When we find the Unoptimized images section
    Then we should warn if score is below "80"


  @warn @normal
  Scenario: We should avoid Render-blocking Stylesheets
    Given we have valid json alert output
    When we find the Render-blocking Stylesheets section
    Then we should warn if score is below "80"


  @warn @minor
  Scenario: We should avoid Render-blocking scripts
    Given we have valid json alert output
    When we find the Render-blocking scripts section
    Then we should warn if score is below "80"
