Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name 
    Given I am on "https://example.com"
    Then the header should be exactly "Example Domain"
