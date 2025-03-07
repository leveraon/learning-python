from bs4 import BeautifulSoup
import scrapy
import json


class EquityHoldersSpider(scrapy.Spider):
    name = "equity_holders"
    target_html = '' 

    with open("crawling/mock_data/gddy.html") as fp:
        target_html = BeautifulSoup(fp, 'html.parser')       
    
    table = target_html.find('table')    
    rows = table.find_all('tr')
    tariff_items = []
    
    for row in rows:
        cols = row.find_all('td')
        item_data = [col.text.strip() for col in cols]
        tariff_items.append({
            'holder': item_data[0],
            'share': item_data[1],
            'date': item_data[2],
            'percentage': item_data[3],
            'value': item_data[4],
        })
        
    with open('equity_holders.json', 'w') as file:
        json.dump(tariff_items, file, indent=4)    