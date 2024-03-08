from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign in form opened')
def verify_sign_in_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text, f'Expected "{expected_text} but got a {actual_text}'


