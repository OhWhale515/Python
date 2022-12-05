from behave import *
from selenium import webdriver


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()

    

@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "admin" and password "admin123"')
def step_impl(context,admin,admin123):
    context.driver.find_element_by_id("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(admin)
    context.driver.find_element_by_id("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys(admin123)


    


@when(u'Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()

    


@then(u'User must sucessfully login to the Dashboard page')
def step_impl(context):
    text=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text()
    assert text=="Dashboard"
    context.driver.close()
    