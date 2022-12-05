from behave import *
from selenium import webdriver


@given(u'I launch Chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I launch Chrome browser')


@when(u'I open orange HRM Homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open orange HRM Homepage')


@when(u'Enter username "admin" and password "admin123"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter username "admin" and password "admin123"')


@when(u'Click on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on login button')


@then(u'User must sucessfully login to the Dashboard page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must sucessfully login to the Dashboard page')