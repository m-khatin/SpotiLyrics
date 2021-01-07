import lyricsgenius
import requests
import json

checkIfPlaysHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQB33j5somlTuoTZcZNeY3xOHcyA8f-nNMs2s4k_dCzJlL7gZXdBvVCgu-SFsYYvDMVWhbwTlfuzqH_q7QPe2JSA7yL4PMWo49g4mQR21hfPk9ySjYw2fGdS0vWkra-pKEbZ2kWv6ujR-sQRIaRSlw8wpGoe2yH-7D-Ka0oEXClrmM1EBpSFtqZFSjXh3yNCfulBY6Bhqz6eWkkh6zd221Pc1SLctGes10V_akcr8rwVG7K6CtiCIMzmhiE5gVGSnkFjWKS5Faqfdi-_0rU6',
}
response = requests.get('https://api.spotify.com/v1/me/player', headers=checkIfPlaysHeaders).json()
if response.get('is_playing'):
    getSongHeaders = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQB33j5somlTuoTZcZNeY3xOHcyA8f-nNMs2s4k_dCzJlL7gZXdBvVCgu-SFsYYvDMVWhbwTlfuzqH_q7QPe2JSA7yL4PMWo49g4mQR21hfPk9ySjYw2fGdS0vWkra-pKEbZ2kWv6ujR-sQRIaRSlw8wpGoe2yH-7D-Ka0oEXClrmM1EBpSFtqZFSjXh3yNCfulBY6Bhqz6eWkkh6zd221Pc1SLctGes10V_akcr8rwVG7K6CtiCIMzmhiE5gVGSnkFjWKS5Faqfdi-_0rU6',
    }
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=getSongHeaders).json()

    songName = response.get('item').get('name')
    artistName = response.get('item').get('artists')[0].get('name')

    #print('Currently playing:', artistName,' - ' , songName)

    token = 'VoyUbspPoaKiCFM3wv4f8lnBrIqtEno7haI_-jKyr1O6qXn0vwPZbHEnXJ4ZX7-6'
    genius = lyricsgenius.Genius(token)
    song = genius.search_song(songName, artistName)
    print(song.lyrics)
else:
    print("Song isn't playing...")
