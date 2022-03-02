from selenium.webdriver.common.by import By

class RegionChooseLocators():
    """Locators for pop-up page where user can choose region.
    It has no url because it's pop-up and can be called in header."""
    MINSK = (By.PARTIAL_LINK_TEXT[0], "brest.rabota.by")
    BREST = (By.XPATH,"/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/ul/li[2]/a")
    VITEBSK = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/ul/li[3]/a")
    GOMEL = (By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/ul/li[4]/a")


class MainPageLocators():
    """Locators for main page rabota.by"""
    REGION_SWITCH = (By.CLASS_NAME, "supernova-navi-item_area-switcher-button")
    VACANCY_SEARCH = (By.ID, "a11y-search-input")