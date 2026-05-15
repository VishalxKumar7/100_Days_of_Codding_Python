from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/Samsung-Storage-Snapdragon-6-9-inch-Included/dp/B0GZQ5LX5G/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.952404da-f039-400e-881e-29c0c23c310a&dib=eyJ2IjoiMSJ9.37vjao5HMmuGZ2aDko-F5VhHxBpCYQwH_LkWJOthvVtVYpl_26lw0Yq-LxBRAbxGqsJjyZKoZzt_QdxpBkWVWTx_4lfHegftBrSarrJaRNaCY_qzmAiaIhoJ1XojVNIhNnupW0F5NKH51u3X-MLOHLeBkt83hjKmEC_LLYTprBNefmm4iAje7KZWvkD1y2dqee138l0Aqx6kThJ46weUa2rVDv3q8OeNDsuoVdpgDWlJM6A7_SzyH7MHpO3rLghP_XzyvVHoTJXfoa20ryGmrddLwbXdgB4H2BVHca-8JZQ.clsXtf88XeWD7MAN3UDJkvDTHWbY_JHcQvMAgCZJsFA&dib_tag=se&pd_rd_r=32730eba-eded-489a-9773-ae2ae6bfa507&pd_rd_w=J2kVM&pd_rd_wg=SDf8E&qid=1778819792&refinements=p_123%3A46655&rnid=1389432031&s=electronics&sr=1-1-spons&aref=MvURCxmn4I&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&psc=1")
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"The price is {price.text}")


driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# button = driver.find_element(By.ID,value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_name[n].text
    }

print(events)

# driver.close() # Closes the single tab you are using
driver.quit()  # Closed the app