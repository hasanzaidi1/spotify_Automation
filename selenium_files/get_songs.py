
from selenium import webdriver # Webdriver is used to control the browser (open, click button, fill information), example of web brower: Chrome, Firefox, Safari, Edge
from selenium.webdriver.chrome.service import Service as ChromeService # In this case we use the Chrome Service
from selenium.webdriver.common.by import By # By is used to locate elements on the page, for example, when you inspect any webbrower, you can see the elements on the page (html code), and a block of code will have id or class to classifies them(example: class="list-group-item")

import time # Time is used to give time to the chrome to appear

driver = webdriver.Chrome()

#Open the URL
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
#Time the chrome gonna be appear, in this case 40 seconds

time.sleep(40)



event_items = driver.find_elements(By.CLASS_NAME, "btE2c3IKaOXZ4VNAb8WQ")


# Open the text file in write mode
with open("../text_files/list_songs.txt", "w") as f:
    for item in event_items:
        f.write(item.text+'\n')
        print(item)



