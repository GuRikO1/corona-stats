from bs4 import BeautifulSoup
import pandas as pd
import requests

pd.set_option('display.max_rows', 500)

url = "https://www.worldometers.info/coronavirus/"
soup = BeautifulSoup(requests.get(url).content,'html.parser')
print(soup)
tag_tr = soup.find_all('tr')
head = [h.text for h in tag_tr[0].find_all('th')]

pre_data = []
flag = False
for i in range(1,len(tag_tr)):
    pre_data.append([d.text for d in tag_tr[i].find_all('td')])

data = []
for d in pre_data:
    if (d == []):
        break
    data.append(d)
df = pd.DataFrame(data, columns = head)
for h in head:
    df[h] = df[h].str.replace(",", "")
    df[h] = df[h].str.replace("+", "")
for h in head[1:10]:    
    df[h] = pd.to_numeric(df[h], errors='coerce')

df_s = df.sort_values('TotalCases', ascending=False)
#print(df_s)