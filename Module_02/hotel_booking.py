"""Fill student form."""
from selenium.webdriver.support.select import Select
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.implicitly_wait(5)
driver.get('https://formsmarts.com/form/axi?mode=h5')

first_name = driver.find_element_by_id('u_Nqo_60857')
first_name.clear()
first_name.send_keys('Jesus')

last_name = driver.find_element_by_id('u_Nqo_60858')
last_name.clear()
last_name.send_keys('Serna')

email = driver.find_element_by_id('u_Nqo_60859')
email.clear()
email.send_keys('test@hotmail.com')

address = driver.find_element_by_id('u_Nqo_60860')
address.clear()
address.send_keys('123 address')

country = Select(driver.find_element_by_id('u_Nqo_60871'))
country.select_by_index(2)

check_in_date = driver.find_element_by_id('u_Nqo_60861')
check_in_date.clear()
check_in_date.send_keys('27042021')

double_room_btn = driver.find_element_by_id('u_Nqo_60866_0')
double_room_btn.click()

number_of_nights = driver.find_element_by_id('u_Nqo_60870')
number_of_nights.clear()
number_of_nights.send_keys('5')

continue_btn = driver.find_element_by_name('submit')
continue_btn.click()

driver.implicitly_wait(5)

validate = driver.find_elements_by_tag_name('td')
if validate [0].text == 'Jesus':
    print(f'El nombre "{validate[0].text}" es correcto.')
if validate[1].text == 'Serna':
    print(f'El lastname "{validate[1].text}" es correcto.')
if validate[2].text == 'test@hotmail.com':
    print(f'El mail "{validate[2].text}" es correcto.')
if validate[3].text == '123 address':
    print(f'El address "{validate[3].text}" es correcto.')
if validate[4].text == 'Åland Islands':
    print(f'El country "{validate[4].text}" es correcto.')
if validate[5].text == 'Tuesday April 27, 2021':
    print(f'El checking "{validate[5].text}" es correcto.')
if validate[6].text == 'Double Room ($160 USD)':
    print(f'El room type "{validate[6].text}" es correcto.')
if validate[7].text == '5':
    print(f'El numero de noches "{validate[7].text}" es correcto.')

driver.quit()