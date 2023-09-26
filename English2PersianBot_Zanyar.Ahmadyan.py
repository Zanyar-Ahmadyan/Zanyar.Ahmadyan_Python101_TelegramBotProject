import telebot
from googletrans import Translator
import tkinter as tk

# Replace 'YOUR_API_TOKEN' with your actual Telegram bot API token
bot = telebot.TeleBot('6488627634:AAFHwOHysWTLAjAi4UImDvxQgOTF5hQ7th8')

translator = Translator()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    chat_id = message.chat.id
    text = message.text
    translation = translator.translate(text, src='en', dest='fa')
    translated_text = translation.text
    bot.send_message(chat_id, f"Translated to Persian: {translated_text}")

if __name__ == "__main__":
    bot.polling()
