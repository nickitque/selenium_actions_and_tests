from framework_for_stepic_tasks.methods_selenium import *


def test_google_search():
    """Test for sending key QA Automation Engineer in google search field."""
    open_url("https://google.com")
    SendKeys.by_class_name("gLFyf.gsfi", "QA Automation Engineer\n")
    time_to_copy_result()
    search_field = browser.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    attribute = search_field.get_attribute("value")
    assert "QA Automation Engineer" in browser.title
    assert attribute == "QA Automation Engineer"
    close_browser()


def test_google_search_num_2():
    """Test for sending empty string to search field."""
    open_url("https://google.com")
    SendKeys.by_class_name("gLFyf.gsfi", "\n")
    assert "Google" == browser.title
    time.sleep(5)
    browser.close()
