import telebot
import sys
import requests
import json
import schedule
import time
import emoji

DEV_API_KEY = "44db6a862fba0b067b1930da0d769e98"
TOKEN = '213675554:AAEHHFkB-NCFt0evRhfoodeL3SOIIEfDGNQ'
dest = '@clima_rio'
creator = '@jgabrielfreitas'

bot = telebot.TeleBot(TOKEN)

def job():
    city = "rio de janeiro"
    country = "br"
    url = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}&lang=pt&appid={2}".format(city, country, DEV_API_KEY)
    response = requests.request("GET", url)
    data = json.loads(response.text)
    list_of_weathers = data['weather']
    current_weather = list_of_weathers[0]
    main_current = current_weather['main']

    main = data['main']

    # get description
    description = current_weather['description']
    description = description[:1].upper() + description[1:]

    # emojis
    cloud = ':cloud:'
    sun_behind_cloud = ':sun_behind_cloud:'
    sun = ':black_sun_with_rays:'
    sun_with_cloud_and_rain = ':white_sun_behind_cloud_with_rain:'
    rain = ':cloud_with_rain:'

    emoji_to_show = sun # by default

    humidity = main['humidity']
    temp = main['temp']
    temp_min = main['temp_min']
    temp_max = main['temp_max'] / 10

    if main_current == 'Clouds':
        emoji_to_show = ':cloud:'
    else:
        # send sun (default) and send message for me
        # TODO
        bot.send_message(creator, "description to add: {0}".format(main_current))


    # message_to_send = u"{0} - {1} \nTemperatura maxima: sC".format(emoji_to_show, description)
    bot.send_message(dest, emoji.emojize(u"{0} - {1} \nTemperatura maxima: {2}C".format(emoji_to_show, description, temp_max))) # dest and msg



# run jobs
job()
