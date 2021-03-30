"""Second Selenium Example"""

from selenium import webdriver

driver_path = '/Users/jjserna/Documents/Repository/2021_python_selenium/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://saucelabs.com/resources/articles/selenium-grid')
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')
# print(f'Current source: {driver.page_source}')  trae todo el codigo fuente
driver.get('https://saucelabs.com/solutions/enterprise')
driver.back()
driver.forward()
driver.refresh()
driver.quit()