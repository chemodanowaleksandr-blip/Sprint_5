from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
from helpers import generate_random_email, generate_random_password

# Актуальный адрес учебного стенда Stellar Burgers в Практикуме
base_host = "stellarburgers.education-services.ru"


class TestRegistration:
    def test_successful_registration(self, driver):
        # Открываем страницу регистрации
        driver.get(f"https://{base_host}/register")
        
        email = generate_random_email()
        password = generate_random_password(6)
        
        # Ожидаем появления формы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Ожидаем автоматический переход на страницу входа
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))
        assert driver.current_url == f"https://{base_host}/login"

    def test_registration_password_error(self, driver):
        # Открываем страницу регистрации
        driver.get(f"https://{base_host}/register")
        
        invalid_password = generate_random_password(5)  # Короткий пароль для ошибки
        
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_random_email())
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем отображение текста ошибки
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )
        assert error_element.text == "Некорректный пароль"
