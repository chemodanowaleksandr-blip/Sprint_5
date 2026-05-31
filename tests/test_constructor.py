import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators

# Актуальный домен стенда
base_host = "stellarburgers.education-services.ru"

class TestConstructorAndProfile:
    # Зарегистрированный на стенде постоянный аккаунт
    EMAIL = "alexandr_test_burgers@yandex.ru"
    PASSWORD = "password123"

    def login_helper(self, driver):
        """Вспомогательный метод для авторизации перед тестами профиля"""
        driver.get(f"https://{base_host}/login")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_go_to_personal_cabinet(self, driver):
        """1. Проверка перехода в личный кабинет"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        # Ожидаем появление кнопки Выход
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        assert "account" in driver.current_url

    def test_go_from_profile_to_constructor_via_button(self, driver):
        """2. Переход из личного кабинета в конструктор по кнопке 'Конструктор'"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        
        # Возвращаемся в Конструктор
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
        assert "account" not in driver.current_url

    def test_go_from_profile_to_constructor_via_logo(self, driver):
        """3. Переход из личного кабинета в конструктор по клику на Логотип"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        # ИСПРАВЛЕНО: Добавлен индекс [0] для корректного JavaScript-клика
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        
        # Кликаем на логотип
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))
        assert "account" not in driver.current_url

    def test_logout_from_profile(self, driver):
        """4. Выход из аккаунта по кнопке 'Выход' в личном кабинете"""
        self.login_helper(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        
        # Прожимаем Выход
        driver.find_element(*ProfilePageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))
        assert "login" in driver.current_url

    def test_constructor_tabs_navigation(self, driver):
        """5. Проверка переходов по вкладкам Конструктора (Булки, Соусы, Начинки)"""
        driver.get(f"https://{base_host}/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(MainPageLocators.SAUCES_TAB, "class", "tab_tab_type_current")
        )
        
        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(MainPageLocators.FILLINGS_TAB, "class", "tab_tab_type_current")
        )

        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(MainPageLocators.BUNS_TAB, "class", "tab_tab_type_current")
        )
