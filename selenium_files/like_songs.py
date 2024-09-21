from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://accounts.spotify.com/en/login")

# Log in to Spotify
username = driver.find_element(By.ID, "login-username")
password = driver.find_element(By.ID, "login-password")
username.send_keys("akzaidi@usf.edu")
password.send_keys("Jamal714!?")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()


# Open the URL
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
# Time the chrome gonna be appear, in this case 40 seconds

# Navigate to the playlist
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

time.sleep(10)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the text file with the song list
with open("../text_files/list_songs.txt", "r") as fr:
    for song in fr:
        # Locate the search bar, type the song name, and press Enter
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='search-input']"))
        )
        search_bar.send_keys(song.strip())  # Use strip() to remove extra spaces or newlines
        search_bar.send_keys(u'\ue007')  # Press Enter
        print(f"Searching for song: {song.strip()}")

        # Wait for results to load
        time.sleep(5)

        try:
            # Locate the Like button
            print("Checking if song is already liked...")
            like_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Add to Liked Songs']"))
            )

            # Check the `aria-checked` attribute to determine if the song is already liked
            is_liked = like_button.get_attribute("aria-checked") == "true"

            if is_liked:
                print(f"Song '{song.strip()}' is already liked, skipping.")
            else:
                print(f"Song '{song.strip()}' is not liked, liking it now...")

                # Scroll the button into view
                driver.execute_script("arguments[0].scrollIntoView();", like_button)
                time.sleep(1)  # Give it a moment to scroll

                # Click the Like button via JavaScript to bypass click interception
                print(())
                driver.execute_script("arguments[0].click();", like_button)
                print("Clicked the Like button via JavaScript.")

        except Exception as e:
            print(f"Error processing song '{song.strip()}': {e}")

        # Wait to see the action
        time.sleep(3)

        # Clear the search bar by clicking the "X" button
        clear_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Clear search field']"))
        )
        clear_button.click()
        print("Cleared the search field.")

        # Wait before processing the next song
        time.sleep(2)
