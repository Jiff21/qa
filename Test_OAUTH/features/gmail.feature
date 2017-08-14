Feature: Login test

  @browser
  Scenario: Check Mail
    Given I am on "/"
      And I click Mail
      And I click Sign In
    When I log into google using as "Admin"
      And I wait for the page to load
    Then I am on inbox page