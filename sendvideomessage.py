import pywhatkit as kit

# Include the country code along with the phone number
number = '+919848586640'

# Schedule a text message to be sent at 3:15 PM
kit.sendwhatmsg(number, 'Hello, check out this video!', 15, 46)

# After the text message is sent, wait for a few seconds to ensure it's delivered
import time
time.sleep(10)  # You can adjust the sleep duration as needed

# Specify the path to the video file you want to send (use a raw string)
video_path = r'C:\Users\saigu\OneDrive\Desktop\V_20230902_152043_ES6.mp4'

# Send the video as a separate step
kit.sendwhatmsg(number, video_path, 15, 47)  # Send the video at 3:16 PM
