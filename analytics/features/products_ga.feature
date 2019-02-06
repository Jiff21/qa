@trivial
Feature: Google's About page should have correct analytics events

  Scenario: The About page fires an event when it loads
    Given I am on "about"
    When I check logs
    Then I should see "title" with a value of "About | Google"

  Scenario: The Career Link in the footer fires correct UA events
    Given I am on "about"
    When I click the Careers link in the footer
      And I close new tab
      And I check logs
    Then I should see "eventCategory" with a value of "Footer"
      And I should see "eventAction" with a value of "more about us"
      And I should see "eventLabel" with a value of "https://careers.google.com/"
