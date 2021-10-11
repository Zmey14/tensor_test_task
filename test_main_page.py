from .pages.main_page import MainPage
from .pages.images_page import ImagesPage
import pytest


@pytest.mark.xfail(reason="Возможно одна или несколько ссылкок недоступны")
def test_search_field(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.search_field()
    page.input_word_in_search_field()
    page.search_results()

def test_go_to_image_page(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_images()
    page.go_to_images_page()
    images_page = ImagesPage(browser, browser.current_url)
    images_page.should_be_go_to_images_page()
    images_page.open_first_category()
    images_page.compare_category()
    images_page.open_first_picture()
    images_page.get_first_picture()






    
