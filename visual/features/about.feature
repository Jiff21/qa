Feature: The about page's style doesn't accidentally change

  @browser
  Scenario:
    Given I am on "/behave/parse_builtin_types.html"
      And I start "Home to other pages test" of "example.com" at "tablet"
    When the "Data Types Page" should look as expected
      And I type in "Dogs"
      And click Go
    Then I see the no results header
      and the "No Results Page" should look as expected
      and we close eyes
