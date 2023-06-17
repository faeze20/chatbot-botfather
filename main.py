from decouple import config
Tk=config("token")
# print(Tk)
API_TOKEN=config("token")

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,CallbackContext
from telegram.ext import MessageHandler, filters
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,ReplyKeyboardMarkup


lorem="jhaskh Kuydsu KHDKJ cmnsjdhiuB"
solidkeys=[[KeyboardButton("1"),KeyboardButton("2")],
           [KeyboardButton("3"),KeyboardButton("4"),KeyboardButton("5")],
           [KeyboardButton("6"),KeyboardButton("7")]
    
]

inlinekeys=[[InlineKeyboardButton("1"),url="https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot.py"],
            [InlineKeyboardButton("2"),url="https://google.com"]
    
]

def solid_reply(update:Update, context:CallbackContext):
    solidMarkup=ReplyKeyboardMarkup(keyboard=solidkeys, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(lorem, reply_markup=solidMarkup)
    
def inline_reply(update:Update, context: CallbackContext):
    inlineMarkup=InlineKeyboardMarkup(keyboards=inlinekeys)  
    update.message.reply_text(lorem, reply_markup=inlineMarkup)  


def remove_solid_reply(update:Update, context:CallbackContext):
    update.message.reply_text("solidrepilr removed", reply_markup=ReplyKeyboardRemove)    
    
    
    
    
async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    args=context.args
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="hello world!")
    chat_id=update.effective_chat.id
    await context.bot.forward_message(chat_id=chat_id, from_chat_id="https://t.me/cs50p",message_id=15624)
    await context.bot.forward_message(chat_id=chat_id, from_chat_id="https://t.me/cs50p",message_id=15624)
    await context.bot.edit_message_text(text="helloworld", chat_id=chat_id, message_id=15624)
    
      
      
      
      
async def gmail(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="your gmail",reply_to_message_id=update.effective_message.id)     




async def echo(update:Update, context:ContextTypes.DEFAULT_TYPE):
    txt=update.effective_message.text.split('\n')
    txt="\n\t\t".join(txt)
    await  context.bot.send_message(chat_id=update.effective_chat.id, text="your gmail", reply_to_message_id=update.effective_message.id) 
    text=f"your to do list is\n\t\t-{txt}"    
    
    
    
async def addUser(update:Update, context:ContextTypes.DEFAULT_TYPE):
    args=context.args
    message_id=Update.effective_message.id    
    user_id=Update.effective_user.id
    chat_id=Update.effective_chat.id
    if user_id in database["id"]:
        await context.bot.send_message(chat_id=chat_id, text="id already in database", reply_to_message_id=message_id)
    elif  len(args)!=3: 
        await context.bot.send_message(chat_id=chat_id, text="Error", reply_to_message_id=message_id)   
    else:
        await database["id"].append(user_id) 
        database["name"].append(args[0])
        database["telephone"].append(args[1]) 
          
        
    
    
    
    
    
    
database={
        "name":["ali"],
        "id":[],
        "telephone":["1234567890"]
    }    
      
def main():
    app=Application.builder().token(Tk).build()
    start_handler=CommandHandler("start",start)
    gmail_handler=CommandHandler("gmail",gmail)
    echo_handler=MessageHandler(filters.TEXT&(~filters.COMMAND), echo)
    user_handler=CommandHandler("adduser", addUser)
    # solid_reply_handler=CommandHandler("solid",  solid_reply)
    # inline_reply_handler=CommandHandler("inline",  inline_reply)
    # remove_solid_reply_handler=CommandHandler("inline",  inline_reply)
    user_handler=CommandHandler("adduser", addUser)
    
    bot=Update(API_TOKEN)
    dis=bot.dispatcher()
    dis.add_handler(CommandHandler("start",start))
    dis.add_handler(CommandHandler("inline",inline_reply))
    dis.add_handler(CommandHandler("solid",  solid_reply))
    dis.add_handler(CommandHandler("remove",  remove_solid_reply))
    bot.stat_polling()
    


    
    
    app.add_handler(user_handler)
    app.add_handler(gmail_handler)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler( solid_reply_handler)
    app.add_handler( inline_reply_handler)
    app.add_handler( remove_solid_reply_handler)
    app.run_polling()
if __name__=="__main__":
    main()       
       