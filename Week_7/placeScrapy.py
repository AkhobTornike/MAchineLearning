from scrapy.http import TextResponse
import requests
import pprint
import pandas as pd
import re

url = requests.get("https://place.ge/ge/ads?object_type=flat&mode=list&nearest=0&type=for_sale&condition=&project"
                   "=&agency_id=&city_id=1&region_id=&district_id=&street_id=&commercial_type=&commercial_type2="
                   "&status=&rooms_from=-%E1%83%93%E1%83%90%E1%83%9C&rooms_to=-%E1%83%9B%E1%83%93%E1%83%94&living"
                   "_space_from=-%E1%83%93%E1%83%90%E1%83%9C&living_space_to=-%E1%83%9B%E1%83%93%E1%83%94&price_"
                   "from=-%E1%83%93%E1%83%90%E1%83%9C&price_to=-%E1%83%9B%E1%83%93%E1%83%94&currency_id=1&with_"
                   "photos=0&owner=0")

resources = TextResponse(url.url, body=url.text, encoding='utf-8')
links = resources.css("div.img a::attr(href)").getall()

price = []
area = []
rooms = []
bedrooms = []
floor = []
district = []

pprint.pprint(links)
for link in links:
    if link != '/ge/faq?open=5':
        linked_url = requests.get("https://place.ge" + link)
        linked_resources = TextResponse(linked_url.url, body=linked_url.text, encoding='utf-8')
        prices = linked_resources.css("div.price::text").extract()
        if len(prices) == 1:
            prices = prices[0]
        else:
            prices = prices[1]
        price.append(re.sub(r"[^\d\-+\.]", "", prices[0:30]) + '₾')
        link_info = linked_resources.css("div.detailRight::text").extract()
        if len(link_info) == 6:
            area.append(link_info[0])
            rooms.append(link_info[3])
            bedrooms.append(link_info[5])
            floor.append(link_info[2])
            district.append(link_info[1])
        else:
            area.append(link_info[0])
            rooms.append(link_info[6])
            bedrooms.append(link_info[8])
            floor.append(link_info[5])
            district.append(link_info[4])


# print(f'price {price}')
# print(f'area {area}')
# print(f'rooms {rooms}')
# print(f'bedrooms {bedrooms}'
# print(f'floor {floor}')
# print(f'district {district}')

data = {
    'Price': price,
    'Area': area,
    'Rooms': rooms,
    'Bedrooms': bedrooms,
    'Floor': floor,
    'District': district
}

df = pd.DataFrame(data)
with pd.ExcelWriter('placeScrapy.xlsx') as writer:
    df.to_excel(writer, index=True)

