from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

TOKEN = "7742693696:AAEhuQEPL1rvlYsQreCyLuctyjov1kFCR_M"


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your bot. Use /help to see available commands.")


async def hello(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am good, just chilling.")



async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/help - Show available commands")

    keyboard = [
        [InlineKeyboardButton('Option 1', callback_data='option_1')],
        [InlineKeyboardButton('Option 2', callback_data='option_2')]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose your option:', reply_markup=reply_markup)

async def animals(update: Update, context: CallbackContext):
    await update.message.reply_text('Choose an animal:')

    keyboard = [
        [InlineKeyboardButton('Axolotl 🫡', callback_data='Axolotl')],
        [InlineKeyboardButton('Quokka 😂', callback_data='Quokka')]

    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose your option:', reply_markup=reply_markup)

async def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'option_1':
        await query.edit_message_text(text='You chose Option 1')
    elif query.data == 'option_2':
        await query.edit_message_text(text='You chose Option 2')

async def button_callback_animals(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'Axolotl':
        await query.edit_message_text(text='You chose Axolotl ')
    elif query.data == 'Quokka':
        await query.edit_message_text(text='You chose Quokka ')


async def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    await update.message.reply_text(
        text=f'You said: {user_text}',

    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("animals", animals))

    app.add_handler(CallbackQueryHandler(button_callback))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == '__main__':
    main()
