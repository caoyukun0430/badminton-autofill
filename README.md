This is Yukun's script to book badminton automatically in https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Badmintoncourt_Einzelterminbuchung.html

NOTE: ONLY USE IT IN CASE YOU CAN NOT MANUALLY GET A PLACE LIKE ME!!! :(

The programm will refresh and monitor vacancy of all 4 courts, once avilable, it register.
In case the court is register, it goes to the next one!

You need to preinstall python and selenium package before using the script
* To install python on windows: https://www.python.org/downloads/
* To install selenium: run 'pip install selenium'

NOTE: as I commented, you need to download the chromedriver.exe that MATCHES your chrome version on windows
from https://sites.google.com/a/chromium.org/chromedriver/downloads
and put the file path here.

DO NOT USE your local chrome.exe PATH !!!

To run the program, simply fulfill all asked infomation in badmintonfill.py and type 'python badmintonfill.py' in your terminal.

ONLY REMAINING BUG: the last two confirm buttom can't not be automated with click, so you HAVE TO CLICK MANUALLY!!!