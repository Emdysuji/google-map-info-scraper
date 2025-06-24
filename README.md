# google-map-info-scraper

**Google Map Info Scraper** is a Python automation script that extracts business data such as organization names, websites, email addresses, and physical addresses from Google Maps search results. It combines the power of **Selenium**, **BeautifulSoup**, **PyAutoGUI**, and **Requests** to collect and store company contact details automatically.

---

## 🚀 Features

- 🌐 Extracts company names, websites, and addresses from Google Maps search results
- 📧 Attempts to discover email addresses by crawling official websites
- 🖱️ Uses PyAutoGUI to scroll through map listings for dynamic content loading
- 💾 Saves extracted data to a `.txt` file
- 🔊 Optional alarm sound when scraping is complete (via `pygame`)

---

## 🛠️ Tech Stack

- `Python 3.x`
- `Selenium`
- `PyAutoGUI`
- `BeautifulSoup`
- `Requests`
- `Pygame`
- `ChromeDriver`

---

## 📦 Installation

1. Make sure **Google Chrome** is installed on your system.
2. Install the required Python packages:

```bash
pip install selenium beautifulsoup4 pygame requests pyautogui webdriver-manager
```

# 🧪 How to Use
1. Clone the repository:
```
git clone https://github.com/yourusername/google-map-info-scraper.git
cd google-map-info-scraper
```

2. Customize the script if needed:
    - Modify the Google Maps URL to match your desired search (e.g., IT companies in Texas).
    - Adjust element selectors if Google Maps layout changes.

3. Run the script:
```
python map_scraper.py
```
4. The script will:
    - Open Chrome
    - Load Google Maps
    - Scroll through business listings
    - Extract organization names, addresses, websites, and emails
    - Save everything to Organizations.txt

# 📁 Output
The script outputs a file called:
```
Organizations.txt
```
Each entry contains:
- Organization Name
- Website
- Email (if found)
- Address
- Phone Number (if found)

Look up ```sample_output.txt``` on how it is displayed 

# 🔔 Optional: Add Alert Sound
To get an alert when scraping finishes:
1. Download a .mp3 file (e.g., alarm) to your system.
2. Update the path in the script:
```
sound_file_path = "path/to/your/alarm.mp3"
```
# ⚠️ Disclaimer
Web scraping Google Maps may violate their terms of service. Use responsibly and for educational purposes only.

Layout changes on Google Maps may break the script in the future.

# 🙌 Author
*Michael-David Osuji*
- 📍 Nigeria
- 💼 Machine Learning & Automation Enthusiast
- 🌐 LinkedIn (www.linkedin.com/in/michael-daivd-osuji-b1811a208)
- 📬 Feel free to connect or contribute!

# ⭐️ Show Your Support
If you like this project, give it a ⭐️ on GitHub and share it with others!
