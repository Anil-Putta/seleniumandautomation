from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
service = Service("/home/anil/Downloads/geckodriver-v0.36.0-linux64/geckodriver")	
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
driver.quit()
