import re
import time
import pyautogui
import requests
from bs4 import BeautifulSoup
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Make browser open in background
options = Options()
options.add_experimental_option("detach", True)

# Create the webdriver object
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Obtain the Google Map URL
url = "https://www.google.com/maps/search/it+company+in+textas/@38.315379,-171.3556447,3z?entry=ttu"

# Open the Google Map URL,
browser.get(url)
browser.maximize_window()
time.sleep(6)

screen_width, screen_height = pyautogui.size()
count_time = 700

# Move the mouse cursor to the center left of the screen
pyautogui.moveTo(screen_width / 4, screen_height / 2)
while count_time:
    pyautogui.scroll(-50)
    time.sleep(0.5)
    count_time -= 1

links = browser.find_elements("xpath", "//div[contains(@class, 'qBF1Pd fontHeadlineSmall')]")
organization_tags = browser.find_elements("xpath", "//a[contains(@class, 'lcr4fd S9kvJb')]")
addresses = browser.find_elements("xpath",
                                  "//div[contains(@class, 'W4Efsd')]//div[contains(@class, 'W4Efsd')]//span[2]//span")


# The organization names, website, address will stored in the list below
organization_name = []
organization_url = []
organization_address = []
organization_map_info_link = []
adr = 1
no = 3


# the function finds the email address form the organization website
def find_email(url_email):
    # i stored the emails in a set instead of a list so i don't stored duplicate.
    emails = set()
    try:
        html_text = requests.get(url_email).text
        soup = BeautifulSoup(html_text, 'lxml')
        emails = set()

        # Find the email address in the footer section
        footer_section = soup.find_all('footer')
        for fs in footer_section:
            email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', str(fs))
            for email in email_list:
                emails.add(email)

        # Find the email address in the footer section (div with id "footer")
        footer_section_attrs = soup.find_all(attrs={'id': 'footer'})
        for fsa in footer_section_attrs:
            email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', str(fsa))
            for email in email_list:
                emails.add(email)

        if not emails:

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url_email)
            time.sleep(15)

            # get the HTML of the website and find the emails
            page_source = driver.page_source

            email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', page_source)
            for email in email_list:
                emails.add(email)

            driver.quit()

        return emails

    except:

        try:

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url_email)
            time.sleep(10)

            # get the HTML of the website and find the emails
            page_source = driver.page_source

            email_list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', page_source)
            for email in email_list:
                emails.add(email)
            driver.quit()
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")

        return emails


for link in links:
    organization_name.append(link.text)
for tag in organization_tags:
    organization_url.append(tag.get_attribute("href"))
for address in addresses:
    organization_address.append(address.text)

with open('Organizations.txt', 'w',  encoding='utf-8') as f:
    for i in range(len(organization_name)):
        org_email = find_email(organization_url[i])
        print(f'{i + 1}).\n')
        print(f'Organization Name: {organization_name[i]}')
        print(f'Organization Website: {organization_url[i]}')
        print(f'Organization Email: {org_email}')
        f.write(f'{i + 1}).\n')
        f.write(f'Organization Name: {organization_name[i]}\n')
        f.write(f'Organization Website: {organization_url[i]}\n')
        f.write(f'Organization Email: {org_email}\n')
        if adr < len(organization_address) and no < len(organization_address):
            print(f'Organization Address: {organization_address[adr]}')
            print(f'Organization Phone Number: {organization_address[no]}\n')
            f.write(f'Organization Address: {organization_address[adr]}\n')
            f.write(f'Organization Phone Number: {organization_address[no]}\n\n')
            adr += 4
            no += 4

# initialize pygame
pygame.mixer.init()

# load the music file
sound_file_path = "../../Downloads/biohazard-alarm-143105.mp3"
pygame.mixer.music.load(sound_file_path)

# play the music
pygame.mixer.music.play()

# wait for the music to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

