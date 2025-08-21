from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.get("https://demo.testfire.net/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)  # wait up to 10 seconds for elements

# Step 1: Click "Sign In"
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

# Step 2: Enter login details
wait.until(EC.presence_of_element_located((By.ID, "uid"))).send_keys("jsmith")
driver.find_element(By.ID, "passw").send_keys("Demo1234")
driver.find_element(By.NAME, "btnSubmit").click()

# ✅ 5 working clicks after login
pages = [
    "View Account Summary",
    "View Recent Transactions",
    "Transfer Funds",
    "Online Statements",
    "Bill Pay"
]

for page in pages:
    try:
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, page)))
        link.click()
        print(f"✅ Visited: {page}")
        time.sleep(2)  # short pause so page loads
    except Exception as e:
        print(f"❌ Could not click {page}: {e}")

# Save screenshot
driver.save_screenshot("demo_testfire_result.png")

# Close browser
driver.quit()
