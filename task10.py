from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# Set up the WebDriver (you can change this to Firefox or Edge if needed)
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

# Maximize window (optional)
driver.maximize_window()


# Get and print the page title and URL
print("Page Title:", driver.title)
print("Page URL:", driver.current_url)

# Get the page source (entire HTML content)
html_content = driver.page_source

# Save the content to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Page HTML saved to 'Webpage_task_11.txt'.")


# Find username and password fields and enter credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click the login button
driver.find_element(By.ID, "login-button").click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Optional: close the browser
driver.quit()

def test_positive_login(driver):
    driver.get("https://www.saucedemo.com")

    # Title and URL before login
    assert driver.title == "Swag Labs"
    assert driver.current_url == "https://www.saucedemo.com/"

    # Valid login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # After login
    expected_dashboard_url = "https://www.saucedemo.com"
    expected_title = "Swag Labs"
    assert driver.current_url == expected_dashboard_url
    assert driver.title == expected_title
print("✅ Positive test passed: logged in successfully.")
print("✅ Positive test passed: Title is correct.")
print("✅ Positive test passed: URL is correct.")

def test_negative_login(driver):
    driver.get("https://www.saucedemo.com")

    # Title and URL before login
    assert driver.title == "Toner Labs"
    assert driver.current_url == "https://www.google.com/"

    # Invalid login
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Ensure still on login page
    #assert driver.current_url == "https://www.saucedemo.com/"
    expected_dashboard_url = "www.google.com"
    expected_title = "Toner Labs"
    assert driver.current_url == expected_dashboard_url
    assert driver.title == expected_title


    # Check for error message
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error
print("❌ Negative test passed: login failed as expected.")
print("❌ Negative test passed: Error message displayed.")
print("❌ Negative test passed: Title is wrong.")
