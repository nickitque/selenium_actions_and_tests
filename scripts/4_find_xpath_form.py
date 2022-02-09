from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/find_xpath_form")

"""Sending keys."""
SendKeys.by_name("first_name", "Ivan")
SendKeys.by_name("last_name", "Sidorov")
SendKeys.by_class_name("form-control.city", "Minsk")
SendKeys.by_id("country", "Belarus")

"""Finding button by xpath and clicking."""
Click.by_xpath("/html/body/div/form/div[6]/button[3]")

"""Waiting 5s and closing browser"""
time_to_copy_result()
close_browser()


