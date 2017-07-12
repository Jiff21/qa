Feature: Pen test the Application

  Scenario: The application should have X-Content-Type-Options set on all requests

    Given we have valid json alert output
    When the alert is on the correct base url
    Then we should not have X-Content-Type-Options alerts
