from bs4 import BeautifulSoup

with open("1_100__Days/Day_45/top_100_movies.html", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all("h2")
movie_title = []
for movie in movies:
    strong = movie.find("strong")
    if strong:
        movie_title.append(strong.text)

with open ("1_100__Days/Day_45/top_100_movies.txt", 'w') as file:
    for title in movie_title[::-1]:
        file.write(f"{title}\n")
