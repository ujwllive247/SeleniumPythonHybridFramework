from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_register_with_mandatory_field():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("Ashutosh")
    driver.find_element(By.ID,"input-lastname").send_keys("Gupta")
    driver.find_element(By.ID,"input-email").send_keys(generate_email_with_stamp())
    driver.find_element(By.ID,"input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("act@321")
    driver.find_element(By.ID, "input-confirm").send_keys("act@321")
    driver.find_element(By.NAME,"agree").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_heading_text = "Your Account Has Been Created!"

    assert driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_heading_text)
    driver.quit()



def register_with_all_fields():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Ashutosh")
    driver.find_element(By.ID, "input-lastname").send_keys("Gupta")
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_stamp())
    driver.find_element(By.ID, "input-telephone").send_keys("123456789")
    driver.find_element(By.ID, "input-password").send_keys("act@321")
    driver.find_element(By.ID, "input-confirm").send_keys("act@321")
    driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    expected_heading_text = "Your Account Has Been Created!"

    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)
    driver.quit()


def generate_email_with_stamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%N_%S")
    return "ujwllive"+time_stamp+"@gmail.com"

