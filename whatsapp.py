import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep #sending image to whatsapp

driver = webdriver.Chrome('/Summer Internship/tasks/task6/chromedriver')
driver.get("https://web.whatsapp.com/")
sleep(20)
# input("Plese scan qr code and press: ")
RM = driver.find_element_by_xpath('//span[@title = "Bhushan"]')
RM.click()
testinput = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
testinput.send_keys("Hello Bhushan , This is message from message task 6  ")
sleep(2)
testinput.send_keys(Keys.RETURN)
print("\t\t\t\n********************** Whatsapp Successfully *********************************\n")
        