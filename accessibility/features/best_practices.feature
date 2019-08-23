Feature: The Site follows Lighthouse best practices


  @blocker
  Scenario Outline: <page> page redirects http traffic to https
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Redirects HTTP traffic to HTTPS section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

    @skip @KEY-1929
    Examples: example of something that's failing.
      | page                 | format |
      | products page        |  json  |


  @blocker
  Scenario Outline: <page> page should not contain vulnerable javascript
    Given we load lighthouse results file "<page>"."<format>"
    When wwe find the vulnerable libraries section
    Then it should have a score value of "1"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @warn @trivial
  Scenario Outline: <page> page should support theme-color nav bars if we have time
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Has a themed-omnibox tag
    Then we should warn if its not "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @warn @trivial
  Scenario Outline: <page> page should be mobile friendly
    Given we load lighthouse results file "<page>"."<format>"
    When we find the content is sized correctly for the viewport
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @trivial
  Scenario Outline: <page> page contains some content when JavaScript is not available
    Given we load lighthouse results file "<page>"."<format>"
    When we find the Content with JavaScript disabled section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @critical
  Scenario Outline: <page> page does not use document write
    Given we load lighthouse results file "<page>"."<format>"
    When we find the avoids document write section
    Then it should have a score value of "0"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @trivial
  Scenario Outline: Target _blank links on <page> page use rel='noopener'
    Given we load lighthouse results file "<page>"."<format>"
    When we find the noopener section
    Then it should have a score value of "0"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

  @critical
  Scenario Outline: <page> page includes canonical references
    Given we load lighthouse results file "<page>"."<format>"
    When we find the canonical reference section
    Then it should have a score value of "1"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |

  @minor
  Scenario Outline: <page> page content should not be larger than the viewport
    Given we load lighthouse results file "<page>"."<format>"
    When we find the content-width section
    Then it should have a score value of "1"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |
