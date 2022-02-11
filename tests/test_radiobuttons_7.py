from framework_for_stepic_tasks.methods_selenium import *

import time


open_url("http://suninjuly.github.io/math.html")


def test_people_radio():
    """Проверяем значение атрибута checked у people_radio."""
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


def test_robots_radio():
    """Проверяем значение атрибута checked у robots_radio..."""
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None


def test_disabled_button():
    """Проверяем значение атрибута disabled у кнопки Submit."""
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None


def test_disabled_button_after_timeout():
    """Проверяем значение атрибута disabled у кнопки Submit после таймаута."""
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    time.sleep(12)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None


if __name__ == "__main__":
    pass
