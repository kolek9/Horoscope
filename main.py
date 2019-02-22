import requests
from bs4 import BeautifulSoup

print("Enter your zodiac sign! Make sure there are no spaces\n")
while True:
    sign = input()
    sign.lower()
    all = ["aries", "taurus", "pisces", "capricorn", "aquarius", "saggitarius", "gemini", "cancer", "leo", "libra", "scorpio", "virgo"]
    if sign in all:
        url = "https://www.astrology.com/horoscope/daily/"+ sign +".html"
        break
    else:
        print("Invalid sign, please try again!\n")
        

page_response = requests.get(url, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
container = page_content.find_all('p')
horoscope = container[0].text
print(horoscope)
