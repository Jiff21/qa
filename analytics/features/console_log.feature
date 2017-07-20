Feature: Home Page has correct GA Tags

  Scenario: The Homepage fires an event when it loads
    When I check logs
    Then I should see "title" with a value of "Our Products | Google"
