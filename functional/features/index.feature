Feature: Tests that should be run on every page

  @requests @major
  Scenario: SEO Best practices insist you should have Facebook open graph data
    Given I get "index" with requests session
    Then it should have an og:title
      And the content attribute should not be empty
      And it should have an og:description
      And the content attribute should not be empty
      And it should have an og:image
      And the content attribute should not be empty
      And it should have an og:url
      And the content attribute should not be empty

  @requests @major
  Scenario: SEO Best practices insist you should have Twitter Card data
    Given I get "index" with requests session
    Then it should have a twitter:card meta tag
      And the content attribute should not be empty
      And it should have a twitter:site meta tag
      And the content attribute should not be empty
      And it should have a twitter:image meta tag
      And the content attribute should not be empty
      And it should have a twitter:title meta tag
      And the content attribute should not be empty
      And it should have a twitter:description meta tag
      And the content attribute should not be empty

  @requests @major
  Scenario: SEO Best practices insist you have 2 types of favicons
    Given I get "index" with requests session
    When I get all rel icon links
    Then at least one should contain rel="icon" and be .png format
      And at least one should contain rel="shortcut icon" and be .ico format


## canonical link check in lighthouse
## <!DOCTYPE html> in lighthouse
## Lang test in lighthouse
