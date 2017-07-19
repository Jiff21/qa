Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: I go to the about page on a tablet it should look as expected
    Given I start eyes at "tablet"
      And I am on "/"
    When the "Home Page" should look as expected
      And I click the sf office image
      And locate the header
    Then the "Contact Page" should look as expected
        and we close eyes
