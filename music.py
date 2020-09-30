import requests


def api_request(url: str) -> requests.Response:  # found some tutorials online in order to make this work
    r = requests.get(
        url,
        params={'fmt': 'json'},
        headers={'Accept': 'application/json'})  # real python mentions using 'content-type' but this seems to work
    return r


if __name__ == '__main__':
    result = api_request('https://musicbrainz.org/ws/2/artist/80c72415-d26a-4f49-b13e-544e50b8c188?inc=recordings')

    print(result.json())  # making sure I have the response that I  want
