import requests
import bs4
import urllib
import urllib3
#
# url = "https://google-search3.p.rapidapi.com/api/v1/search/q=elon+musk&num=2"
#
headers = {
    'x-rapidapi-key': "7acfb85b32msh218cdca2c7e7bdfp1163b1jsna314ac48f283",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }
#
# response = requests.request("GET", url, headers=headers)
#
# a = response.text
# a = dict(a)
# a = a.split("description")[1]
#
# print(response.text)
# print(a)
# print(type(a))
# print(a["answers"])

query = "pizza"
searchInput = "https://google.com/search?q="+urllib.parse.quote(query)

res = requests.get(searchInput)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

linkElements = soup.select('div#main > div > div > div > a')

link = linkElements[0].get("href")

i = 0

while link[0:4] != "/url" or link[14:20] == "google":
    i += 1
    link = linkElements[i].get("href")

# url = "http://google.com"+link
url = "https://google-search3.p.rapidapi.com/api/v1/search/q=elon+musk&num=2"
print(url)
response = requests.request("GET", url, headers=headers)
opop = requests.get(url, headers=headers).content
print(response.text)
print(opop)