from framework_for_stepic_tasks.methods_selenium import *


def test_google_search():
    """This is test presentation with using simple framework designed by me.
    It's possible to make it more tiny and readable in future. This func is taking 4 strings."""
    open_url("https://google.com")
    SendKeys.by_class_name("gLFyf.gsfi", "QA Automation Engineer\n")
    time_to_copy_result()
    close_browser()


def test_google_search_num_2():
    """And this is test using standart functions. It takes more place.
    This func is taking 6 strings."""
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    search_input = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
    search_input.send_keys("QA Automation Engineer\n")
    time.sleep(5)
    driver.close()
