from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/alert_accept.html")

"""Click the button and confirm action."""
Click.by_class_name("btn.btn-primary")
confirm = browser.switch_to.alert
confirm.accept()

"""Find element X and get text from it. Then give the text
to calc formula."""
x_element = browser.find_element_by_id("input_value")
calculation = calc(x_element.text)

"""Send keys, submit result, wait 5secs and close browser."""
SendKeys.by_id("answer", calculation)
Click.by_class_name("btn.btn-primary")
time_to_copy_result()
close_browser()
