from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()


def open_url(url):
    """Get Method."""
    browser.get(url)


def close_browser():
    """Closing browser after needed operations."""
    browser.quit()


def time_to_copy_result():
    """Method that is usually used before close browser method
    to visual check the results of script executing"""
    time.sleep(5)


def calc(x):
    """Math formula needed for tasks starting from script #7."""
    return str(math.log(abs(12*math.sin(int(x)))))


class SendKeys:
    """Class for sending keys depending of the element type."""
    # def by_locator(locator, key):
    #     element = browser.find_element(locator)
    #     element.send_keys(key)

    def by_name(el_name, key):
        element = browser.find_element(By.NAME, el_name)
        element.send_keys(key)

    def by_class_name(element_name, key):
        element = browser.find_element(By.CLASS_NAME, element_name)
        element.send_keys(key)

    def by_id(el_name, key):
        element = browser.find_element(By.ID, el_name)
        element.send_keys(key)

    def by_tag_name(el_name, key):
        elements = browser.find_elements(By.TAG_NAME, el_name)
        for element in elements:
            element.send_keys(key)

    def by_xpath(el_name, key):
        element = browser.find_element(By.XPATH, el_name)
        element.send_keys(key)


class Click:
    """Class for clicking buttons depending of the element type."""
    def by_link_text(el_name):
        button = browser.find_element(By.LINK_TEXT, el_name)
        button.click()

    def by_css_selector(el_name):
        button = browser.find_element(By.CSS_SELECTOR, el_name)
        button.click()

    def by_xpath(el_name):
        button = browser.find_element(By.XPATH, el_name)
        button.click()

    def by_ID(el_name):
        button = browser.find_element(By.ID, el_name)
        button.click()

    def by_class_name(el_name):
        button = browser.find_element(By.CLASS_NAME, el_name)
        button.click()


