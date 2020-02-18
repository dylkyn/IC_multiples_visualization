from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.direxion.com/etfs")
soup = BeautifulSoup(page.content, "html.parser")
funds = soup.find_all("option")
tickers = []
for i in funds:
	if len(i)>0:
		tickers.append(i.text.split()[0])
print(tickers)


	