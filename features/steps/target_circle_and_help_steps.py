from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOX_LINKS = (By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
HELP_PAGE_UI_LINKS = (By.CSS_SELECTOR, "")

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")


@given('Open Target Help page')
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")


@then('Verify {expected_number_boxes} boxes are present')
def verify_boxes_present(context, expected_number_boxes):
    expected_number_boxes = int(expected_number_boxes)
    benefit_box_links = context.driver.find_elements(*BENEFIT_BOX_LINKS)
    assert len(benefit_box_links) == 5, f'expected {expected_number_boxes} but got {len(benefit_box_links)}'


@then('Verify {expected_num_elements} UI elements are present')
def verify_elements_present(context,expected_num_elements):
    expected_elements = int(expected_num_elements)
    help_page_ui_links = context.driver.find_elements(*HELP_PAGE_UI_LINKS)
    assert len(help_page_ui_links) == expected_elements, f'expected {expected_num_elements} but got {len()}'