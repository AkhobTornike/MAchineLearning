from scrapy.http import TextResponse
import pandas as pd
import requests
import pprint

url = requests.get("https://www.myhome.ge/ka/s/?Keyword=%E1%83%97%E1%83%91%E1%83%98%E1%83%9A%E1%83%98%E1%83%"
                   "A1%E1%83%98&AdTypeID=1&cities=1996871&GID=1996871")
resources = TextResponse(url.url, body=url.text, encoding='utf-8')
links = resources.css("a.card-container::attr(href)").getall()

# მოკლედ ყველანაირად ვცადე და არ გამოდის ბოლოს დავასკვენი, რომ საიტს აქვს პრობლემა. როცა გამოვიტანე url.text ბოლოს
# წერია რომელიღაც თაგში რომ დროებით საიტზე წვდომა შეზღუდულია ამიტომ თუ ამ კვირაში არ გამოსწორდება რაც არამგონია
# ამ საიტს ვერ დავსკრაპავთ ჯერჯერობით