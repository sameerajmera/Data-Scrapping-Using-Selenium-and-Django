# Using beautifulsoup

import requests
import bs4 import BeautifulSoup
url = 'https://dsscic.nic.in/cause-list-report-web/registry_cause_list/1?page_length=all&fromdate=01%2F05%2F2019&todate=23%2F10%2F2020&commissionname=8539&seach_type=public_authority&search_text='
page = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
table = soup.find_all('table')
table =table[0]
table_rows=table.find_all('tr')
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
df = pd.DataFrame(l, columns=['Sl.No.', 'File No.', 'Name Of Appellant/Complainant', 'IC Name','Public Authority', 'Date of Hearing', 'Time of Hearing',
       'Bench Details', 'Action'])
df = df.iloc[2:]
df=df.replace({'\n': ''}, regex=True)
df=df.replace({'\t': ''}, regex=True)
df



*******************************************************************************************************************************************************

#Using pandas library
import pandas as pd
url = 'https://dsscic.nic.in/cause-list-report-web/registry_cause_list/1?page_length=all&fromdate=01%2F05%2F2019&todate=23%2F10%2F2020&commissionname=8539&seach_type=public_authority&search_text='
df_list = pd.read_html(url)
final_df = df_list[0]
final_df.columns = final_df.columns.droplevel()
final_df

