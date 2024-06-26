import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_with_valid_credentials():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    driver.find_element(By.ID,"input-email").send_keys("ujwllive247@gmail.com")
    driver.find_element(By.ID,"input-password").send_keys("Kangaroo@123")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()

    assert driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
    driver.quit()


def test_login_with_invalid_credentials():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_stamp())
    driver.find_element(By.ID, "input-password").send_keys("Kangaroo@123")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
    driver.quit()



def test_login_with_valid_email_and_invalid_password():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("ujwllive247@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("Kangadddsdfroo@123")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
    driver.quit()


def test_login_without_entering_credentials():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
    driver.quit()




def generate_email_with_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%N_%S")
    return "ujwllive"+time_stamp+"@gmail.com"




