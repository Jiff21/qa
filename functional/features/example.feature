Feature: Some example tests on Google

  @browser @minor
  Scenario: This is a scenario name
    Given I am on "about"
    When I look at the about nav
    Then it should have an underline that is "26, 115, 232" color

  @browser @chrome-only @normal @local-only
  Scenario: Page should have no console errors if user has slow internet
    Given I am on "index"
    When I throttle network speed to "10.0" MB/s down, "10.0" MB/s up, with "0.0" ms latency
      And I am on "about"
      And I check the console logs
    Then there should be no severe console log errors

  @validity @minor
  Scenario: The page has valid html
    Given I am on "index"
    When I look for html validator messages
    Then it should not have any validation errors

  @browser @minor
  Scenario: The first result for Python behave should contain expected title
    Given I am on "index"
    When I type in "Behave Python"
    Then the results should contain "Welcome to behave!"
