import urllib.parse
import urllib.request
import urllib.error
import json

API_KEY = 'AIzaSyDvysm00R5FClmqtxcATsgpKHdt2GxCaiU'


def search_video(query):
    params = {
        'maxResults': 50,
        'q': query,
        'key': API_KEY
    }
    url = 'https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&'
    for key, value in params.items():
        t = urllib.parse.urlencode({key: value})
        url += t + '&'

    try:
        response = urllib.request.urlopen(url)

    except urllib.error.URLError:
        return -1

    data = json.loads(response.read())
    search_results = []

    for x in data['items']:
        d = dict()
        d['id'] = x['id']['videoId']
        d['title'] = x['snippet']['title']
        search_results.append(d)

    return search_results


def search_playlist(query):
    url = 'https://www.googleapis.com/youtube/v3/search?type=playlist&part=snippet&'
    t = urllib.parse.urlencode({"q": query})
    url += t + '&'
    t = urllib.parse.urlencode({"key": API_KEY})
    url += t

    try:
        response = urllib.request.urlopen(url)

    except urllib.error.URLError:
        return -1

    data = json.loads(response.read())
    search_results = []

    for x in data['items']:
        d = dict()
        d['id'] = x['id']['playlistId']
        d['title'] = x['snippet']['title']
        search_results.append(d)

    return search_results
