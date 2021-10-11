from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELDS), f"Поле поиска на главной странице не найдено"

    def input_word_in_search_field(self):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELDS).send_keys("Тензор")
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mini-suggest__popup_svg_yes")))
        assert self.is_element_present(*MainPageLocators.SUGGEST_FIELD), f"Выпадающее меню отсутствует"

    def search_results(self):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELDS).send_keys(Keys.ENTER)
        five_links = self.browser.find_elements(*MainPageLocators.FIVE_LINKS)[:5]
        links = [link.get_attribute('href') for link in five_links]
        for i in links:
            if "tensor.ru" in i:
                assert i
            else:
                assert "tensor.ru" in links, f"Одна или несколько ссылок не переходят на tensor.ru"

    def check_images(self):
        link = self.browser.find_element(*MainPageLocators.SEARCH_LINK_IMAGES).get_attribute("href")
        assert "images" in link, "Отсутствует ссылка на картинки"
        
    def go_to_images_page(self):
        images_link = self.browser.find_element(*MainPageLocators.SEARCH_LINK_IMAGES)
        images_link.click()
        new_window = self.browser.window_handles[1]  
        self.browser.switch_to.window(new_window)

        
        