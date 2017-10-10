Feature: Website meets our performance standards

  Scenario: The index page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/"
    Then it should be lower than or equal to "200"

  Scenario: The about page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/about"
    Then it should be lower than or equal to "200"

  Scenario: The contact page has an average response under 2 seconds
    Given request results file exists
    When we get "Average response time" for the page "/contact"
    Then it should be lower than or equal to "200"

  Scenario: The index page has an average response under 2 seconds
    Given request results file exists
    When we get "# failures" for the page "/"
    Then it should be lower than or equal to "2"

  Scenario: The about page has an average response under 2 seconds
    Given request results file exists
    When we get "# failures" for the page "/about"
    Then it should be lower than or equal to "2"

  Scenario: The contact page has an average response under 2 seconds
    Given request results file exists
    When we get "# failures" for the page "/contact"
    Then it should be lower than or equal to "2"

  Scenario: The index page should never take longer than 15 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/"
    Then it should be lower than or equal to "1500"

  Scenario: The about page should never take longer than 15 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/about"
    Then it should be lower than or equal to "1500"

  Scenario: The contact page should never take longer than 15 seconds to respond
    Given request results file exists
    When we get "Max response time" for the page "/contact"
    Then it should be lower than or equal to "1500"
