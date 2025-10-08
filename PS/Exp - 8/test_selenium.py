from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")
print("PS - IV | Experiment - 8 ")
print("Title is:", driver.title)

# Close the browser
driver.quit()
