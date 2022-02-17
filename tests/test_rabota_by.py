from framework_for_stepic_tasks.methods_selenium import *


def test_google_search():
    """Test that sends keys to search field, clicks find button.
    Then uses Xpath to find certain H1, and asserts if vac name in H1."""
    vac_name = "QA Automation Engineer"
    open_url("https://rabota.by/")
    SendKeys.by_id("a11y-search-input", vac_name)
    Click.by_class_name("supernova-search-submit-text")
    find_h1_with_vac_name = browser.find_element(By.XPATH, "/html/body/div[6]/div/div/div[4]/div/div/div[1]/div/h1")
    h1_with_vac_name = find_h1_with_vac_name.text
    assert vac_name in h1_with_vac_name
    close_browser()
