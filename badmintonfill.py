# you should do pip install selenium before import
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

##############################################################################
# All information needed to register are below
# the two array stands for 4 courts in 19:45 and 21:00, select the timeslot you want
# the program monitor all vacancy in 4 courts and register once available
courtlocation_array_1945 = ['//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[9]/td[4]/input',
'//*[@id="bs_pl3FE6C9AEA6F8"]/tbody/tr[9]/td[4]/input',
'//*[@id="bs_pl3FE6C9AE4851"]/tbody/tr[9]/td[4]/input',
'//*[@id="bs_pl3FE6C94D4C08"]/tbody/tr[9]/td[4]/input'
]

courtlocation_array_2100 = ['//*[@id="bs_pl3FE6C936AAFC"]/tbody/tr[10]/td[4]/input',
'//*[@id="bs_pl3FE6C9AEA6F8"]/tbody/tr[10]/td[4]/input',
'//*[@id="bs_pl3FE6C9AE4851"]/tbody/tr[10]/td[4]/input',
'//*[@id="bs_pl3FE6C94D4C08"]/tbody/tr[10]/td[4]/input'
]
# select the court and define courtlocation_array = xxx below!

# MODIFY (and UNCOMMENT) below input lines before you run the programm!
courtlocation_array = courtlocation_array_1945
chromedriverpath = 'D:\ChromeDownloads\chromedriver_win32\chromedriver.exe'
sex = 'male' # define sex = 'female' if needed!
vorname = 'Yukun'
name = 'Cao'
address = 'Melatener strasse 159A'
city = '52074 Aachen'
stuID = '384159'
tel = '015201095257'
email = 'caoyukunk9999@126.com'
card = 'DE81390500001073070938'
##############################################################################

# download the chromedriver.exe https://sites.google.com/a/chromium.org/chromedriver/downloads
# and put the file path here, NOT USE your local chrome.exe!!!
driver = webdriver.Chrome(chromedriverpath)

driver.get('https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Badmintoncourt_Einzelterminbuchung.html')
# tested with volleyball booking url
# driver.get('https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Beachvolleyballplatz_Einzelterminbuchung.html')
# courtlocation = '//*[@id="bs_pl3FE63E5FAFBB"]/tbody/tr[10]/td[3]/input'
# courtlocation_array = ['//*[@id="bs_pl3FE6C94D4C08"]/tbody/tr[7]/td[4]/input', '//*[@id="bs_pl3FE6C9AE4851"]/tbody/tr[7]/td[4]/input', '//*[@id="bs_pl3FE6C94D4C08"]/tbody/tr[5]/td[4]/input']

for i in range(0, len(courtlocation_array)):
    # it keeps refreshing the page until the buchen button is green
    while True:
        try:
            driver.find_element_by_xpath(courtlocation_array[i])
            break
        except:
            driver.refresh
    driver.find_element_by_xpath(courtlocation_array[i]).click()

    # # important to switch your driver to NEW page opened! otherwise location fails
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    # x-path location of buchen/wartelist in https://buchung.hsz.rwth-aachen.de/cgi/anmeldung.fcgi
    driver.find_element_by_xpath('//*[@id="bs_form_main"]/div/div[2]/div[1]/label/div[2]/input').click()

    # # important to switch your driver to NEW page opened! otherwise location fails
    window_after2 = driver.window_handles[-1]
    driver.switch_to.window(window_after2)
    # HERE WE WILL FILL IN ALL INFORMATION
    if sex == 'male':
        sexloc = '//*[@id="bs_kl_anm"]/div[3]/div[2]/label[2]/input'
    elif sex == 'female':
        sexloc = '//*[@id="bs_kl_anm"]/div[3]/div[2]/label[1]/input'
    try:
        driver.find_element_by_xpath(sexloc)
    except:
        print("occupied")
        driver.close()
        driver.switch_to.window(window_before)
        continue

    selectstuloc = '//*[@id="BS_F1600"]'
    vornameloc = '//*[@id="BS_F1100"]'
    nameloc = '//*[@id="BS_F1200"]'
    addressloc = '//*[@id="BS_F1300"]'
    cityloc = '//*[@id="BS_F1400"]'
    stuIDloc = '//*[@id="BS_F1700"]'
    telloc = '//*[@id="BS_F2100"]'
    emailloc = '//*[@id="BS_F2000"]'
    cardloc = '//*[@id="BS_F_iban"]'
    agreeboxloc = '//*[@id="bs_bed"]/label/input'

    # select your sex
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
    driver.find_element_by_xpath(emailloc).send_keys(email)
    driver.find_element_by_xpath(telloc).send_keys(tel)
    driver.find_element_by_xpath(cardloc).send_keys(card)

    # check the agree box
    driver.find_element_by_xpath(agreeboxloc).click()

# # click the weiter button
driver.find_element_by_xpath('//*[@id="bs_foot"]/div[3]/div[2]/input').click()

# # remember there is a info confirmation page to click
# # driver.find_element_by_xpath('//*[@id="bs_foot"]/div[1]/div[2]/input').click()