from scrapy.http import TextResponse
import requests
import pandas as pd

url = requests.get("https://home.ss.ge/ka/udzravi-qoneba/l/bina/iyideba?cityIdList=95&currencyId=1")

resources = TextResponse(url.url, body=url.text, encoding='utf-8')

links = resources.css("div.sc-b11955d3-0.dpQqCX a::attr(href)").getall()

price = []
area = []
rooms = []
bedrooms = []
floor = []
district = []

for i in range(0, len(links), 15):
    link = links[i]
    linked_url = requests.get("https://home.ss.ge/" + link)
    linked_resources = TextResponse(linked_url.url, body=linked_url.text, encoding='utf-8')
    prices = linked_resources.css("h2.sc-6e54cb25-1.foFfic::text").extract()
    infos = linked_resources.css("h5.sc-6e54cb25-4.kjoKdz::text").extract()
    districts = linked_resources.css("p.sc-e48984a1-10.hSPoNA::text").extract()
    if len(prices) != 0 and infos != 0 and len(districts) != 0:
        price.append(prices[0] + prices[1])
        area.append(infos[0])
        rooms.append(infos[1])
        bedrooms.append(infos[2])
        floor.append((infos[3]))
        district.append(districts[1])

data = {
    'price': price,
    'area': area,
    'rooms': rooms,
    'bedrooms': bedrooms,
    'floor': floor,
    'district': district
}

df = pd.DataFrame(data)
with pd.ExcelWriter('ssScrapy.xlsx') as writer:
    df.to_excel(writer, index=True)
