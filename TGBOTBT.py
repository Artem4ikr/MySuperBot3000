
from telegram import *
from telegram.ext import *
from requests import *

updater = Updater(token='7669735890:AAHscyurijAl-6_ENRyG-6Bnn8SBOC5HS-s')
dispatcher = updater.dispatcher

def startCommand(updtade: Update, context: CallbackContext):
    buttons = [[KeyboardButton('random image')], [KeyboardButton('random person')]]
    context.bot.send_message(chat_id=update.effective_chat.id, text='welcome to my bot!')
    reply_markup=ReplyKeyboardMarkup(buttons)

dispatcher.add_handler(CommandHandler('start', startCommand))

updater.start_polling()