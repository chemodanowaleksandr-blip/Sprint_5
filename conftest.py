import pytest  
from selenium import webdriver  
@pytest.fixture  
def driver():  
    options = webdriver.ChromeOptions()  
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})  
    driver = webdriver.Chrome(options=options)  
    driver.maximize_window()  
    yield driver  
    driver.quit() 
