
from selenium import webdriver # Webdriver is used to control the browser (open, click button, fill information), example of web brower: Chrome, Firefox, Safari, Edge
from selenium.webdriver.chrome.service import Service as ChromeService # In this case we use the Chrome Service
from selenium.webdriver.common.by import By # By is used to locate elements on the page, for example, when you inspect any webbrower, you can see the elements on the page (html code), and a block of code will have id or class to classifies them(example: class="list-group-item")
import time
driver = webdriver.Chrome()
#Open the URL
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
#Time the chrome gonna be appear, in this case 40 seconds


with open("../text_files/list_songs.txt", "r") as fr:
    for song in fr:
        # Locate the search bar (use your search bar's actual class or id)
        search_bar = driver.find_element(By.CSS_SELECTOR, "input[data-testid='search-input']")

        # Type into the search bar
        search_bar.send_keys(song)

        # Press Enter after typing (optional, depending on what the search needs)
        search_bar.send_keys(u'\ue007')  # This simulates the "Enter" key

        # Wait for results to load (adjust time as needed)
        time.sleep(5)

        # You may need to inspect Spotify's webpage to find the correct class or id for the like button
        like_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Save to Your Library']")

        # Click the "Like" button
        like_button.click()





        # Wait to see the action
        time.sleep(3)

        search_bar.send_keys("")

