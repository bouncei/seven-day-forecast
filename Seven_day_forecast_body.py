import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999#.XznDsDUo_IV")
soup = BeautifulSoup(page.content,"html.parser")
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_="tombstone-container")

# print(items[0].find(class_="period-name").get_text())
# print(items[2].find(class_="period-name").get_text())
# print(items[1].find(class_="temp").get_text())


period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions =  [item.find(class_="short-desc").get_text() for item in items]


print(period_names)
print(short_descriptions)

the_weather = pd.DataFrame(
    {
    "period": period_names,
    "short-desc": short_descriptions
    }
)

print(the_weather)

the_weather.to_csv("weather.csv")
















