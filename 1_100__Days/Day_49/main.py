from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

ACCOUNT_EMAIL = "vishalkumar1234@gamil.com"
ACCOUNT_PASSWORD = "vishal123"

driver.get("https://appbrewery.github.io/gym/")


join_today_tomorrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3")))
join_today_tomorrow.click()
register = driver.find_element(By.ID, value="toggle-login-register")
register.click()
name = driver.find_element(By.NAME, value="name")
name.send_keys("Vishal Kumar")
email = driver.find_element(By.NAME, value="email")
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.NAME, value="password")
password.send_keys(ACCOUNT_PASSWORD)
submit = driver.find_element(By.ID, value="submit-button")
submit.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            if "Book Class" in button.text:
                button.click()
                booked_count += 1
                print(f"Booked: {class_name} on {day_title}")
            elif "Join Waitlist" in button.text:
                button.click()
                print(f"Joined the waiting List! {class_name} on {day_title}")
                waitlist_count += 1
            elif "Booked" in button.text:
                print(f"{class_name} on {day_title} is already booked!")
                already_booked_count += 1
            else:
                print(f"Choice doesn't exist")


# ***************************************Verification************************************

my_booking = driver.find_element(By.ID, value="my-bookings-link")
my_booking.click()

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n----Total Tuesday/Thursday 6pm classes: {total_booked}---")
print("\n---VERIFYING ON MY BOOKINGS PAGE---")

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f" Verified: {class_name}")
            verified_count += 1
    except ValueError:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} Bookings")
print(f"Found: {verified_count} Bookings")
