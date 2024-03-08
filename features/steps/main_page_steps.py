from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[ID*='addToCartButtonOrTextId']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")


@given('Open Target main page')
def open_target_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys({product})
    # context.driver.find_element(*SEARCH_ICON).click()
    # sleep(6)
    context.app.header.search_product()
    sleep(6)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()
    # context.driver.find_element(*CART_ICON).click()
    # sleep(6)


@then('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign in')
def click_sign_in_sliding_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify header is shown')
def verify_header_is_shown(context):
    header = context.driver.find_element(*HEADER)
    print(header)


@then("Verify header has {expected_amount} links")
def verify_header_has_5_links(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == 5, f'Expected {expected_amount} links, but got {len(header_links)}'