#pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url= r"C:\Program Files\Google\Chrome\Application"

service = Service(executable_path= url)
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('https://www.google.com/')
    #find element by xpath
    searchinp = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
    searchinp.send_keys('ChromeDriver')

    searchButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    searchButton.click()
    time.sleep(15) # Let the user actually see something!



 