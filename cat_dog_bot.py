import telebot
from telebot import types
import urllib
import json

bot = telebot.TeleBot('5053129987:AAEx3Yunb-0qcqZaAGR1fOggyUfj3XWoLKc')

# @message_handler reacts on incoming messages.

# Handling all messages that contain '/start'
@bot.message_handler(commands=['start'])
def send_message(message):
    sticker = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_cat = types.KeyboardButton("Get image of cat")
    item_dog = types.KeyboardButton("Get image of dog")

    markup.add(item_cat, item_dog)

    bot.send_message(message.chat.id, "Please, choose an option from the menu", parse_mode=None, reply_markup=markup)

# Sending requested image of dog/cat
@bot.message_handler(content_types=['text'])
def send_image(message):
    if message.chat.type == 'private':
        if message.text == "Get image of cat":
            get_image_of_cat()
            photo = open('cat.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == "Get image of dog":
            get_image_of_dog()
            photo = open("dog.jpg", 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "Whaaaaaaaat????")

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

bot.infinity_polling()