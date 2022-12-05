from behave import *
from selenium import webdriver


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()

    

@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_name("username").send_keys(user)
    context.driver.find_element_by_name("password").send_keys(pwd)


    


@when(u'Click on login button')
def step_impl(context):
    


@then(u'User must sucessfully login to the Dashboard page')
def step_impl(context):
    