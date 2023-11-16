from scrapy.http import TextResponse
import requests
import pprint

url = requests.get("https://place.ge/ge/ads?object_type=flat&mode=list&nearest=0&type=for_sale&condition=&project="
                   "&agency_id=&city_id=1&region_id=&district_id=&street_id=&commercial_type=&commercial_type2=&status"
                   "=&rooms_from=-%E1%83%93%E1%83%90%E1%83%9C&rooms_to=-%E1%83%9B%E1%83%93%E1%83%94&living_space_from="
                   "-%E1%83%93%E1%83%90%E1%83%9C&living_space_to=-%E1%83%9B%E1%83%93%E1%83%94&price_from=-%E1%83"
                   "%93%E1%83%90%E1%83%9C&price_to=-%E1%83%9B%E1%83%93%E1%83%94&currency_id=1&with_photos=0&owner=0")

# print(url)

res = TextResponse(url.url, body=url.text, encoding='utf-8')

# print(res.text)
# pprint.pprint(res.text)

urls = res.css("div.img a::attr(href)").getall()
# print(urls)
# pprint.pprint(urls)

for u in urls:
    if u != '/ge/faq?open=5':
        print(u)


# ssScrapy ->
# print(f"city -> {city}; \nneighbour -> {neighbour}; \nstreet -> {street};")

# city.append(address[0])
    # neighbour.append(address[1])
    # street.append(address[2])
    # print(city)
    # print(address)
    # print(street)
    # info = linked_resources.css("h5.sc-6e54cb25-4.gMvFbt::text").extract()
    # area.append(info[0])
    # rooms.append(info[0])
    # beds.append(info[0])
    # floor.append(info[0])



# info = linked_resources.css("h5.sc-6e54cb25-4.gMvFbt::text").extract()
# area = info[0]
# rooms = info[1]
# beds = info[2]
# floor = info[3]

# print(f"area -> {area}; \nrooms -> {rooms}; \nbeds -> {beds}; \nfloor -> {floor}")
