from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm login homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.TAG_NAME, "button").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//header/div[1]/div[1]/span[1]/h6[1]").text
    context.driver.close()
    assert text == "Dashboard"
