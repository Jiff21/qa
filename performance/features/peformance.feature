Feature: Website meets our performance standards

  Scenario: The index page has an average response under 50
    Given request results file exists
    When we get "Average response time" for the page "/"
    Then it should be lower than or equal to "50"
