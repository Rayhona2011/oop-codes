# from telgram import Update
# from telegram.ext import{
#     ApplicationBuilder ,
#     CommandHandler ,
#     MessageHandler ,
#     ContextTypes , 
#     ConversationHandler ,
#     filters
# }

# TOKEN = ""

# ASK_NAME = 1

# async def start(update: Update , context: ContextTypes.DEFULT_TYPE):
#     await update.message.reply_text("Assalomu alaykum\n\nIsmingizni kiriting:")
#     return ASK_NAME

# async def get_name(update: Update , context: ContextTypes.DEFULT_TYPE):
#     name =update.message.text
#     context.user_data["name"] = name

#     await update.message.reply_text(
#         f"Xush kelibsiz , {name}! "
#     )
#     return ConversationHandler.END

# conv_handler = ConversationHandler(
#     entery_points=[CommandHandler("start" , start )],
#     states={
#         ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND , get_name)]
#     }
#     fallbacks =[]
# )

# app =ApplicationBuilder(.token(TOKEN).build())
# app.add_handler(conv_handler)

# print("Bot ishga tushdi ...")
 





# from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes , CallbackQueryHandler

# TOKEN =""

# async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
#     keyboard =[
#         [
#         InlineKeyboardButton("Ha" , callback_data="ha"),
#         InlineKeyboardButton("Yo'q" , callback_data="yo'q")
#         ]
#     ]
    
#     markup =InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(
#         "Tanlang:",
#         reply_markup=markup
#     )

# async def button(update: Update , context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     if query.data == "ha":
#         await query.edit_message_text("Siz HA ni bosdingiz")

#     else:
#         await query.edit_message_text("Siz YO'Q ni bosdingiz")

# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start" , start))
# app.add_handler(CallbackQueryHandler(button))

# app.run_polling()