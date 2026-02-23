# from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder , CommandHandler , ContextTypes , CallbackQueryHandler

# TOKEN =""

# savollar = 'Pthonda matn nima yordamida chop etiladi?'
# varint =[
#     ("if" , "A"),
#     ("for" , "B"),
#     ("print" , "C"),
#     ("while", "D")
# ]

# javob = "C"

# async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
#     keyboard =[]
#     for matn , qiymat in varint:
#         keyboard.append([InlineKeyboardButton(matn , callback_data=qiymat)
#         ])
        
#     reply_markup =InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text(
#         savollar,
#         reply_markup=reply_markup
#     ) 

# async def button(update: Update , context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     if query.data == javob:
#         await query.edit_message_text("To'g'ri javob!")
#     else:
#         await query.edit_message_text("Noto'g'ri javob!")

# def main():
#     app = ApplicationBuilder().token(TOKEN).build()

#     app.add_handler(CommandHandler("start" , start))
#     app.add_handler(CallbackQueryHandler(button))
#     print("Bot ishga tushdi ...")
#     app.run_polling()      

# if __name__ == "__main__":
#     main()