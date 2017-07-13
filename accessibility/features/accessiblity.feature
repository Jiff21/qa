Feature: Our app follows accessibility best practices

  Scenario: Element aria-* attributes are allowed for this role

    Given we have valid json alert output
    When we find the aria-* attributes section
    Then aria should have be True

  Scenario: Background and foreground colors have a sufficient contrast ratio

    Given we have valid json alert output
    When we find the contrast ratio section
    Then contrast ratio should be True
