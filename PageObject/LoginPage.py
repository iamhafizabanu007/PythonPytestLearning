from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    text_username_id="Email"
    text_password_id="Password"
    button_type="//button[@type='submit']"
    link_text_logout="Logout"

    def __init__(self,driver):
        self.driver=driver

    def username(self,username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)
    def password(self,password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)
    def login(self):
        self.driver.find_element(By.XPATH,self.button_type).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_text_logout).click()
