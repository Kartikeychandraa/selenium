from selenium import webdriver
from selenium import * 

browser = webdriver.Firefox()
browser.get("https://github.com/login")
browser.maximize_window() 
#harvesting

user=browser.find_element_by_xpath("//input[@id ='login_field']") 
user.send_keys("your username")

password = browser.find_element_by_xpath("//input[@id ='password']") 
password.send_keys("your Password")ss

browser.find_element_by_xpath("//a[. = 'Sign in']").click()
browser.find_element_by_class_name('btn btn-primary btn-block').click()

