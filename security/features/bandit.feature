Feature: The files we changed should pass bandit scans

  @critical
  Scenario: Bandit finds no vulberabilities in the functional steps
    When I scan "qa/security/features/steps/" with bandit
    Then the bandit scan should not contain any "High" severity issues
      And the bandit scan should not contain any "Medium" severity issues
