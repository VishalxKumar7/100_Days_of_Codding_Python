from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# ***********************************************************************************************
# driver.get("https://en.wikipedia.org/wiki/?gad_source=1&gad_campaignid=23567450077&gbraid=0AAAABB0-3wG2OIlJ9UqTSf2iyTfmRY99I&gclid=CjwKCAjw5ZXQBhBdEiwAI5XVWZVh1iPWW3rRmqX7WHQHLB9bgvrI_CM5Ji-2wBvpbCsXlRuGDcqQKRoC1b0QAvD_BwE")

# active_editor = driver.find_element(By.CSS_SELECTOR, value='#articlecount ul li a')
# # active_editor.click()

# # Find elements by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Operation Brevity")
# # all_portals.click()

# # Find the "Search" <input? by Name
# search = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "cdx-text-input__input"))
# )
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# ************************************************************************************************

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "fName")))
fname.send_keys("Vishal")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Kumar")

mail = driver.find_element(By.NAME, value="email")
mail.send_keys("singvishal40001@gmail.com")

sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-block")))
sign_up.send_keys(Keys.ENTER)

# driver.quit()
