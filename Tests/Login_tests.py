import string
import time
import random

from faker import Faker

from Locators import Login_Locators

succesfull_login_text = "Logged In Successfully"
unsuccesfull_login_text = "Your username is invalid!"
succesfull_url = "https://practicetestautomation.com/logged-in-successfully/"

# Function to run the test case
def succesfull_login():
    Login_Locators.LoginLocators.Email.send_keys("student ")
    Login_Locators.LoginLocators.Password.send_keys("Password123")
    Login_Locators.LoginLocators.Submit_Button.click()
    time.sleep(5)

    actual_text = Login_Locators.LoginLocators.Success_Message
    logout_button_exists = Login_Locators.LoginLocators.logout_button
    current_url = Login_Locators.get_current_url()

    assert succesfull_login_text in actual_text and logout_button_exists > 1 and current_url in succesfull_url

def succesfull_login():
    fake = Faker()

    # Generate random email address
    email = fake.email()

    # Generate random first name
    username = fake.user_name()
    password = fake.password()

    # Generate random phone number with length between 11 and 21 characters
    phone_number = ''.join(random.choices(string.digits, k=random.randint(11, 21)))

    # Generate random subject between 5 and 100 characters
    subject = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(5, 100)))

    # Generate random text for description with length between 20 and 2000 characters
    description = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=random.randint(20, 2000)))

    # URL to send the request to
    url = "https://practicetestautomation.com/practice-test-login/"

    Login_Locators.LoginLocators.Email.send_keys(username)
    Login_Locators.LoginLocators.Password.send_keys(password)
    Login_Locators.LoginLocators.Submit_Button.click()
    time.sleep(5)

    actual_text = Login_Locators.LoginLocators.unsuccesfull_message

    assert unsuccesfull_login_text in actual_text