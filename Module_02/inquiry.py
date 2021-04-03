"""Fill student form."""
from selenium.webdriver.support.select import Select
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(5)
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to_frame(driver.find_element_by_class_name('fs_embeded'))

first_name = driver.find_element_by_id('u_vY6_4607')
first_name.clear()
first_name.send_keys('Jesus')

last_name = driver.find_element_by_id('u_vY6_338354')
last_name.clear()
last_name.send_keys('Serna')

email = driver.find_element_by_id('u_vY6_4608')
email.clear()
email.send_keys('jj.sernav@hotmail.com')

inquiry = driver.find_element_by_id('u_vY6_4609')
inquiry.clear()
inquiry.send_keys('This is just a test')



continue_btn = driver.find_element_by_name('submit')
continue_btn.click()

driver.quit()