Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "about"
    Then the header should be exactly "The latest from our blog"

  @browser
  Scenario: There should be no severe console log errors on index page
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors
