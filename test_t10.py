import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
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
    expected_dashboard_url = "https://www.saucedemo.com/inventory.html"
    expected_title = "Swag Labs"
    html_content = driver.page_source
    # Save it as an .txt file (which you can open later in any browser)
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(html_content)
    assert driver.current_url == expected_dashboard_url
    assert driver.title == expected_title

    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)
    print("✅ Positive test passed: logged in successfully.")


def test_negative_login(driver):
    driver.get("https://www.saucedemo.com")

    # Title and URL before login
    assert driver.title == "Swag Labs"
    assert driver.current_url == "https://www.saucedemo.com/"

    # ❌ Invalid login attempt
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Capture HTML content
    html_content = driver.page_source
    with open("Webpage_task_11_negative.txt", "w", encoding="utf-8") as file:
        file.write(html_content)

    # Still on the login page
    assert driver.current_url == "https://www.saucedemo.com/"
    assert driver.title == "Swag Labs"

    # Check for error message
    error_text = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_text

    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)
    print("❌ Negative test passed: login failed as expected.")


   