from framework_for_stepic_tasks.methods_selenium import *
vac_name = "QA Automation Engineer"


def test_rabota_by_search():
    """Test that sends keys to search field, clicks find button.
    Then uses Xpath to find certain H1, and asserts if vac name in H1."""
    open_url("https://rabota.by/")
    SendKeys.by_id("a11y-search-input", vac_name)
    Click.by_class_name("supernova-search-submit-text")
    h1_with_vac_name = (browser.find_element(By.XPATH,
                                             "/html/body/div[6]/div/div/div[4]/div/div/div[1]/div/h1")).text
    assert vac_name in h1_with_vac_name
    close_browser()


def test_rabota_by_location():
    """This test checks if there string Минск in location notification."""
    open_url("https://rabota.by/")
    location_notif = (browser.find_element(By.CLASS_NAME, "HH-Supernova-RegionClarification-Content")).text
    assert "Работа в Минске, свежие вакансии - rabota.by" == browser.title
    assert "Минск" in location_notif
    close_browser()


def test_rabota_by_cvs():
    """This test switches search from Vacancies to CVs,
    Sends keys QA Automation Engineer. Gets attribute of
    search field, and asserts if its vac_name in value."""
    open_url("https://rabota.by/")
    Click.by_class_name("supernova-dashboard-link-switch")
    button = browser.find_element(By.CLASS_NAME, "employer-index-search-submit-label")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    SendKeys.by_xpath("/html/body/div[6]/div/div/div[5]/div/div[2]"
                      "/div/div/div[3]/form/div[1]/div[1]/input", vac_name)
    button.click()
    search_field = browser.find_element(By.ID, "a11y-search-input")
    attribute_value = search_field.get_attribute("value")
    assert attribute_value == vac_name
    close_browser()
