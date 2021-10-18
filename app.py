import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Declaraciones
ramonLopezAddress = 'https://twitter.com/ramonlopez54'
primeraLineaXPath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article'



browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get(ramonLopezAddress)

time.sleep(5)

prueba = browser.find_element_by_xpath(primeraLineaXPath)

print(prueba.text)

time.sleep(2)
browser.quit()