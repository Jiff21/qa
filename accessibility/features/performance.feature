Feature: Our app performs well

  Scenario: The application can load over a flaky connection

    Given we have valid json alert output
    When we find the flaky connection section
    Then it should have an overall score above "80"
