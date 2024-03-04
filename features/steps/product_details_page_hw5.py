from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='styles__ButtonWrapper']")
SELECTED_OPTIONS = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage']")


@given('Open target product {product_id} page')
def open_product_product(context,product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)


@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Deep Olive', 'White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    first_three_colors = colors[:3]
    for color in first_three_colors:
        color.click()
        selected_options = context.wait.until(EC.presence_of_element_located(SELECTED_OPTIONS)).text
        selected_options = selected_options.split('\n')[1]
        actual_colors.append(selected_options)
        print(actual_colors)

    assert actual_colors == expected_colors, f"Expected {expected_colors}, got {actual_colors}"
