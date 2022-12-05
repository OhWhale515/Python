from behave import *
from selenium import webdriver

@given(u'launch chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given launch chrome browser')


@when(u'open CodeGreen home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When open CodeGreen home page')


@then(u'verify that the Logo present on page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the Logo present on page')


@then(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')