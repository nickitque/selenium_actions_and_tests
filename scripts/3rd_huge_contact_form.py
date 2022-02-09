from framework_for_stepic_tasks.methods_selenium import *

open_url("http://suninjuly.github.io/huge_form.html")

SendKeys.by_tag_name("input", "Pass")
Click.by_css_selector("button.btn")
close_browser()