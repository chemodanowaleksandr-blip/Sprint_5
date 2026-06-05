from selenium.webdriver.common.by import By

class MainPageLocators:
    # Ищем элементы по тегам, классам и ссылкам (href), без русского текста
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(@class, 'button_button')]")
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']|.//p[contains(@class, 'header_link')]")
    # Исправленный локатор логотипа: ищет элемент по двум путям для надежности
    LOGO_BUTTON = (By.XPATH, "//*[contains(@class, 'logo')]/a|.//header//a[@href='/']")

    # Разделы конструктора (идем по порядку вкладок)
    BUNS_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[1]")
    SAUCES_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[2]")
    FILLINGS_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[3]")
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")

class RegisterPageLocators:
    # Поля ввода ориентируются на порядковый номер блока fieldset на форме регистрации
    NAME_INPUT = (By.XPATH, "(//form//fieldset)[1]//input")
    EMAIL_INPUT = (By.XPATH, "(//form//fieldset)[2]//input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//form//button")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    PASSWORD_ERROR = (By.XPATH, "//*[contains(@class, 'input__error')]")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//*[contains(@class, 'input__error')]")

class LoginPageLocators:
    # На форме логина всего два поля входа — берем их по порядку fieldset
    EMAIL_INPUT = (By.XPATH, "(//form//fieldset)[1]//input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    ENTER_BUTTON = (By.XPATH, ".//form//button")
    SUCCESS_LOGIN_MARK = (By.XPATH, ".//button[contains(@class, 'button_button_size_large')]")

class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")

class ProfilePageLocators:
    # Кнопка выхода в профиле
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
