"""Run xpath in Amazon."""
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.implicitly_wait(10)
driver.get('https://www.amazon.com.mx/')

print('A elements:')
a_elmts= driver.find_elements_by_xpath("//a")
print(f'Total Elements: {len(a_elmts)}')
for element in a_elmts:
    print(f'{element.text} - {element.get_attribute("href")}')

print('Head children:')
head_elmts = driver.find_elements_by_xpath("//head/*")
print(f'Total Elements: {len(head_elmts)}')
for element in head_elmts:
    print(element.get_attribute("href"))

driver.quit()