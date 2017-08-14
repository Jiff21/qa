Feature: Example.com should have a head

  @browser
  Scenario: This is a scenario name
    Given I am on "/about"
    Then the header should be exactly "The latest from our blog"
