from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
   #context.driver=webdriver.Chrome(executable_path="C:\Users\sterl\Downloads\chromedriver_win32\chromedriver.exe")
   context.driver=webdriver.Chrome() 


@when(u'open OrangeHRM home page')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    


@then(u'verify that the Logo present on page')
def verifyLogo(context):
    status=context.driver.find_element_by_css_selector("div.orangehrm-login-layout div.orangehrm-login-layout-blob div.orangehrm-login-container div.orangehrm-login-slot-wrapper div.orangehrm-login-branding > img:nth-child(1)").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
    