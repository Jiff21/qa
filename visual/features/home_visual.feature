Feature: The homepage does not unexpected visual changes

  @minor @wip
  Scenario Outline: Homepage works matches galen specs on <size> <browser>
    Given we find the json for "homepage" on "<browser>" for "<size>"
      And it's valid json
      And we get sections portion of the json
      And and get the "Main Section" section
    When we loop get a list of objects
      And we loop get a list of specs
      And we make a list of errors
    Then they should not have errors

  @chrome-only
  Examples: Homepage works matches galen specs in Chrome
  | browser        | size            |
  | chrome         | mobile          |
  | chrome         | tablet          |
  | chrome         | desktop         |

  @firefox-only
  Examples: Homepage works matches galen specs in Firefox
  | browser        | size            |
  | firefox        | mobile          |
  | firefox        | tablet          |
  | firefox        | desktop         |

  @minor @wip
  Scenario Outline: Footer and Header match galen specs on <size> <browser>
    Given we find the json for "homepage" on "<browser>" for "<size>"
      And it's valid json
      And we get sections portion of the json
      And and get the "Navigation" section
    When we loop get a list of objects
      And we loop get a list of specs
      And we make a list of errors
    Then they should not have errors

  @chrome-only
  Examples: Homepage works matches galen specs in Chrome
  | browser        | size            |
  | chrome         | mobile          |
  | chrome         | tablet          |
  | chrome         | desktop         |

  @firefox-only
  Examples: Homepage works matches galen specs in Firefox
  | browser        | size            |
  | firefox        | mobile          |
  | firefox        | tablet          |
  | firefox        | desktop         |
