from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_NAV_PREV_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")


@when('Click "View cart and check out" button')
def click_view_cart_and_check_out(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__StyledBaseButtonInternal'][href='/cart']").click()


@when('Click on Add to Cart button for product {i}')
def click_add_to_cart_by_index(context, i):
    # Find all Add to cart buttons, click on a button by index:
    # product 1 -> index 0
    # product 2 -> index 1, etc.
    context.driver.find_elements(*ADD_TO_CART_BTN)[int(i)-1].click()


@when('Store product name')
def store_product_name(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Store product name to a list')
def store_product_names(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    current_product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    try:  # try to add a product to context.product_names:
        context.product_names.append(current_product_name)
    except AttributeError:  # if context.product_names not set, set it and put the current_product_name itno it:
        context.product_names = [current_product_name]


@when('Click on "Add to Cart" button below item')
def click_add_to_cart(context):
    add_to_cart_button = context.driver.find_elements(By.CSS_SELECTOR, "[ID*='addToCartButtonOrTextId']")
    add_to_cart_button[0].click()


@when('Click on "Add to Cart" button on right slide out menu')
def click_add_to_cart_right_slide_out(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()


@then('Page URL has search term {expected_part_url}')
def verify_search_page_url(context, expected_part_url):
    # url = context.driver.current_url
    # assert expected_part_url in url, f'Expected {expected_part_url} but got {url}'
    context.app.search_results_page.verify_search_page_url(expected_part_url)


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'
    # print('Test case passed')

    context.app.search_results_page.verify_search_results_correct(expected_result)