Feature: Complies with Recommendations

  Scenario: Does not allow parameter tampering in the url
    Given we have valid json alert output
      and the alert is on the correct base url
    Then we should not have any "Parameter Tampering" errors
