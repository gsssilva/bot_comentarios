from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"C:\Users\gsssi\Documents\geckodriver-v0.26.0-win64\geckodriver.exe")
        
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(1)
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        time.sleep(1)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(1)
        password_element.send_keys(Keys.RETURN)
        time.sleep(3)
  
        driver.get("https://www.instagram.com/p/B-FJ44PBXKl/")

  
        comentarios = [
                "Comente aqui para o bot postar"
        ]
        try:
            for sText in comentarios:    
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentarios = driver.find_element_by_class_name('Ypffh')
                time.sleep(1)
                campo_comentarios.send_keys(sText)
                time.sleep(1)
                campo_comentarios.send_keys(Keys.SPACE)
                time.sleep(1)
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(300)
           

        except Exception as e:
            print(e)
            time.sleep(3)


# Entre com o usuário e senha aqui
jhonatanBot = InstagramBot("Usuario", "Senha")
jhonatanBot.login()
