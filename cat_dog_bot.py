import telebot
from telebot import types
from get_image import get_image_of_dog
from get_image import get_image_of_cat

bot = telebot.TeleBot('5053129987:AAEx3Yunb-0qcqZaAGR1fOggyUfj3XWoLKc')

# @message_handler reacts on incoming messages.

# Handling all messages that contain '/start'
@bot.message_handler(commands=['start'])
def send_message(message):
    sticker = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, "If you need help, type /help")

# Handling /help command.
# The function sends to user a message with explanation how to get image of animal.
@bot.message_handler(commands=["help"])
def help_user(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Send message to developer", url="telegram.me/Diana_s96"))
    bot.send_message(message.chat.id,
                     "1) Type /photo.\n" +
                     "2) Click on the option you are interested in.\n" +
                     "3) Enjoy picture of cute animal!", reply_markup=keyboard)

# Handling /photo command.
# The function creates menu that allows to choose image the user can get
@bot.message_handler(commands="photo")
def get_photo_of_cute_animal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_cat = types.KeyboardButton("Get image of cat")
    item_dog = types.KeyboardButton("Get image of dog")

    markup.add(item_cat, item_dog)

    bot.send_message(message.chat.id, "Please, choose an option from the menu", parse_mode=None, reply_markup=markup)

# Sending requested image of animal to user
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
            bot.send_message(message.chat.id, "Ooops, I don't understand you. Try again")

bot.infinity_polling()