Feature: About Page meets our performance standards

  @normal
  Scenario: The About page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "about"
    Then it should be lower than or equal to "200"

  @critical
  Scenario: The About page has less than 3 failures
    Given request results file exists
    When we get "# failures" for the page "about"
    Then it should be lower than or equal to "2"

  @minor
  Scenario: The About page should never take longer than 5 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "about"
    Then it should be lower than or equal to "500"
