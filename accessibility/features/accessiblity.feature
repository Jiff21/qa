Feature: The site follows Lighthouse accessibility best practices


  @trivial
  Scenario Outline: <page> page has aria-* attributes on its elements
    Given we load lighthouse results file "<page>"."<format>"
    When we find the aria-* attributes section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

    @skip @KEY-1929
    Examples: example of something that's failing and we need to skip the test until its fixed
      | page                 | format |
      | products page        |  json  |


  @normal
  Scenario Outline: <page> page background and foreground colors have a sufficient contrast ratio
    Given we load lighthouse results file "<page>"."<format>"
    When we find the contrast ratio section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @minor
  Scenario Outline: <page> page every image element has an alt attribute
    Given we load lighthouse results file "<page>"."<format>"
    When we find the image-alt section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @minor
  Scenario Outline: <page> page every form element has a label
    Given we load lighthouse results file "<page>"."<format>"
    When we find the form label section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @major
  Scenario Outline: <page> page does not have duplicate-ids
    Given we load lighthouse results file "<page>"."<format>"
    When we find the duplicate-id label section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

  @major
  Scenario Outline: <page> page does has <lang=\"XX\">
    Given we load lighthouse results file "<page>"."<format>"
    When we find the html-has-lang section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @major @wip
  Scenario Outline: <page> page allows zooming
    Given we load lighthouse results file "<page>"."<format>"
    When we find the meta-viewport section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |
