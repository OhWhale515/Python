from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def launchBrowser(context):
    raise NotImplementedError(u'STEP: Given launch chrome browser')


@when(u'open CodeGreen home page')
def openHomepage(context):
    raise NotImplementedError(u'STEP: When open CodeGreen home page')


@then(u'verify that the Logo present on page')
def verifyLogo(context):
    raise NotImplementedError(u'STEP: Then verify that the Logo present on page')


@then(u'close browser')
def closeBrowser(context):
    raise NotImplementedError(u'STEP: Then close browser')