Feature: The site follows Lighthouse SEO best practices


  @critical
  Scenario Outline: <page> page has a meta description tag
    Given we load lighthouse results file "<page>"."<format>"
    When we find the meta description section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @critical
  Scenario Outline: <page> page has a meta description tag
    Given we load lighthouse results file "<page>"."<format>"
    When we find the title tag section
    Then it should be "True"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |


  @critical
  Scenario Outline: <page> page should not use meta refresh
    Given we load lighthouse results file "<page>"."<format>"
    When we find the meta-refresh section
    Then it should be "False"

    Examples: Passing Tests
      | page               | format |
      | index              |  json  |
      | about              |  json  |
