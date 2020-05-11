Feature: Index Page meets our performance standards

  @normal
  Scenario: The index page has an average response under 2 seconds
    Given request results file exists
    When we get "Average Response Time" for the page "index"
    Then it should be lower than or equal to "200"

  @critical
  Scenario: The index page has less than 3 failures
    Given request results file exists
    When we get "Failure Count" for the page "index"
    Then it should be lower than or equal to "2"

  @minor
  Scenario: The index page should never take longer than 5 seconds to respond
    Given request results file exists
    When we get "Max Response Time" for the page "index"
    Then it should be lower than or equal to "500"
