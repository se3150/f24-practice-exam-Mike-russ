from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    global driver
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

def teardown_driver():
    global driver
    if driver:
        driver.quit()
        driver = None

@given('I open the url "https://byjus.com/herons-calculator/"')
def step_impl(context):
    setup_driver()
    driver.get('https://byjus.com/herons-calculator/')
    time.sleep(2)  # wait for page to load

@when('I enter valid credentials')
def step_impl(context):
    a = driver.find_element(By.ID, "a")
    b = driver.find_element(By.ID, "b")
    c = driver.find_element(By.ID, "c")
    submit_button = driver.find_element(By.CLASS_NAME, "clcbtn")

    #enter information
    a.send_keys("3")
    b.send_keys("5")
    c.send_keys("7")
    submit_button.click()
    time.sleep(2)


@then("I should get valid results")
def step_impl(context):
    assert driver.find_element(By.ID, "_d") == 6.495