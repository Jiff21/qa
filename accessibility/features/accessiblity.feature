Feature: Our app follows accessibility best practices

  @trivial
  Scenario: Element aria-* attributes are allowed for this role
    Given we have valid json alert output
    When we find the aria-* attributes section
    Then it should be "True"

  @normal
  Scenario: Background and foreground colors have a sufficient contrast ratio
    Given we have valid json alert output
    When we find the contrast ratio section
    Then it should be "True"

  @minor
  Scenario: Every image element has an alt attribute
    Given we have valid json alert output
    When we find the image-alt section
    Then it should be "True"

  @minor
  Scenario: Every form element has a label
    Given we have valid json alert output
    When we find the form label section
    Then it should be "True"
