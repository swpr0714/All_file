import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/edgedriver_win64/msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://cds.climate.copernicus.eu/#!/home")
time.sleep(5)
driver.quit()

