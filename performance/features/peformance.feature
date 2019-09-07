Feature: Website meets our performance standards

  @normal
  Scenario: The index page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/"
    Then it should be lower than or equal to "200"

  @normal
  Scenario: The about page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/about"
    Then it should be lower than or equal to "200"

  @normal
  Scenario: The contact page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/contact"
    Then it should be lower than or equal to "200"

  @critical
  Scenario: The index page has less than 3 failures
    Given request results file exists
    When we get "# failures" for the page "/"
    Then it should be lower than or equal to "3"

  @critical
  Scenario: The about page has less than 3 failures
    Given request results file exists
    When we get "# failures" for the page "/about"
    Then it should be lower than or equal to "3"

  @critical
  Scenario: The contact page has less than 3 failures
    Given request results file exists
    When we get "# failures" for the page "/contact"
    Then it should be lower than or equal to "3"

  @minor
  Scenario: The index page should never take longer than 5 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/"
    Then it should be lower than or equal to "500"

  @minor
  Scenario: The about page should never take longer than 5 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/about"
    Then it should be lower than or equal to "500"

  @minor
  Scenario: The contact page should never take longer than 5 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/contact"
    Then it should be lower than or equal to "500"
