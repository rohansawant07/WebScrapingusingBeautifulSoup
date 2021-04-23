import requests
import re
import csv
from bs4 import BeautifulSoup


page = requests.get('https://www.brownells.com/rifle-parts/bolt-parts/bolt-carrier-parts/bolt-carriers/m16-sand-cutter-bolt-carrier-prod118544.aspx')

f = csv.writer(open('product-names.csv', 'w'))
f.writerow(['Name', 'Status','URL'])
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


rows= soup.find('div', class_="media group1")

rows_items= rows.find('div',class_="bd")



name= rows_items.text

print(name)


rows2= soup.find('div', class_="media group2")

rows2_items= rows2.find('div',class_='status')



status= rows2_items.text 
print(status)
x= re.search("unavailable+",status)
print (x)
if x:
    status="Out of Stock"

print(status)

f.writerow([name,status,'https://www.brownells.com/rifle-parts/bolt-parts/bolt-carrier-parts/bolt-carriers/m16-sand-cutter-bolt-carrier-prod118544.aspx' ])




