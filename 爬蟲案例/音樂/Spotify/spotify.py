import os
import re
import requests
import string
import time

spotify_playlist_link = input("請輸入spotify撥放清單: ")

if not spotify_playlist_link:
    print("檢測到你沒輸入撥放清單連結!")
    exit()

pattern = r"https://open.spotify.com/playlist/([a-zA-Z0-9]+)\?si=.*"
match = re.match(pattern, spotify_playlist_link)

if not match:
    raise ValueError("無效撥放清單，正確格式http://open.spotify.com/playlist/XXXX?si=XXXXXXX")

playlist_id = match.group(1)

headers = {
    'origin': 'https://spotifydown.com',
    'referer': 'https://spotifydown.com/',
}

playlist_url = f'https://api.spotifydown.com/metadata/playlist/{playlist_id}'

response = requests.get(url=playlist_url, headers=headers)
meta_data = response.json()

playlist_name = meta_data['title'] + ' - ' + meta_data['artists']
print('撥放清單名稱:', playlist_name)

music_folder = os.path.join(os.getcwd(), "music")  # Change this path to your desired music folder
folder_path = ''.join(e for e in playlist_name if e.isalnum() or e in [' ', '_'])
playlist_folder_path = os.path.join(music_folder, folder_path)

if not os.path.exists(playlist_folder_path):
    os.makedirs(playlist_folder_path)

tracklist_url = f'https://api.spotifydown.com/trackList/playlist/{playlist_id}'
offset_data = {}
offset = 0
offset_data['offset'] = offset

while offset is not None:
    response = requests.get(url=tracklist_url, params=offset_data, headers=headers)
    track_list = response.json()['trackList']
    page = response.json()['nextOffset']
    print("*" * 100)
    for count, song in enumerate(track_list):
        print("第",count+1,"首歌:", song['title'])
        song_id = song['id']
        url = f'https://api.spotifydown.com/download/{song_id}'
        response = requests.get(url=url, headers=headers)
        image_url = response.json().get('metadata').get('cover')
        download_link = response.json().get('link')
        if download_link:
            title = song['title'].translate(str.maketrans('', '', string.punctuation))
            artists = song['artists'].translate(str.maketrans('', '', string.punctuation))
            filename = f"{title} - {artists}.mp3"
            filepath = os.path.join(playlist_folder_path, filename)

            link = requests.get(download_link, stream=True)
            block_size = 1024
            downloaded = 0

            with open(filepath, "wb") as f:
                for data in link.iter_content(block_size):
                    f.write(data)
                    downloaded += len(data)
            print(f"歌曲 {filename} 下載完成.")
    while page is not None:
        offset_data['offset'] = page
        response = requests.get(url=playlist_url, params=offset_data, headers=headers)
    else:
        print("*" * 100)
        print('[*] 下載完成!!!')
        print("*" * 100)
        exit()