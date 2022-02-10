from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/get_attribute.html")

"""Get Imagage attribute value to put it into Math function."""
x_element = browser.find_element(By.ID, "treasure")
attribute = x_element.get_attribute("valuex")
answer = calc(attribute)

"""Send keys, click checkbox and radio buttions, send results."""
SendKeys.by_id("answer", answer)
Click.by_ID("robotCheckbox")
Click.by_ID("robotsRule")
Click.by_class_name("btn.btn-default")

"""Time to visual check the results of script work and close browser."""
time_to_copy_result()
close_browser()
