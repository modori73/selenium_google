from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.relative_locator import with_tag_name
import time

URL = 'https://dart.fss.or.kr/report/viewer.do?rcpNo=20220817000059&dcmNo=8775996&eleId=20&offset=156514&length=25881&dtd=dart3.xsd'

driver = webdriver.Chrome(executable_path='C:\\GitHub\\Test\\selenium_google\\Scrapping\\chromedriver')
driver.implicitly_wait(time_to_wait=5)
driver.get(url=URL)


menu_balanceSheet = driver.find_element(By.XPATH,'/html/body/table[1]')
print(menu_balanceSheet.text)

driver.close()




