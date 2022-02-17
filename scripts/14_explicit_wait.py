from framework_for_stepic_tasks.methods_selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Url open."""
open_url("http://suninjuly.github.io/explicit_wait2.html")

"""Waiting until the price become $100 and then clicking the button."""
element = WebDriverWait(browser, 15)\
    .until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
Click.by_ID("book")

"""Getting text attrubute, calculating it, sending keys and clicking
the button. Then closing browser."""
x_element = (browser.find_element(By.ID, "input_value")).text
SendKeys.by_id("answer", calc(x_element))
Click.by_ID("solve")
close_browser()
