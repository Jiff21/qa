Feature: Our app follows Lighthouse accessibility best practices


  @trivial
  Scenario: Element aria-* attributes are allowed for this role
    Given we load lighthouse results file "index"."json"
    When we find the aria-* attributes section
    Then it should be "True"


  @normal
  Scenario: Background and foreground colors have a sufficient contrast ratio
    Given we load lighthouse results file "index"."json"
    When we find the contrast ratio section
    Then it should be "True"


  @minor
  Scenario: Every image element has an alt attribute
    Given we load lighthouse results file "index"."json"
    When we find the image-alt section
    Then it should be "True"


  @minor
  Scenario: Every form element has a label
    Given we load lighthouse results file "index"."json"
    When we find the form label section
    Then it should be "True"
