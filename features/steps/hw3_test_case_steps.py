from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[ID*='addToCartButtonOrTextId']").click()
    sleep(6)


@then('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign in')
def click_sign_in_sliding_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@when('Search for product "valentine candy"')
def search_for_product_valentine_candy(context):
    context.driver.find_element(By.ID, 'search').send_keys('valentine candy')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@when('Click on "Add to Cart" button below item')
def click_add_to_cart(context):
    add_to_cart_button = context.driver.find_elements(By.CSS_SELECTOR, "[ID*='addToCartButtonOrTextId']")
    add_to_cart_button[0].click()


@when('Click on "Add to Cart" button on right slide out menu')
def click_add_to_cart_right_slide_out(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()


@when('Click "View cart and check out" button')
def click_view_cart_and_check_out(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__StyledBaseButtonInternal'][href='/cart']").click()


@then('Verify "Your cart is empty" message is shown')
def cart_empty_text(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text, f'Expected "{expected_text} but got a {actual_text}'


@then('Verify Sign in form opened')
def verify_sign_in_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Expected "{expected_text} but got a {actual_text}'


@then('Verify item in cart')
def verify_item_in_cart(context):
    actual_text = context.driver.find_element(By.XPATH, "//p[contains(text(),'1 item')]").text
    expected_text = '1 item'
    assert expected_text in actual_text, f'Expected "{expected_text} but got {actual_text}'
