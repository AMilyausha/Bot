from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot import *

app = ApplicationBuilder().token('***********************************8').build()

app.add_handler(CommandHandler("hello", hello_coommand))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("mult", mult_command))

app.run_polling()

