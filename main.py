import os
import random
import subprocess

from telegram.ext import *
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

from gaalis import GAALIS
from commands import COMMANDS
from greetings import GREETINGS
import subprocess
import random
from names import combo_1,combo_2
import requests

load_dotenv('.env')
API_KEY = '{}:{}'.format(os.getenv('API_ID'),os.getenv('API_TOKEN'))
API_URL = os.getenv('TORRENT_API')

def error_handler(update: Update, context) -> None:
    update.message.reply_text('Lode einstein hu kya?')


def helper_handler(update: Update, context) -> None:
    update.message.reply_text(
        "**This is under-development toh kuch mat bolna!**\ntry out commands available\n/downloadkarna : Download kar ke dunga\n/nikal : Teri nazro se door ho jaunga\n/naamde : Mast naam dunga")


def start_handler(update: Update, context) -> None:
    update.message.reply_text(
        'Arrey! Kaisa hai re tu? Abhi /dikha bhej teri madad ho jaegi!')


def random_name_generator(update: Update, context) -> None:
    name = combo_1[random.randint(0, len(combo_1)-1)] + \
        ' ' + combo_2[random.randint(0, len(combo_2)-1)]
    update.message.reply_text('Kaisa hai re {}!'.format(name))

async def listing_handler(update: Update,context):
    message = update.message.text
    splits = message.split(' ')
    if len(splits) == 2:
        params = {"q":splits[1],'size':6,'page':1}
        response = requests.get(API_URL,params=params)
        if response.status_code == 200:
            keyboard = []
            for obj in response.json():
                keyboard.append([InlineKeyboardButton(obj['name'], callback_data=obj['infohash'])])
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Please choose:", reply_markup=reply_markup)
        else:
            await update.message.reply_text('Error {}!'.format(response.status_code))
#/dhundh uncharted
async def option_handler(update: Update, context) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

def download_handler(update: Update,context ) -> None:
    message = update.message.text
    splits = message.split(' ')
    if len(splits) == 2:
        if (len(splits[1]) < 50):
            update.message.reply_text(
                'Dusra fresh URL/Magnet bhej ye nahi chalega!')
            return
        subprocess.run('dir', shell=True)
        update.message.reply_text('Kar raha hun na bhai! rukja jara.')
        return
    update.message.reply_text('Saath mein URL/Magnet bhej ye nahi chalega!')


def greet_handler(update: Update, context) -> None:
    message = update['message'].text
    if '/' in message:
        update.message.reply_text('Galat command kyu de raha hai?')
        return
    if message.lower() in GAALIS:
        update.message.reply_text(
            'Gaali kyu de raha bhosd*ke? aur kaam hai to bol baki pehli fursat mein nikal.')
        return
    if message.lower() in GREETINGS:
        update.message.reply_text('Hi but itna kyu formal banna hai?')
        return
    update.message.reply_text('Time khoti mat kar bhosd*ke! Bol kya kaam hai?')


if __name__ == '__main__':
    print('Struggle chalu!')
    updater = Updater(API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("downloadkarna", download_handler))
    # dispatcher.add_handler(CommandHandler("karnalode",karna))
    dispatcher.add_handler(CommandHandler("dikha",helper_handler))
    dispatcher.add_handler(CommandHandler("naamde",random_name_generator))
    dispatcher.add_handler(CommandHandler("dhundh",listing_handler))
    dispatcher.add_handler(CallbackQueryHandler(option_handler))
    dispatcher.add_handler(MessageHandler(Filters.text,greet_handler))
    updater.start_polling(poll_interval=0.2,drop_pending_updates=True)
    updater.idle()
