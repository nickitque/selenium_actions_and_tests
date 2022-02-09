from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/huge_form.html")

"""Sending keys. Waiting 5s and closing browser."""
SendKeys.by_tag_name("input", "Pass")
Click.by_css_selector("button.btn")
time_to_copy_result()
close_browser()
