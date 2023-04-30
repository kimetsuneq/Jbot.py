import logging
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = 'YOUR_BOT_TOKEN_HERE'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please send a message to me")

def reply(update, context):
    message = update.message.reply_to_message
    if message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Processing...")
        for i in range(1, 1001):
            time.sleep(2)
            context.bot.send_message(chat_id=update.effective_chat.id, text=str(i), reply_to_message_id=message.message_id)

def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stopping...")
    # your code for stopping the execution of the bot

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(MessageHandler(Filters.reply, reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
