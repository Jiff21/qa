Feature: Should follow site requirements that only need to be checked once

  @requests
  Scenario: There should be a sitemap.xml file
    Given we get the sitemap
    Then it should include the front end base url
      And it should not contain relative urls

  @requests
  Scenario: Should have correct robots.txt
    When I hit the robots.txt url
    Then it should have a "200" status code
      And it should contain User-agent: *
