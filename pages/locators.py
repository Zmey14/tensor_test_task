from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_FIELDS = (By.CSS_SELECTOR, "#text")
    SUGGEST_FIELD = (By.CSS_SELECTOR, ".mini-suggest__popup_svg_yes")
    FIVE_LINKS = (By.XPATH, "//h2/a[@href]")
    SEARCH_LINK_IMAGES = (By.CSS_SELECTOR, "ul > li:nth-child(3) > a")


class ImagesPageLocators():
    SEARCH_LINK_IMAGES = (By.CSS_SELECTOR, "ul > li:nth-child(3) > a")
    OPEN_FIRST_CAT = (By.CSS_SELECTOR, "div.PopularRequestList-Item")
    CATEGORY_ONE = (By.CSS_SELECTOR, "div .PopularRequestList-SearchText")
    CATEGORY_TWO = (By.CSS_SELECTOR, "[name='text']")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next .CircleButton-Icon")
    BUTTON_BACK = (By.CSS_SELECTOR, ".CircleButton_type_prev .CircleButton-Icon")
    CHECK_OPEN_PICTURE = (By.CSS_SELECTOR, "img.MMImage-Origin")
    SEARCH_PICTURE = (By.CSS_SELECTOR, "a.serp-item__link")
    LINK_ONE_AND_TWO = (By.CSS_SELECTOR, "img.MMImage-Origin")
    
