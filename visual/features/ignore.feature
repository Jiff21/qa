Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: Ignore header link and target body
    Given I am on "/behave/"
      And I start "Home to other pages test" of "python hosted" at "tablet"
    When only the body of the "home page body" should look as expected
      And I am on "/behave/api.html"
    Then the "API Page" should look as expected, without the headerlink
      And I ignore the "Region Selector" by dimensions
      and we close eyes
