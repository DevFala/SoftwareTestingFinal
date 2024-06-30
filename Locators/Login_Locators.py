from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver

def get_current_url():
    return driver.current_url

class LoginLocators:
    Email = driver.find_element(By.XPATH, "//*[@id='username']")
    Password = driver.find_element(By.XPATH, "//*[@id='password']")
    Submit_Button = driver.find_element(By.XPATH, "//*[@id='submit']")
    Success_Message = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1")
    logout_button = driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[2]/div/div/div/a")
    unsuccesfull_message = driver.find_element(By.XPATH, "//*[@id='error']")