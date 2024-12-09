from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('I open the url "https://byjus.com/herons-calculator/"')
def step_impl(context):
    context.behave_driver.get("https://byjus.com/herons-calculator/")
    time.sleep(2)  # Wait for page to load

@when('I enter valid credentials')
def step_impl(context):
    a = context.behave_driver.find_element(By.ID, "a")
    b = context.behave_driver.find_element(By.ID, "b")
    c = context.behave_driver.find_element(By.ID, "c")
    submit_button = context.behave_driver.find_element(By.CLASS_NAME, "clcbtn")

    # Enter values
    a.send_keys("3")
    b.send_keys("5")
    c.send_keys("7")
    submit_button.click()
    time.sleep(2)  # Wait for results to load

@then("I should get valid results")
def step_impl(context):
    result = context.behave_driver.find_element(By.ID, "_d").text
    assert result == "6.495"
