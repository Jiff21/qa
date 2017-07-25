Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: Take a screenshot of the page
    Given I am on "/behave/parse_builtin_types.html"
      And I start "about" at "600" x "800"
    When I create or compare a screenshot
    Then it should match


  @browser
  Scenario: Take a screenshot of an element
    Given I am on "/behave/api.html#logging-setup"
      And I start "logging_element" at "1200" x "1200"
    When I find the logging setup section
      And I create or compare a screenshot of an element
    Then it should match
