Feature: Google your way to documentation

  @browser
  Scenario: The first result for Python behave should contain expected title
    Given I am on "index"
    When I type in "Behave Python"
    Then the results should contain "Welcome to behave!"
