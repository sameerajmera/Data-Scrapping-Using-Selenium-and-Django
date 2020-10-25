import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrapFunct():
#code for scrapping data using beautifulsoup and selenium web driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://dsscic.nic.in/cause-list-report-web/registry_cause_list/")
    driver.find_element_by_xpath("//input[@value='appCom']").click()
    driver.find_element_by_xpath("//select[@name='commissionname']/option[text()='Yashvardhan Kumar Sinha']").click()
    driver.find_element_by_xpath("//select[@name='seach_type']/option[text()='Public Authority']").click()
    #driver.find_element_by_xpath("//input[@class='input-group' and @id='datetimepicker1']").send_keys("01/05/2019")
    driver.find_element_by_id('fromdate').send_keys("01/05/2019")
    driver.find_element_by_id('todate').send_keys("23/10/2020")
    driver.find_element_by_xpath("//button[@id='search_button']").click()
    driver.find_element_by_xpath("//select[@name='page_length']/option[text()='All']").click()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    table = soup.find_all('table')
    table =table[0]
    table_rows=table.find_all('tr')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
    df = pd.DataFrame(l, columns=['Sl.No.', 'File No.', 'Name Of Appellant/Complainant', 'IC Name',
        'Public Authority', 'Date of Hearing', 'Time of Hearing',
        'Bench Details', 'Action'])
    df = df.iloc[2:]
    df = df.replace({'\n': ''}, regex=True)
    df = df.replace({'\t': ''}, regex=True)
    df = df.reset_index().drop('index',axis=1)
    return df