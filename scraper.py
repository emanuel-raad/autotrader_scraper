from lxml import html
import requests
import numpy as np
import csv

fl = open('jetta.csv', 'wb')
writer = csv.writer(fl)
writer.writerow(['mileage', 'price'])

link_dart = "http://www.autotrader.ca/cars/dodge/dart/on/etobicoke/?prx=100&prv=Ontario&loc=M9C+5J1&trans=Automatic&fuel=Gasoline&sts=New-Used&yRng=%2c2014&hprc=True&wcp=True&inMarket=advancedSearch&rcs=0&rcp=100"
link_jetta = "http://www.autotrader.ca/cars/volkswagen/jetta/on/etobicoke/?prx=100&prv=Ontario&loc=M9C+5J1&trans=Automatic&fuel=Gasoline&sts=New-Used&yRng=%2c2014&hprc=True&wcp=True&inMarket=advancedSearch&rcs=0&rcp=100&srt=9"
link_civic = "http://www.autotrader.ca/cars/honda/civic/on/etobicoke/?prx=100&prv=Ontario&loc=M9C+5J1&trans=Automatic&fuel=Gasoline&sts=New-Used&yRng=2008%2c2014&hprc=True&wcp=True&inMarket=advancedSearch"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# page = requests.get(link_civic, headers=headers)
# tree = html.fromstring(page.content)

with open('jetta.txt', 'r') as myfile:
    page = myfile.read()

tree = html.fromstring(page)

mileage = tree.xpath('//div[@class="at_km"]/text()')
price = tree.xpath('//div[@class="at_price"]/text()')
price = price[1::2]

mileage_filtered = np.empty((len(mileage)))
price_filtered = np.empty((len(mileage)))

for i in range(0, len(mileage)):
    mileage_filtered[i] = int(filter(str.isdigit, mileage[i]))
    price_filtered[i] = int(filter(str.isdigit, price[i]))
    writer.writerow([mileage_filtered[i], price_filtered[i]])
    #print("{}\t{}").format(mileage_filtered[i], price_filtered[i])

fl.close()