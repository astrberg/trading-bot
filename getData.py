#!/usr/bin/python3 
from bs4 import BeautifulSoup
from datetime import date
import requests
import csv
import sys

with open("../data/stock-data/{}.csv".format(date.today()), "w") as f:
	header = ['Aktie', '%', '+/-', 'Köp', 'Sälj', 'Senast', 'Högst', 'Lägst', 'Volym', 'Tid']
	writer = csv.DictWriter(f, fieldnames=header)
	writer.writeheader()

	url = 'https://trader.di.se/index.php/stocklist/index/3812?list=7126&searchstring='
	resp = requests.get(url)
	html_page = resp.content
	soup = BeautifulSoup(html_page, 'html.parser')

	for stock in soup.find_all("tr")[2:-1]:
		row = []
		for data in stock.find_all("td"):
			row.append(data.get_text().replace('\n', '').replace(',', '.'))
		mapToDic = dict(zip(header, row))
		writer.writerow(mapToDic)
	

