from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Instagram's login page
driver.get("https://www.instagram.com/accounts/login/")

# Enter your Instagram username and password
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Navigate to the Direct Messages page
driver.get("https://www.instagram.com/direct/inbox/")

# Function to send auto-reply
def send_auto_reply(message):
    message_box = driver.find_element(By.TAG_NAME, "textarea")
    message_box.send_keys(f"Thank you for your message! We will get back to you as soon as possible.")
    message_box.send_keys(Keys.RETURN)

# Check for new messages and send auto-reply
while True:
    try:
        # Find the list of message threads
        threads = driver.find_elements(By.CLASS_NAME, "-qQT3")

        # Iterate through each thread
        for thread in threads:
            # Check if the thread has an unread message
            unread_indicator = thread.find_elements(By.CLASS_NAME, "_ab8w")
            if unread_indicator:
                # Open the message thread
                thread.click()
                time.sleep(2)

                # Send the auto-reply
                send_auto_reply("Auto-reply message")

                # Go back to the inbox
                driver.get("https://www.instagram.com/direct/inbox/")

    except Exception as e:
        print(f"Error: {e}")
        break

    time.sleep(10)  # Wait for 10 seconds before checking again