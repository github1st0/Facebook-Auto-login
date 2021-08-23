
import os
import sys
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By

class FacebookBot:
    def __init__(self,username,password):
        #Globally declared username and password
        self.username=username
        self.password=password

        #operation system identify
        if sys.platform=="linux":
            driver_path=os.path.join(os.getcwd(),"chromedriver")
        elif sys.platform.startswith("win"):
            driver_path=os.path.join(os.getcwd(),"chromedriver.exe")

        #Browser controller
        self.driver=webdriver.Chrome(executable_path=driver_path)

    #login mechanism
    def login(self):
        #set url location
        url="https://www.facebook.com/login"
        #webdriver receive url for searching
        self.driver.get(url)
        time.sleep(2)

        #username field identify
        username_field=self.driver.find_element(By.NAME,"email")
        #password field identify
        password_field=self.driver.find_element(By.NAME,"pass")
        #login button
        login_button=self.driver.find_element(By.XPATH,'//*[@id="loginbutton"]')


        #fill password and email or mobile number field and click login button
        #username_field
        username_field.send_keys(self.username)
        #password_field
        password_field.send_keys(self.password)
        #click login button
        login_button.click()

def main(username,password):
    bot=FacebookBot(username,password)
    bot.login()
    time.sleep(30)

if __name__=="__main__":
    #input username and password
    username=input("Enter your mobile number or Email:")
    password=getpass.getpass("Enter your password: ")
    main(username,password)