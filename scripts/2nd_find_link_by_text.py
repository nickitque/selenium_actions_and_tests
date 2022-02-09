"""This is automated script for finding link by text and then
sending keys to contact form."""

from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/find_link_text")

"""Finding link by text"""
Click.by_link_text("224592")
SendKeys.by_name("first_name", "Ivan")
SendKeys.by_name("last_name", "Petrov")
SendKeys.by_class_name("form-control.city", "Smolensk")
SendKeys.by_id("country", "Russia")
Click.by_css_selector("button.btn")
close_browser()
