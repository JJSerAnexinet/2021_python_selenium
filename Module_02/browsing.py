"""Browsing example using Selenium"""

from pathlib import Path
from selenium import webdriver

# from module_02.browsing import get_chrome_path -> jala el metodo para el chromedriver a otro archivo


def get_project_root() -> Path:
    """Get project root path."""
    # 1. Absolute Path file of the project
    return Path(__file__).parent.parent

def get_chrome_path() -> Path:
    """Get chrome driver path."""
    #1. Root = path del chrome driver
    #2. une ambos path "proyecto + chrome"
    root = get_project_root()
    return root.joinpath('drivers','chromedriver')

def get_firefox_path() -> Path:
    """Get Firefox driver path."""
    #1. Root = path del chrome driver
    #2. une ambos path "proyecto + chrome"
    root = get_project_root()
    return root.joinpath('drivers','geckodriver')

def print_page_details(driver: webdriver.Remote):
    """Get page details, title, currentURL, code"""
    print(f'Current title: {driver.title}')
    print(f'Current url: {driver.current_url}')

driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.google.com')
print_page_details(driver)

driver.get('https://www.mlb.com/es')
print_page_details(driver)
print(f'Current source: {driver.page_source}')

driver.get('https://www.nytimes.com/es')
driver.refresh()
print_page_details(driver)

driver.back()

driver.back()
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')

print(driver.get_cookies())
print(driver.application_cache)

if "SOCzOAOac8uhByk5zGU2Zg==" in driver.page_source:
    print("Found")
else:
    print("Not Found")

driver.quit()

