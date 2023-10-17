from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import sys


author = sys.argv[1]

output = { "author": { "name": author } }

driver = webdriver.Chrome()

page = driver.get("https://quotes.toscrape.com/")

quotes = driver.find_element(by=By.CLASS_NAME, value="quote")

with open("quotes.json", "w") as outfile:
  json.dump(output, outfile)

driver.quit()