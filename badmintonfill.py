# you should do pip install selenium before import
from selenium import webdriver
from selenium.webdriver.support.ui import Select

##############################################################################
# All information needed to register are below

# Donnerstag court 3 19:45-20:45 Uhr '//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[9]/td[4]/input'
# Donnerstag court 3 21:00-22:00 Uhr '//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[10]/td[4]/input'
# Donnerstag court 4 19:45-20:45 Uhr '//*[@id="bs_pl3FE6C9AEA6F8"]/tbody/tr[9]/td[4]/input'
# Donnerstag court 4 19:45-20:45 Uhr '//*[@id="bs_pl3FE6C9AEA6F8"]/tbody/tr[10]/td[4]/input'
# select the court and define courtlocation = xxx, e.g.
# courtlocation = '//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[9]/td[4]/input'

# MODIFY and UNCOMMENT below input lines before you run the programm!
courtlocation = '//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[9]/td[4]/input'
chromedriverpath = 'D:\ChromeDownloads\chromedriver_win32\chromedriver.exe'
vorname = 'xxx'
name = 'xxx'
address = 'xxx'
city = 'xxx'
stuID = 'xxx'
tel = 'xxx'
email = 'xxx'
card = 'xxx'
##############################################################################

# download the chromedriver.exe https://sites.google.com/a/chromium.org/chromedriver/downloads
# and put the file path here, NOT USE your local chrome.exe!!!
driver = webdriver.Chrome(chromedriverpath)

driver.get('https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Badmintoncourt_Einzelterminbuchung.html')
# x-path location of the buchen botton in https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Badmintoncourt_Einzelterminbuchung.html
driver.find_element_by_xpath(courtlocation).click()

# # important to switch your driver to NEW page opened! otherwise location fails
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
# x-path location of buchen/wartelist in https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi
driver.find_element_by_xpath('//*[@id="bs_form_main"]/div/div[2]/div[1]/label/div[2]/input').click()

# # important to switch your driver to NEW page opened! otherwise location fails
window_after2 = driver.window_handles[1]
driver.switch_to_window(window_after2)

# HERE WE WILL FILL IN ALL INFORMATION
sexloc = ''
selectstuloc = ''
vornameloc = ''
nameloc = ''
addressloc = ''
cityloc = ''
stuIDloc = ''
telloc = ''
emailloc = ''
cardloc = ''
agreeboxloc = ''

# click the sex button
driver.find_element_by_xpath(sexloc).click()

# select identity to be rwth student so that we can fill in matikel number
s1 = Select(driver.find_element_by_xpath(selectstuloc))
s1.select_by_index(1)

# fill in all infomation
driver.find_element_by_xpath(vornameloc).send_keys(vorname)
driver.find_element_by_xpath(nameloc).send_keys(name)
driver.find_element_by_xpath(addressloc).send_keys(address)
driver.find_element_by_xpath(cityloc).send_keys(city)
driver.find_element_by_xpath(stuIDloc).send_keys(stuID)
driver.find_element_by_xpath(telloc).send_keys(tel)
driver.find_element_by_xpath(emailloc).send_keys(email)
driver.find_element_by_xpath(cardloc).send_keys(card)

# check the agree box
driver.find_element_by_xpath(agreeboxloc).click()

# click the weiter button
driver.find_element_by_xpath('//*[@id="bs_foot"]/div[1]/div[2]/input').click()

# remember there is a info confirmation page to click
driver.find_element_by_xpath('//*[@id="bs_foot"]/div[1]/div[2]/input').click()