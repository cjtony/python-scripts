from selenium import webdriver
import unittest
# browser = webdriver.Firefox(executable_path='C:/Users/marco/Documents/geckodriver')
# browser.maximize_window()
# browser.get('https://facebook.com')
# email = browser.find_element_by_name('email')
# password = browser.find_element_by_name('pass')
# email.send_keys('marcocaaguilar@gmail.com')

browser = webdriver.Firefox(executable_path='C:/Users/marco/Documents/geckodriver')
browser.maximize_window()
browser.get('https://python.org')
assert "Python" in browser.title