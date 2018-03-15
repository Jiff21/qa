Feature: Complies with Recommendations

  @blocker
  Scenario: Does not allow parameter tampering in the url
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Parameter Tampering" errors

  @blocker
  Scenario: Does not allow Session ID in URL Rewrite
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Session ID in URL Rewrite" errors

  @critical
  Scenario: Does not allow HTTP Parameter Override
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "HTTP Parameter Override" errors

  @critical
  Scenario: Does not have Loosely Scoped Cookie
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Loosely Scoped Cookie" errors

  @normal
  Scenario: Does not allow Absence of Anti-CSRF Tokens
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Absence of Anti-CSRF Tokens" errors

  @blocker
  Scenario: Does not have Debug Error Messages
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Information Disclosure - Debug Error Messages" errors
