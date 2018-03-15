Feature: The homepage does not unexpected visual changes

  @minor @wip
  Scenario Outline: Homepage works matches galen specs
    Given we find the json for "homepage" on "<browser>" for "<size>"
      And it's valid json
      And we get the relevant json
    When we loop get a list of objects
      And we loop get a list of specs
      And we make a list of errors
    Then they should not have errors

  Examples: Browsers and sizes
  | browser        | size            |
  | chrome         | mobile          |
  | chrome         | tablet          |
  | chrome         | desktop         |
  | firefox        | mobile          |
  | firefox        | tablet          |
  | firefox        | desktop         |
