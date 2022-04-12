from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/math.html")

"""Taking value of x by it's id. And putting the value to math formula."""
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

"""Send keys, submit result, wait 5secs and close browser."""
SendKeys.by_id("answer", y)
Click.by_ID("robotCheckbox")
Click.by_ID("robotsRule")
Click.by_class_name("btn.btn-default")
time_to_copy_result()
close_browser()
