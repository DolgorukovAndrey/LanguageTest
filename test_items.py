import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза для визуальной проверки языка (по требованию задания)
    time.sleep(30)

    # Ищем кнопку добавления в корзину (уникальный селектор для этой страницы)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка есть на странице
    assert button is not None, "Кнопка добавления в корзину не найдена"