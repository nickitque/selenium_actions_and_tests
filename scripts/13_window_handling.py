from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/redirect_accept.html")

"""Click the button and switch the window."""
Click.by_class_name("trollface.btn.btn-primary")
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

"""Find element X and get text from it. Then give the text
to calc formula."""
x_element = browser.find_element_by_id("input_value")
calculation = calc(x_element.text)

"""Send keys, submit result, wait 5secs and close browser."""
SendKeys.by_id("answer", calculation)
Click.by_class_name("btn.btn-primary")
time_to_copy_result()
close_browser()