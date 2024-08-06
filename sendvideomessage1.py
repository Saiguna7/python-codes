from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver without specifying executable_path
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Rest of your code...

time.sleep(10)  # Wait for the user to scan the QR code or log in

# Find the chat or contact you want to send the video to
search_box = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
search_box.send_keys("Contact Name")  # Replace with the contact's name
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Attach the video file
attach_button = driver.find_element_by_xpath('//div[@title="Attach"]')
attach_button.click()
time.sleep(1)

video_input = driver.find_element_by_xpath('//input[@accept="video/*,video/heif"]')
video_input.send_keys("C:/Users/saigu/OneDrive/Desktop/V_20230902_152043_ES6.mp4")
 # Replace with the video file path

# Send the video
send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()

# Close the browser
driver.quit()
