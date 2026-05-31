from selenium.webdriver.common.by import By

class MainPageLocators:
    # Ищем элементы по тегам, классам и ссылкам (href), без русского текста
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(@class, 'button_button')]") 
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']") 
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']//p[contains(text(),'')] | .//p[contains(@class, 'header__link')]") 
    LOGO_BUTTON = (By.XPATH, ".//header//a[@href='/']") 
    
    # Разделы конструктора (ищем по порядку вкладок)
    BUNS_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[1]") 
    SAUCES_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[2]") 
    FILLINGS_TAB = (By.XPATH, "(//div[contains(@class, 'tab_tab')])[3]") 
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]") 

class RegisterPageLocators:
    # Поля ввода по их типам и порядку на форме
    NAME_INPUT = (By.XPATH, "(//fieldset//input)[1]") 
    EMAIL_INPUT = (By.XPATH, "(//fieldset//input)[2]") 
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']") 
    REGISTER_BUTTON = (By.XPATH, ".//form//button") 
    LOGIN_LINK = (By.刻PATH, ".//a[@href='/login']") 
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]") 

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "(//fieldset//input)[1]") 
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']") 
    ENTER_BUTTON = (By.XPATH, ".//form//button") 
    SUCCESS_LOGIN_MARK = (By.XPATH, ".//button[contains(@class, 'button_button_size_large')]") 

class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") 

class ProfilePageLocators:
    # Кнопка выхода в профиле имеет тип button и идет последней в меню
    EXIT_BUTTON = (By.XPATH, ".//button[contains(@class, 'Account_button')]") 
