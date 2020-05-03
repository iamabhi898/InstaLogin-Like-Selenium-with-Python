# a short Program to login Insta and like the first post in feed

'''

LOOK FOR THE USERNAME AND PASSWORD COMMENT (line 34 and 38)
DELETE '>>here<<' THEN ENTER YOUR USERNAME AND PASSWORD AS MENTIONDED


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/")
print(driver.title)

try:
    search_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q")))
    search_element.send_keys("instagram login")
    search_element.send_keys(Keys.RETURN)
    insta_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="r"]/a/h3')))
    insta_link.click()
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))
    username_element.send_keys(">>here<<")
    #                 user name ^^^^^^^^
    passwd_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password")))
    passwd_element.send_keys(">>here<<")
    #                password ^^^^^^^^
    passwd_element.send_keys(Keys.RETURN)
    popup_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]")))
    popup_element.click()
    like_first = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='wpO6b ']")))
    like_first.click()

except:
    print("couldn't like")
