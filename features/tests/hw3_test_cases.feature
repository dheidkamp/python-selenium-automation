# Created by dheid at 2/6/2024

Feature: Target.com search and sign in tests

  Scenario: Verify "Your cart is empty is shown"
    Given Open Target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown


  Scenario: Verify that logged out user can access Sign in:
    Given Open Target main page
    Then Click Sign in
    When From right side navigation menu, click Sign in
    Then Verify Sign in form opened
#
  Scenario: Verify cart has accurate cart items
    Given Open Target main page
    When Search for product "valentine candy"
    When  Click on "Add to Cart" button below item
    When Click on "Add to Cart" button on right slide out menu
    When Click "View cart and check out" button
    Then Verify item in cart
