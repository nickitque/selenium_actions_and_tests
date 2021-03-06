from framework_for_stepic_tasks.methods_selenium import *

"""Url open."""
open_url("http://suninjuly.github.io/registration2.html")

"""Sending keys to required fields."""
SendKeys.by_xpath("/html/body/div/form/div[1]/div[1]/input", "Nikita")
SendKeys.by_xpath("/html/body/div/form/div[1]/div[2]/input", "Radzisheuski")
SendKeys.by_xpath("/html/body/div/form/div[1]/div[3]/input", "JustEmailForRegistration@mail.com")
time_to_copy_result()

"""Sending filled form."""
Click.by_css_selector("button.btn")

"""Finding element containing text."""
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

"""Write to variable welcome_text text from element welcome_text_elt"""
welcome_text = welcome_text_elt.text

"""With help of assert we check that expected text is similar to actual text."""
assert "Congratulations! You have successfully registered!" == welcome_text
time_to_copy_result()
close_browser()
