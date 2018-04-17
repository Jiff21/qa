Feature: Example.com should have a head

  @browser @minor
  Scenario: This is a scenario name
    Given I am on "about"
    Then the header should be exactly "The latest from our blog"

  @browser  @chrome-only @critical
  Scenario: There should be no severe console log errors on index page
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors

  @browser @chrome-only @wip @skip @KEY-666 @normal
  Scenario: Page should have no console errors if user has slow internet
    Given I am on "index"
    When I throttle network speed to "10.0" MB/s down, "10.0" MB/s up, with "0.0" ms latency
      And I click the start test button
    Then there should be no severe console log errors

  @validity @skip @KEY-GoogleFails
  Scenario: The page has valid html
    Given I am on "index"
    When I look for html validator messages
    Then it should not have any validation errors
