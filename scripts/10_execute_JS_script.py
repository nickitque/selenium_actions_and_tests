from framework_for_stepic_tasks.methods_selenium import *


"""Url open."""
open_url("http://suninjuly.github.io/execute_script.html")

"""Find element by id, take this text value ad put into method calc.
Then send the result to field answer."""
x_element = browser.find_element(By.ID, "input_value")
SendKeys.by_id("answer", calc(x_element.text))

"""Scroll the page to become checkbox visible then click checkbox."""
button = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

"""Click the radio button and send results."""
Click.by_ID("robotsRule")
Click.by_class_name("btn.btn-primary")

"""Wait 5 secs and close browser."""
time_to_copy_result()
close_browser()
