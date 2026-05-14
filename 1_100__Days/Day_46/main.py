import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

if not os.path.exists("oauth.json"):
    print("oauth.json not found. Run: ytmusicapi oauth")
    exit()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]
print(f"Found {len(song_names)} songs")

yt = YTMusic("oauth.json")

playlist_id = yt.create_playlist(
    title=f"{date} Billboard 100",
    description=f"Top songs from {date}",
)
print(f"Created playlist, ID: {playlist_id}")

for song in song_names:
    try:
        results = yt.search(song, filter="songs", limit=1)
        if results:
            yt.add_playlist_items(playlist_id, [results[0]["videoId"]])
            print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")