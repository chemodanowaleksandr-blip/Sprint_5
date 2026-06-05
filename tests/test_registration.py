from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
from helpers import generate_random_email, generate_random_password, TestData

# Актуальный адрес учебного стенда Stellar Burgers в Практикуме


class TestRegistration:
    def test_successful_registration(self, driver):
        # Открываем страницу регистрации
        driver.get(f"https://{TestData.BASE_HOST}/register")

        email = generate_random_email()
        password = generate_random_password(6)

        # Ожидаем появление формы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ожидаем автоматический переход на страницу входа
        # УВЕЛИЧЕНО ВРЕМЯ ОЖИДАНИЯ ДО 15 СЕКУНД, ЧТОБЫ ТЕСТ НЕ ПАДАЛ ИЗ-ЗА МЕДЛЕННОГО СТЕНДА
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.ENTER_BUTTON))
        assert driver.current_url == f"https://{TestData.BASE_HOST}/login"

    def test_registration_password_error(self, driver):
        # Открываем страницу регистрации
        driver.get(f"https://{TestData.BASE_HOST}/register")

        email = generate_random_email()
        # Пароль меньше 6 символов для проверки ошибки
        password = generate_random_password(5)

        # Ожидаем появление формы
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Александр")
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Проверяем отображение ошибки некорректного пароля
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR_MESSAGE))
        assert driver.find_element(*RegisterPageLocators.PASSWORD_ERROR_MESSAGE).is_displayed()

