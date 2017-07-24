Feature: The about page's style doesn't accidentally change

  @browser
  Scenario:
    Given I am on "/behave/parse_builtin_types.html"
      And I start "about" at "600" x "800"
    When the "Data Types Page" should look as expected
      And I type in "Dogs"
      And click Go
    Then I see the no results header
      and the "No Results Page" should look as expected
      and we close eyes
