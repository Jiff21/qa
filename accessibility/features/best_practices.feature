Feature: Our site follows best practices

  Scenario: Redirects http traffic to https
    Given we have valid json alert output
    When we find the Redirects HTTP traffic to HTTPS section
    Then it should be "True"

  @stdout-all
  Scenario: If we have time we should support theme-color nav bars
    Given we have valid json alert output
    When we find the Has a <meta name="theme-color"> tag
    Then we should warn if its not "True"

  Scenario: Should be mobile friendly
    Given we have valid json alert output
    When we find the Content is sized correctly for the viewport
    Then it should be "True"

  Scenario: Contains some content when JavaScript is not available
    Given we have valid json alert output
    When we find the Content with JavaScript disabled section
    Then it should be "True"

  Scenario: Does not use document write
    Given we have valid json alert output
    When we find the avoids document write section
    Then it should be "True"

  Scenario: Target _blank links use rel='noopener'
    Given we have valid json alert output
    When we find the noopener section
    Then it should be "True"
