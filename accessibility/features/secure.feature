Feature: Our app is secure

  Scenario: Redirects http traffic to https

    Given we have valid json alert output
    When we find the Redirects HTTP traffic to HTTPS section
    Then it should be "True"
