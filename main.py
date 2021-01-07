import lyricsgenius
import requests
import json

bearer = 'Bearer BQDAYkTA5zFhNUhbSBHMh7XcYaKLl4RLF6_J2PuRZ6jZzHcq6uwrqfxUZLWyieott4FFPp88jeGHLUqwzdUSBSNyTd8vOUAtTVJfjC6kmOT9xW6sFG7RvvZaQWSmnD5dNwocpwQZosGYjtMl1S73Du_kcHbZjqfoh0B2IKUd6gfLKpBBWTuyH1Mu4p2KAfJa-SA9OR9RzbDJT-ozbH6w_kYCNdaJMobTMQUfEZCTFhydkMuAEQvpSLUQ2e-VaObUe8OBkXLBWdRv9w_TCSZJ'

checkIfPlaysHeaders = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': bearer,
}
response = requests.get('https://api.spotify.com/v1/me/player', headers=checkIfPlaysHeaders).json()
if response.get('is_playing'):
    getSongHeaders = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': bearer,
    }
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=getSongHeaders).json()

    songName = response.get('item').get('name')
    artistName = response.get('item').get('artists')[0].get('name')

    #print('Currently playing:', artistName,' - ' , songName)

    geniusToken = '_GMyErJoefQ4VBSD1zaXFROpuKFnGiV7a99yiDFk2hHwadKihVT_NSoUUIXsCww6'
    genius = lyricsgenius.Genius(geniusToken)
    song = genius.search_song(songName, artistName)
    print(song.lyrics)
else:
    print("Song isn't playing...")
