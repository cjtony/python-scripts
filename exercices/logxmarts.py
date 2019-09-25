from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/Users/marco/Documents/geckodriver')

browser.maximize_window()
browser.get('https://xmarts.com/web/login')
email = browser.find_element_by_name('login')
email.send_keys('marco.carranza@xmarts.com')
passw = browser.find_element_by_name('password')
passw.send_keys('123456')
#browser.find_element_by_class_name('btn-block').click()
browser.implicitly_wait(10)

val_email = email.get_attribute('value')
print(str(val_email))
val_passw = passw.get_attribute('value')
print(str(val_passw))