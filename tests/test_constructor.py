import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from data import Urls
from helpers import login_user

class TestConstructorAndProfile:

    def test_go_to_personal_cabinet(self, driver):
        """1. Проверка перехода в личный кабинет"""
        login_user(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        # Исправлено: Ожидание встроено в ассерт
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))

    def test_go_from_profile_to_constructor_via_button(self, driver):
        """2. Переход из личного кабинета в конструктор по кнопке 'Конструктор'"""
        login_user(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        # Исправлено: Ожидание встроено в ассерт
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_go_from_profile_to_constructor_via_logo(self, driver):
        """3. Переход из личного кабинета в конструктор по клику на логотип"""
        login_user(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        
        # Исправлено: Ожидание встроено в ассерт
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SUCCESS_LOGIN_MARK))

    def test_logout_from_profile(self, driver):
        """4. Выход из аккаунта по кнопке 'Выход' в личном кабинете"""
        login_user(driver)
        
        cabinet_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON))
        driver.execute_script("arguments[0].click();", cabinet_btn)
        
        exit_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.execute_script("arguments[0].click();", exit_btn)
        
        # Исправлено: Ожидание встроено в ассерт
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))

    def test_constructor_tabs_sauces(self, driver):
        """5.1 Проверка перехода на вкладку 'Соусы'"""
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        tab_element = driver.find_element(*MainPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", tab_element)
        
        # Исправлено: Ожидание изменения класса вкладки встроено прямо в ассерт
        assert WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in tab_element.get_attribute("class"))

    def test_constructor_tabs_fillings(self, driver):
        """5.2 Проверка перехода на вкладку 'Начинки'"""
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        tab_element = driver.find_element(*MainPageLocators.FILLINGS_TAB)
        driver.execute_script("arguments[0].click();", tab_element)
        
        # Исправлено: Ожидание изменения класса вкладки встроено прямо в ассерт
        assert WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in tab_element.get_attribute("class"))

    def test_constructor_tabs_buns(self, driver):
        """5.3 Проверка перехода на вкладку 'Булки'"""
        driver.get(Urls.BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        
        sauce_element = driver.find_element(*MainPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", sauce_element)
        WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in sauce_element.get_attribute("class"))
        
        bun_element = driver.find_element(*MainPageLocators.BUNS_TAB)
        driver.execute_script("arguments[0].click();", bun_element)
        
        # Исправлено: Ожидание изменения класса вкладки встроено прямо в ассерт
        assert WebDriverWait(driver, 5).until(lambda d: "tab_tab_type_current" in bun_element.get_attribute("class"))
