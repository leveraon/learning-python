from bs4 import BeautifulSoup
import scrapy
import json


class TariffItemSpider(scrapy.Spider):
    name = "tariff_items"
    target_html = '' 

    with open("crawling/mock_data/tariff.html") as fp:
        target_html = BeautifulSoup(fp, 'html.parser')       
    
    table = target_html.find('table')    
    rows = table.find_all('tr')
    tariff_items = []
    
    for row in rows:
        headers = row.find_all('th')
        item_id = [header.text.strip() for header in headers]
        cols = row.find_all('td')
        item_data = [col.text.strip() for col in cols]
        tariff_items.append({
            'id': item_id[0],
            'name': item_data[0],
            'description': item_data[1],
        })
        
    with open('tariff_items.json', 'w') as file:
        json.dump(tariff_items, file, indent=4)    