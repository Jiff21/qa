Feature: Site follows Lighthouse performance recommendations


  @minor
  Scenario Outline: <page> Page first meaningful paint is less than half a second
    Given we load lighthouse results file "<page>"."<format>"
    When first meaningful paint section
    Then we should warn if score is below "5000"

    Examples: Passing Tests
      | page               | format |
      | index              |  html  |
      | about              |  json  |
      | products page      |  json  |


  @minor
  Scenario Outline: <page> page time To Interactive is under one second
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Time To Interactive
    Then we should warn if score is below "2000"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @warn @normal
  Scenario Outline: <page> page should avoid Unoptimized Images
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Unoptimized images section
    Then we should warn if score is below "80"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @warn @normal
  Scenario Outline: <page> page should avoid Render-blocking Resources
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Render-blocking Resources section
    Then we should warn if score is below "80"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @normal
  Scenario Outline: <page> page should avoid using a large amount of resources
    Given we load lighthouse results file "<page>"."<format>"
    When we find the total weight section
    Then we check to see make sure its under 1504 kb

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

#TODO: Number of resource but might need page speed api.
