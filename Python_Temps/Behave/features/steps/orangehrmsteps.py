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
    status=context.driver.find_element_by_src("/web/images/ohrm_branding.png?1666596668857" alt="company-branding").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
    