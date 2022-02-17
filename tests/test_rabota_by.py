from framework_for_stepic_tasks.methods_selenium import *


def test_rabota_by_search():
    """Test that sends keys to search field, clicks find button.
    Then uses Xpath to find certain H1, and asserts if vac name in H1."""
    vac_name = "QA Automation Engineer"
    open_url("https://rabota.by/")
    SendKeys.by_id("a11y-search-input", vac_name)
    Click.by_class_name("supernova-search-submit-text")
    h1_with_vac_name = (browser.find_element(By.XPATH,
                                             "/html/body/div[6]/div/div/div[4]/div/div/div[1]/div/h1")).text
    assert vac_name in h1_with_vac_name
    close_browser()


def test_rabota_by_location():
    open_url("https://rabota.by/")
    location_notif = (browser.find_element(By.CLASS_NAME, "HH-Supernova-RegionClarification-Content")).text
    assert "Минск" in location_notif
    close_browser()
