from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json
import sys


author_input = str(sys.argv[1])

driver = webdriver.Chrome()

all_author_quotes = []

start_link = "https://quotes.toscrape.com"

page = driver.get(start_link)

isThereANextPage = True

about_link = ''

while isThereANextPage:
  
  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "quote")))

  quotes_containers = driver.find_elements(By.CLASS_NAME, "quote")

  author_quotes_on_page = []

  for quote_container in quotes_containers:
    
    author = quote_container.find_element(By.CLASS_NAME, "author").text
    if (author != author_input): 
      continue
    
    if (len(about_link) == 0):
      about_link = quote_container.find_element(By.TAG_NAME, "a").get_attribute("href")
    
    quote = quote_container.find_element(By.CLASS_NAME, "text").text.strip('\u201c').strip('\u201d')

    tags = []
    tags = quote_container.find_element(By.CLASS_NAME, "tags").text.split(" ")
    tags.pop(0)

    author_quotes_on_page.append({ "text": quote, "tags": tags })

  all_author_quotes += author_quotes_on_page

  try:
    next_page = driver.find_element(By.CLASS_NAME, "next")
    next_page_link = next_page.find_element(By.TAG_NAME, "a")
    next_page_link.click()
  except NoSuchElementException:
    isThereANextPage = False

page = driver.get(about_link)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "author-details")))

author_name = driver.find_element(By.CLASS_NAME, "author-title").text
author_birth_date = driver.find_element(By.CLASS_NAME, "author-born-date").text
author_birth_location = driver.find_element(By.CLASS_NAME, "author-born-location").text
author_description = driver.find_element(By.CLASS_NAME, "author-description").text

author_info = {
  "author": {
    "name": author_name,
    "birth_date": author_birth_date,
    "birth_location": author_birth_location,
    "description": author_description,
    "quotes": all_author_quotes
  }
}

with open("author.json", "w") as outfile:
  json.dump(author_info, outfile)

driver.quit()