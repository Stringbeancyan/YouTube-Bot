from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHANNEL_URL = "https://www.youtube.com/c/YourChannelName"

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without UI
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get(CHANNEL_URL)
time.sleep(3)

try:
    subscribe_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Subscribe')]")
    subscribe_button.click()
    print("✅ Subscribed successfully!")
except:
    print("❌ Subscription failed.")

driver.quit()
