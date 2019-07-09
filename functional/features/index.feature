Feature: Tests that should be run on every page

  @browser @minor
  Scenario: SEO Best practices insist you have a title
    Given I am on "index"
    When I look at the about nav
    Then it should have an underline that is "26, 115, 232" color

  @browser  @chrome-only @critical
  Scenario: SEO Best practices insist you have a meta description
    Given I am on "index"
    When I check the console logs
    Then there should be no severe console log errors

  @browser @chrome-only @normal @local-only
  Scenario: SEO Best practices insist you should have open graphs info
    Given I am on "index"
    When I check for og:url
      And I check for og:title
      And I check for og:description
      And I check for og:image

  @browser @chrome-only @normal @local-only
  Scenario: SEO Best practices insist you should have Twitter Card info
    Given I am on "index"
    When I check for og:url
      And I check for twitter:card
      And I check for twitter:site
      And I check for twitter:image

  @validity @minor
  Scenario: SEO Best practices insist you should have a favicon
    Given I am on "index"
    When I look for a favicon

  @browser @minor
  Scenario: SEO Best practices insist you should have a canonical link even if it is to yourself
    Given I am on "index"
    When I look for a canonical link


  @browser @minor
  Scenario: Sites must have <!DOCTYPE html>
    Given I am on "index"
    When I look for a "<!DOCTYPE html>"

  @browser @minor
  Scenario: Sites must have a lang attribute on their html
    Given I am on "index"
    When I look for a "<!DOCTYPE html>"
