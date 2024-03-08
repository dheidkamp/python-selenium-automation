Feature: Target.com search tests

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown
    Then Page URL has search term coffee

#  # Make sure Scenario names are unique:
#  Scenario: User can search for a mug on target
#    Given Open Target main page
#    When Search for mug
#    Then Search results for mug are shown
#    Then Page URL has search term mug
#
#  Scenario Outline: User can search for a product on target
#    Given Open Target main page
#    When Search for <search_word>
#    Then Search results for <expected_result> are shown
#    Then Page URL has search term <expected_part_url>
#    Examples:
#    |search_word   |expected_result   |expected_part_url    |
#    |coffee mug    |coffee mug        |coffee+mug           |
#    |coffee        |coffee            |coffee               |
#    |tea           |tea               |tea                  |
