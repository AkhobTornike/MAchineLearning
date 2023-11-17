from scrapy.http import TextResponse
import pandas as pd
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/91.0.4472.124 Safari/537.36'
}

url = requests.get("https://www.myhome.ge/ka/s/?Keyword=%E1%83%97%E1%83%91%E1%83%98%E1%83%9A%E1%83%98%E1%83%"
                   "A1%E1%83%98&AdTypeID=1&cities=1996871&GID=1996871", headers=headers)
resources = TextResponse(url.url, body=url.text, encoding='utf-8')

links = resources.css("a.card-container::attr(href)").getall()

price = []
area = []
rooms = []
bedrooms = []
floor = []
district = []

for link in links:
    linked_url = requests.get(link, headers=headers)
    linked_resources = TextResponse(linked_url.url, body=linked_url.text, encoding='utf-8')
    span_price = linked_resources.css("span.d-block.convertable[data-price-gel]::attr(data-price-gel)").extract_first()
    price.append(span_price)
    addresses = linked_resources.css("span.address::text").extract()
    districts = addresses[0].strip().split(',', 2)
    if any(char.isdigit() for char in districts[0].strip()) and any(char.isalpha() for char in districts[0].strip()):
        district.append(districts[0].strip())
    else:
        district.append(districts[0].strip() + ' ' + districts[1].strip())

    info = linked_resources.css("div.main-features.row.no-gutters div div span::text").extract()
    if len(info) == 6:
        area.append(info[0])
        rooms.append(info[1])
        bedrooms.append(info[2])
        floor.append(info[4].strip().split()[0])
    else:
        area.append(info[0])
        rooms.append('NaN')
        bedrooms.append('NaN')
        floor.append('NaN')


data = {
    'Price': price,
    'Area': area,
    'Rooms': rooms,
    'Bedrooms': bedrooms,
    'Floor': floor,
    'District': district
}

df = pd.DataFrame(data)
with pd.ExcelWriter('myhomeScrapy.xlsx') as writer:
    df.to_excel(writer, index=True)
