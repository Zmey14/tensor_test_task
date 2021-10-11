from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagesPage(BasePage):
    def should_be_go_to_images_page(self):
        assert 'https://yandex.ru/images' in self.browser.current_url, \
            "Ссылка не совпадает c 'https://yandex.ru/images'"
      
    def open_first_category(self):
        self.browser.find_element(*ImagesPageLocators.OPEN_FIRST_CAT).click()
        assert self.is_element_present(*ImagesPageLocators.OPEN_FIRST_CAT), "Категория не открылась"

    def compare_category(self):
        category1 = self.browser.find_element(*ImagesPageLocators.CATEGORY_ONE).text
        category2 = self.browser.find_element(*ImagesPageLocators.CATEGORY_TWO).get_attribute("value")
        assert category1 == category2, "Категории отличаются"

    def open_first_picture(self):
        picture = self.browser.find_element(*ImagesPageLocators.SEARCH_PICTURE)
        picture.click()
        cheken_open_picture1 = self.is_element_present(*ImagesPageLocators.CHECK_OPEN_PICTURE)
        assert cheken_open_picture1, "картинка не открылась"

    def get_first_picture(self):
        link_1 = self.browser.find_element(*ImagesPageLocators.LINK_ONE_AND_TWO).get_attribute('src')        
        button_next = self.browser.find_element(*ImagesPageLocators.BUTTON_NEXT)
        button_next.click()
        button_back = self.browser.find_element(*ImagesPageLocators.BUTTON_BACK)
        button_back.click()
        link_2 = self.browser.find_element(*ImagesPageLocators.LINK_ONE_AND_TWO).get_attribute('src')
        assert link_1 == link_2, "Изображения разные"
        
