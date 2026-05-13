from bs4 import BeautifulSoup

with open("1_100__Days/Day_45/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# company_url = soup.select_one(selector="#name")
# print(company_url)

heading = soup.select(".heading")
print(heading)