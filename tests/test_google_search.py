
from selenium import webdriver


def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print("hhh")