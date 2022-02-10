from framework_for_stepic_tasks.methods_selenium import *
from selenium.webdriver.support.ui import Select
import time
"""Url open."""
open_url("http://suninjuly.github.io/selects1.html")

"""Open dropdown menu by clicking element by ID.
Get text value of num1 and num2.Then calculate num1+num2
integers and making it string."""
Click.by_ID("dropdown")
x_element = browser.find_element(By.ID, "num1")
y_element = browser.find_element(By.ID, "num2")
x = x_element.text
y = y_element.text
z = str(int(x)+int(y))
print(z)

"""Select element from dropdown list."""
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(z)  # ищем элемент с текстом "z1"

"""Send results, wait 5 secs and close browser."""
Click.by_class_name("btn.btn-default")
time_to_copy_result()
close_browser()