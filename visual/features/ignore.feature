Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: Ignore the body
    Given I am on "/behave/"
      And I start "Home to other pages test" of "python hosted" at "tablet"
      And I force fullscreen mode
    When the "home page" should look as expected, without the body
      And I am on "/behave/api.html"
    Then the "API Page" should look as expected, without the body
      and we close eyes
