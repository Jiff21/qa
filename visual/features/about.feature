Feature: The about page's style doesn't accidentally change

  @browser
  Scenario: I go to the about page on a tablet it should look as expected
    Given I start eyes at "tablet"
    When I type in "hello world!"
      and click a certain button
    Then it should look a certain way with the message "Click!"
        and we close eyes
