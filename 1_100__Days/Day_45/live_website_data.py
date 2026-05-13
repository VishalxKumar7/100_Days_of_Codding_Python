from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)

# print(soup.title)

# first_title = soup.find(name="a")
# print(first_title)

# titles = soup.select("span.titleline > a")
# for title in titles:
#     print(title.text)
#     print(title["href"])

# link = soup.find("a", href="https://arxiv.org/abs/2605.08419")
# print(link.text)


# titles = soup.select("span.titleline > a")
# for title in titles:
#     print(title.text)
#     print(title["href"])
#     print(title.s)

# score = soup.find("span", class_="score").getText()
# print(score)

# scores = soup.find_all("span", class_="score")

# for score in scores:
#     print(score.text)


titles = soup.find_all("span", class_="titleline")

articles = {title.find("a").text: title.find("a")["href"] for title in titles}
print(articles)