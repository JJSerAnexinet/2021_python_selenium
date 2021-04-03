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
    return root.joinpath('drivers', 'chromedriver')

def navigate_2url(url):
    driver.find_element_by_link_text(url).click()
    print(driver.page_source.count('Selenium'))

driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.selenium.dev')
navigate_2url('Downloads')
navigate_2url('Projects')
navigate_2url('Support')
navigate_2url('Blog')
