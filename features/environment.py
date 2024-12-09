from behave_webdriver import Chrome

def before_all(context):
    # Use Chrome in headless mode for CI environments
    context.behave_driver = Chrome(headless=True)

def after_all(context):
    context.behave_driver.quit()
