import urllib
import json
from urllib import request
import requests

# Getting image of cat
def get_image_of_cat():
    with urllib.request.urlopen("https://api.thecatapi.com/v1/images/search") as url:
        data = url.read().decode('utf-8')
    data_json = json.loads(data)
    url = data_json[0]['url']
    img = requests.get(url).content
    with open("cat.jpg", "wb") as handler:
        handler.write(img)

# Getting image of dog
def get_image_of_dog():
    with urllib.request.urlopen("https://dog.ceo/api/breeds/image/random") as url:
        data = url.read().decode('utf-8')
    data_json = json.loads(data)
    url = data_json['message']
    fd_dog = open("dog.jpg", "wb")
    fd_dog.write((urllib.request.urlopen(url).read()))
    fd_dog.close()
