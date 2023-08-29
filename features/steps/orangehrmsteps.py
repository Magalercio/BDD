from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verifyLogo(context):
    context.driver.implicitly_wait(2)
    status = context.driver.find_element(By.XPATH, '//body/div[@id="app"]/div[1]/div[1]/div[2]').is_displayed()
    assert status is True


@then('Close browser')
def closeBrowser(context):
    context.driver.close()
