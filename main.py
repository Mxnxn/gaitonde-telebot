from dotenv import load_dotenv
import os
from telegram.ext import *
from telegram import Update
from gaalis import GAALIS
from commands import COMMANDS
from greetings import GREETINGS
import subprocess
import random
from names import combo_1,combo_2

load_dotenv('.env')
API_KEY = '{}:{}'.format(os.getenv('API_ID'),os.getenv('API_TOKEN'))


def error_handler(update: Update,context ) -> None:
    update.message.reply_text('Lode einstein hu kya?')

def helper_handler(update: Update,context ) -> None:
    update.message.reply_text("**This is under-development toh kuch mat bolna!**\ntry out commands available\n/downloadkarna : Download kar ke dunga\n/nikal : Teri nazro se door ho jaunga\n/naamde : Mast naam dunga")

def start_handler(update: Update,context ) -> None:
    update.message.reply_text('Arrey! Kaisa hai re tu? Abhi /dikha bhej teri madad ho jaegi!')

def random_name_generator(update: Update,context ) -> None:
    name = combo_1[random.randint(0,len(combo_1)-1)] + ' ' + combo_2[random.randint(0,len(combo_2)-1)]
    update.message.reply_text('Kaisa hai re {}!'.format(name))

def download_handler(update: Update,context ) -> None:
    message = update.message.text
    splits = message.split(' ')
    if len(splits) == 2:
        if(len(splits[1]) < 50):
            update.message.reply_text('Dusra fresh URL/Magnet bhej ye nahi chalega!')
            return 
        subprocess.run('dir',shell=True)
        update.message.reply_text('Kar raha hun na bhai! rukja jara.')
        return 
    update.message.reply_text('Saath mein URL/Magnet bhej ye nahi chalega!')


def greet_handler(update: Update,context ) -> None:
    message = update['message'].text
    if '/' in message:
        update.message.reply_text('Galat command kyu de raha hai?')
        return
    if message.lower() in GAALIS:
        update.message.reply_text('Gaali kyu de raha bhosd*ke? aur kaam hai to bol baki pehli fursat mein nikal.')
        return
    if message.lower() in GREETINGS:
        update.message.reply_text('Hi but itna kyu formal banna hai?')
        return
    update.message.reply_text('Time khoti mat kar bhosd*ke! Bol kya kaam hai?')

if __name__ == '__main__':
    print('Struggle chalu!')
    updater = Updater(API_KEY,use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start",start_handler))
    dispatcher.add_handler(CommandHandler("downloadkarna",download_handler))
    # dispatcher.add_handler(CommandHandler("karnalode",karna))
    dispatcher.add_handler(CommandHandler("dikha",helper_handler))
    dispatcher.add_handler(CommandHandler("naamde",random_name_generator))

    dispatcher.add_handler(MessageHandler(Filters.text,greet_handler))
    updater.start_polling(poll_interval=0.2,drop_pending_updates=True)
    updater.idle()