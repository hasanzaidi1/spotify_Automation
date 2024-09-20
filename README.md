# Spotify Song Liker

This Python script uses Selenium to automate the process of liking songs on a Spotify playlist. It reads song titles from a text file and searches for each song on Spotify, clicking the "like" button for each one.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install Selenium using pip:
   ```bash
   pip install selenium
   ```
3. Download the appropriate Chrome WebDriver for your version of Chrome from [ChromeDriver](https://sites.google.com/chromium.org/driver/).
4. Place the ChromeDriver executable in a directory that is in your system's PATH, or specify the path in the script.

## Usage

1. Create a text file named `list_songs.txt` in the `text_files` directory (relative to your script) and list the song titles you want to like, one per line.
2. Modify the scripts to ensure the correct CSS selectors are used for the Spotify elements (search bar and like button).
3. Run the scripts in the following order:
   ```bash
   python get_songs.py
   python like_songs.py
   ```

## Code Explanation

### 1. `get_songs.py`

This script retrieves the list of songs from the Spotify playlist page and saves them to a text file.

```python
from selenium import webdriver  # Webdriver is used to control the browser (open, click button, fill information), example of web browser: Chrome, Firefox, Safari, Edge
from selenium.webdriver.common.by import By  # By is used to locate elements on the page
import time  # Time is used to give time to the chrome to appear

driver = webdriver.Chrome()

# Open the URL
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
# Time for the Chrome to appear, in this case 40 seconds
time.sleep(40)

event_items = driver.find_elements(By.CLASS_NAME, "btE2c3IKaOXZ4VNAb8WQ")

# Open the text file in write mode
with open("../text_files/list_songs.txt", "w") as f:
    for item in event_items:
        f.write(item.text + '\n')
        print(item)
```

**Explanation:**
- This script opens the specified Spotify playlist URL and waits for 40 seconds to allow the page to fully load.
- It then finds the song elements using their class name and writes the song titles into `list_songs.txt`.

### 2. `like_songs.py`

This script reads the song titles from the text file and likes each song on Spotify.

```python
from selenium import webdriver  # Webdriver is used to control the browser
from selenium.webdriver.common.by import By  # By is used to locate elements on the page
import time

driver = webdriver.Chrome()
# Open the URL
driver.get("https://open.spotify.com/playlist/6nZJDrkwViKpyEbYfLtVz1")
# Time the chrome gonna be appear, in this case 40 seconds
time.sleep(40)

with open("../text_files/list_songs.txt", "r") as fr:
    for song in fr:
        # Locate the search bar (use your search bar's actual class or id)
        search_bar = driver.find_element(By.CSS_SELECTOR, "input[data-testid='search-input']")

        # Type into the search bar
        search_bar.send_keys(song.strip())  # Strip whitespace/newline

        # Press Enter after typing (optional, depending on what the search needs)
        search_bar.send_keys(u'\ue007')  # This simulates the "Enter" key

        # Wait for results to load (adjust time as needed)
        time.sleep(5)

        # Locate and click the "Like" button
        like_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Save to Your Library']")
        like_button.click()

        # Wait to see the action
        time.sleep(3)

        # Clear the search bar for the next song
        search_bar.send_keys("")
```

**Explanation:**
- This script opens the Spotify playlist URL and waits for 40 seconds.
- It reads the song titles from `list_songs.txt`, searches for each song in the search bar, and clicks the "like" button for each one.

## Important Notes

- Make sure you're logged into your Spotify account before running the scripts.
- Adjust the `time.sleep()` calls based on your internet speed and how quickly the Spotify interface loads.
- The selectors used in the scripts (for the search bar and like button) may change over time; ensure they are up-to-date by inspecting the Spotify web page.

## Disclaimer

This script is for educational purposes only. Use it responsibly and ensure compliance with Spotify's terms of service.
