Feature: Pen test the Application

  Scenario: The application should not contain Cross Domain Scripting vulnerabilities

    Given we have valid json alert output
    Then We should not have X-Content-Type-Options alerts
