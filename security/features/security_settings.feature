Feature: Follows security requirements

  @browser
  Scenario: The site should upgrade insecure requests
    Given I try to go to http version of "index"
    When I get the browser url
    Then it should contain https

  Scenario: Homepage includes X-Content-Type-Options no-sniff header
    Given I call the api "index"
    When I find the "X-Content-Type-Options" header
    Then it should have the X-Content-Type-Options set to no-sniff

   Scenario: Homepage includes X-Frame-Options SAMEORIGIN header
    Given I call the api "index"
    When I find the "X-Frame-Options" header
    Then it should have the X-Frame-Options set to SAMEORIGIN

   Scenario: Homepage has X-XSS-Protection on
    Given I call the api "index"
    When I find the "X-XSS-Protection" header
    Then it should have the X-XSS-Protection set to 1

  Scenario: Homepage has an appropriate Content Security Policy
    Given I call the api "index"
    When I find the "Content-Security-Policy" header
    Then the CSP should contain "script-src 'self'"
      And the CSP should contain "unsafe-inline"
      And the CSP should contain "unsafe-eval"
      And the CSP should contain "*.google-analytics.com"
      And the CSP should contain "*.youtube.com"
      And the CSP should contain "*.googletagmanager.com"
      And the CSP should contain "*.gstatic.com"
      And the CSP should contain "*.googleapis.com"
      And the CSP should contain "*.doubleclick.net"
      And the CSP should contain "report-uri"

  @browser
  Scenario: Site uses secure cookie
    Given I am on "index"
    When I get all cookies
    Then the ones from our domain should be secure

  Scenario: Does not allow javascript execution as part of the url
    When I add "javascript:alert('Look ma!')" to the URL
    Then the response is a "404"
    And I add "javas[0x0a][0x0d]cript:alert('Look ma!')" to the URL
    Then the response is a "404"
    And I add "javascript://www.example.com/?foo=%0a%0dalert('Look ma!')" to the URL
    Then the response is a "404"

  Scenario: Does not allow vbscript injection as part of the url
    When I add "vbscript:MsgBox("Look ma!")" to the URL
    Then the response is a "404"

  Scenario: Does not allow data injection as part of the url
    When I add "data:text/html,<script>alert('Look ma!')</script>" to the URL
    Then the response is a "404"
