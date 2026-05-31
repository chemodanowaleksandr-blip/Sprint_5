from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") 
    # Железный поиск по атрибуту ссылки — JS-клик по нему бьет без промахов
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']") 
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[text()='Конструктор']") 
    LOGO_BUTTON = (By.XPATH, ".//header//a[@href='/']") 
    
    # Разделы конструктора
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/..") 
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/..") 
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/..") 
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]") 

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/../input") 
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input") 
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']") 
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") 
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") 
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]") 

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input") 
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']") 
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']") 
    SUCCESS_LOGIN_MARK = (By.XPATH, ".//button[text()='Оформить заказ']") 

class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") 

class ProfilePageLocators:
    # Ищем строго слово 'Выход', как на вашем скриншоте страницы профиля
    EXIT_BUTTON = (By.XPATH, ".//*[text()='Выход']") 
