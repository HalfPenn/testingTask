from urllib import request
from playwright.sync_api import sync_playwright
import pytest

# Ожидаемый заголовок страницы
EXPECTED_TITLE = "Playwright: Fast and reliable end-to-end testing"

# Список браузеров для тестирования
BROWSERS = ["chromium", "webkit"]

# Фикстура для запуска браузера
@pytest.fixture(params=BROWSERS)
def browser_instance(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=True)
        yield browser
        browser.close()

# Тест проверяет заголовок страницы
def test_playwright_title(browser_instance):
    page = browser_instance.new_page()
    page.goto("https://playwright.dev/")
    title = page.title()
    assert title == EXPECTED_TITLE, f"Заголовок не совпадает в браузере {request.param}"
    print(f"Проверка пройдена успешно в браузере: {request.param}")