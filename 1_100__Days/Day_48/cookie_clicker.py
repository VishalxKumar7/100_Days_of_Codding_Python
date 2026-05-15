from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep  # ✅ single import

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://orteil.dashnet.org/cookieclicker/")

language = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
language.click()

sleep(5)  # ✅ no need for time.sleep()

cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "bigCookie")))

wait_time = 5
timeout = time() + wait_time
game_time = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookie_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookie_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):  # ✅ fixed typo
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (Exception, ValueError):  # ✅ fixed except
            print("Couldn't find cookie or items")

        timeout = time() + wait_time

    if time() > game_time:  # ✅ added ()
        try:
            cookie_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookie_element.text}")
        except Exception:  # ✅ fixed except
            print("Couldn't get final cookie count")
        break