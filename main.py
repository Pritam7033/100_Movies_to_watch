import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
html_document = response.text

soup = BeautifulSoup(html_document, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies.reverse()
movies_list_to_add = []
for movie in movies:
    movies_list_to_add.append(f"{movie.get_text()}\n")

with open(file="./movie_list.txt",mode="w",encoding="utf-8") as file:
    file.writelines(movies_list_to_add)

