from framework_for_stepic_tasks.methods_selenium import *
import os

"""Url open."""
open_url("http://suninjuly.github.io/file_input.html")

"""Send keys to all required fields."""
SendKeys.by_name("firstname", "Nikita")
SendKeys.by_name("lastname", "Radzisheuski")
SendKeys.by_name("email", "justRandom123EmailAddress@mail.com")

"""Create test.txt file and send it to element with id "file"."""
with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file
path = os.getcwd() + '/' + file.name
SendKeys.by_id("file", path)

"""Send all data, wait 5 secs and close browser."""
Click.by_xpath("/html/body/div/form/button")
time_to_copy_result()
close_browser()