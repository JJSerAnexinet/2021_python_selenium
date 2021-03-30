"""Browsing example using Selenium"""

from pathlib import Path
from selenium import webdriver


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

driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.google.com')
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')

driver.get('https://www.mlb.com/es')
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')
print(f'Current source: {driver.page_source}')

driver.get('https://www.nytimes.com/es')
driver.refresh()
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')
driver.back()
driver.back()
print(f'Current title: {driver.title}')
print(f'Current url: {driver.current_url}')