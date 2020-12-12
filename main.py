from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


print(' Created By SUSHANT DHIMAN '.center(80, '*'))
time.sleep(1)
print('Follow on Instagram = @sushantdhiman2004'.center(80))
time.sleep(1)
print(''.center(80, '*'))
print('')

print('Website Screenshot Capture'.center(80))


site_link = input("Enter Site Link (Example = google.com) : ")


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://" + site_link)
print("Taking Screenshot Of" + " " + site_link)
time.sleep(1)
driver.get_screenshot_as_file(site_link + ".png")
time.sleep(1)
print("Screenshot Successfully Taken")
driver.quit()