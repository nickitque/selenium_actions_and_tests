"""Automated script for filling the required data:
Name, Surname, City and Country. Sending it."""

from framework_for_stepic_tasks.methods_selenium import *


"""Url Open."""
open_url("http://suninjuly.github.io/simple_form_find_task.html")

"""Sending all required keys."""
SendKeys.by_name("first_name", "Ivan")
SendKeys.by_name("last_name", "Petrov")
SendKeys.by_class_name("form-control.city", "Smolensk")
SendKeys.by_id("country", "Russia")

"""Button click and browser closing"""
Click.by_css_selector("button.btn")
time_to_copy_result()
close_browser()
