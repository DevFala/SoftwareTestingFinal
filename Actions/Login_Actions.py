from Locators import Login_Locators

def click_login_button():
    Login_Locators.LoginLocators.Submit_Button.click()

def get_current_rul():
    get_url = driver.current_url