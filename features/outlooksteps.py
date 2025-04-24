import time
from behave import *
from playwright.sync_api import sync_playwright
playwright_start = sync_playwright().start()
browser = playwright_start.chromium.launch(headless=False)
tab = browser.new_context(viewport={'width': 1890, 'height': 920})
page = tab.new_page()

application_url = 'https://www.microsoft.com/en-us/microsoft-365/outlook/log-in'

Locators = {
    "signin_button": "( //span[text()='Sign in'])[3]",
    "input_mail": "//input[@id='i0116']",
    "mail_next_button": " //button[@id='idSIButton9']",
    "input_password": "//input[@type='password']",
    "final_signin_button": "//input[@id='idSIButton9']",
    "home": " //span[@id='id__13']"
}

def wait_for_pageLoad(locator,max_time):
    start_time = (int(round(time.time() * 1000))) // 1000
    while True:
        if page.locator(locator).is_visible():
            break
        running_time= (int(round(time.time() * 1000))) // 1000
        if running_time-start_time > max_time:
            raise Exception(f"Page took more than {max_time} seconds to load without showing next object")
        time.sleep(1)

@given('User open Outlook Application')
def step_impl(context):
    page.goto(application_url)
    page.wait_for_pageLoad("(//div[@id='primaryArea'])[3]",60)

@when('User click on Sign in button')
def step_impl(context):
    page.locator(Locators["signin_button"]).click()
    page.wait_for_pageLoad(" (//div[@data-testid='banner'])", 30)

@then('User should able to give email and login')
def step_impl(context):
    page.locator(Locators["input_mail"]).fill("tejaswini.gundala@external.atlascopco.com")
    page.locator(Locators["mail_next_button"]).click()
    page.wait_for_pageLoad(Locators["input_password"], 10)
    page.locator(Locators["input_password"]).fill("Atlas@2025")
    page.locator(Locators["signin_button"]).click()
    page.wait_for_pageLoad(Locators["home"], 30)
    try:
        if Locators["home"].is_visible():
            print("True")
    except:
        page.wait_for_pageLoad(Locators["home"], 30)




