
Feature: Google's product page should have correct GA Tags

  Scenario: The Homepage fires an event when it loads
  Given I am on "/about/products/"
    When I check logs
    Then I should see "title" with a value of "Our Products | Google"

  Scenario: When I click a Products Learn More it should fire correct events
    Given I am on "/about/products/"
    When I click Youtube's Get Started button
      And I click Youtube's Learn more
      And I check logs
    Then I should see "eventLabel" with a value of "Learn more"
      And I should see "eventCategory" with a value of "products"
      And I should see "eventAction" with a value of "watch, listen, and play: youtube"
