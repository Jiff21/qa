Feature: Google your way to documentation

  @browser
  Scenario: The first result for Python behave should contain expected title
    Given I am on "index"
    When I type in "Behave Python"
    Then the results should contain "GitHub - behave/behave: BDD, Python style."

  @browser @chrome-only
  Scenario: There should be no severe console log errors on index page
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors
