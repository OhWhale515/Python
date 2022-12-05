from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def launchBrowser(context):
   context.driver = webdriver.Chrome(executable_path="C:\Users\sterl\Downloads\chromedriver_win32\chromedriver.exe")
    


@when(u'open CodeGreen home page')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    


@then(u'verify that the Logo present on page')
def verifyLogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
    