import urllib
import json
from urllib import request

# Getting image of cat
def get_image_of_cat():
    url = "https://cataas.com/cat"
    fd = open("cat.jpg", 'wb')
    fd.write(urllib.request.urlopen(url).read())
    fd.close()

# Getting image of dog
def get_image_of_dog():
    with urllib.request.urlopen("https://dog.ceo/api/breeds/image/random") as url:
        data = url.read().decode('utf-8')
    data_json = json.loads(data)
    url = data_json['message']
    fd_dog = open("dog.jpg", "wb")
    fd_dog.write((urllib.request.urlopen(url).read()))
    fd_dog.close()
