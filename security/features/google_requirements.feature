Feature: Complies with Google Sites Security Requirements


  Scenario: Only uses Secure Cookies
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Cookie No HttpOnly Flag" errors


  Scenario: Has XXS Protection Enabled
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Web Browser XSS Protection Not Enabled" errors


  Scenario: Has Content Type set to No Sniff
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "X-Content-Type-Options Header Missing" errors


  Scenario: Has X-Frame set to same origin
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "X-Frame-Options Header Not Set" errors


  Scenario: Does not disclose sensitive information in errors
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Application Error Disclosure" errors


  Scenario: Does not allow reflected cross site scripting
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Cross Site Scripting (Reflected)" errors

  Scenario: Does not allow reflected cross site scripting
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Cross Site Scripting (Persistent)" errors


  Scenario: Does not allow reflected cross site scripting
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Secure Pages Include Mixed Content" errors


  Scenario: Does not allow SQL Injection
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "SQL Injection" errors
