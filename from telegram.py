from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "7251524549:AAHMhDKGeXiRI08vPxHzninmmgmYKnQ1Mns"

print("Bot çalışmaya başladı!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()