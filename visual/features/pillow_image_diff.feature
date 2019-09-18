Feature: Testing the index page with a pillow visual diff at various sizes

  @browser @medium @pillow
  Scenario: No unexpected visual changes on the index page on mobile
    Given I am on "index"
      And I start "index page Mobile" at "375" x "812"
    When I create or compare a screenshot
    Then it should match

  @browser @medium @pillow
  Scenario: No unexpected visual changes on the index page on mobile
    Given I am on "index"
      And I start "index page Tablet" at "600" x "1024"
    When I create or compare a screenshot
    Then it should match

  @browser @medium @pillow
  Scenario: No unexpected visual changes on the index page on Desktop
    Given I am on "index"
      And I start "index page Desktop" at "1250" x "1024"
    When I create or compare a screenshot
    Then it should match
