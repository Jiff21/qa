Feature: Google your way to documentation

  Scenario: Google
    Given I am on google.com
    When  I type in "Behave Python"
      and I hit return
    Then  The results should contain "Behave"
