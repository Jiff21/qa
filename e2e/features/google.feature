Feature: Google your way to documentation

  @browser
  Scenario: Google
    Given I am on "https://google.com"
    When I type in "Behave Python"
    Then the results should contain "Welcome to behave!"
