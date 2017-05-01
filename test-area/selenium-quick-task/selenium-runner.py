from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

DELAY = 10
RETRIES = 3
browser = webdriver.Chrome()
browser.get("http://mccog.maps.arcgis.com/apps/webappviewer/index.html?id=09bf2f0e07a243ffb262793cf106cd01")

try:
    print "waiting for page to load"
    time.sleep(DELAY)
    print "waiting done"
    okbutton = browser.find_element_by_css_selector("div.jimu-btn.jimu-float-trailing.enable-btn")
    okbutton.click()
    print "-----------------------------"
except Exception as e:
    print "there was a timeout exception at the welcome popup"
    print str(e)

e = browser.find_element_by_id("esri_dijit_Search_0_input")

"----------------------------------------------------------------------------------------------------------"

" this needs to be made to read from file"

e.clear()
e.send_keys("48-08-13-400-024.000-017")
e.send_keys(Keys.RETURN)
time.sleep(DELAY)

l = []
retry = 0
while retry < RETRIES:
    name_table = [x.text for x in browser.find_elements_by_css_selector("td.attrName")]
    value_table = [x.text for x in browser.find_elements_by_css_selector("td.attrValue")]
    if len(name_table[0]) < 1 or len(value_table[0]) < 1:
        print "retrying since no elements were found"
        retry += 1
        continue
    else:
        zip_table = zip(name_table, value_table)
        retry = 3
        print zip_table




