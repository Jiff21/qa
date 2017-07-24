Feature: The about page's style doesn't accidentally change

  @browser
  Scenario:
    Given I am on "/behave/parse_builtin_types.html"
      And I start "about" at "600" x "800"
    When I create or compare a screenshot
    Then it should match
