import os
from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
user = os.getenv('user')
api = os.getenv('api')
aio = Client(user,api)
f = aio.feeds('fan')
l = aio.feeds('light')
def start(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Go to /help for commands')
def help1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('COMMANDS\n TURN ON LIGHT\n TURN OFF LIGHT\n TURN ON FAN\n TURN OFF FAN') 
def light1(bot,update):
  chat_id = bot.message.chat_id
  aio.send_data(l.key,1)
  bot.message.reply_text('TURNING ON LIGHT')
def light0(bot,update):
  chat_id = bot.message.chat_id
  aio.send_data(l.key,0)
  bot.message.reply_text('TURNING OFF LIGHT')
def fan1(bot,update):
  chat_id = bot.message.chat_id
  aio.send_data(f.key,1)
  bot.message.reply_text('TURNING ON LIGHT')
def fan0(bot,update):
  chat_id = bot.message.chat_id
  aio.send_data(f.key,0)
  bot.message.reply_text('TURNING OFF LIGHT')      
def main(bot,update):
  a = bot.message.text
  if (a =="/help"):
    help1(bot,update)
  elif (a =="/start"):
    start(bot,update)
  elif (a =="TURN ON LIGHT"):
    light1(bot,update)
  elif (a =="TURN OFF LIGHT"):
    light0(bot,update)  
  elif (a =="TURN ON FAN"):
    fan1(bot,update)
  elif (a =="TURN OFF FAN"):
    fan0(bot,update)    
  else :
    bot.message.reply_text("invalid input refer /help for commands")

bot_token = '1915159744:AAHvaMx3XzeNVw2HQd0qdYWpxZVxdSpKac0'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle() 
