from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from time import sleep

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("http://google.com")
print('Está funcionando!')
sleep(10)
driver.quit()