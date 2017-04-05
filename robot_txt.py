
from urllib.request import urlopen
import io

def get_robot_txt(url):

    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urlopen(path + 'robots.txt', data = None )
    data = io.TextIOWrapper(req, encoding = 'utf-8')
    return data.read()

print(get_robot_txt('​https://www.reddit.com/'))