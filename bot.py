from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال 24/7 🚀")

app = ApplicationBuilder().token("8524204360:AAH2jDtYKfKVxigEcVxvzwCdAleiDWs_pYU").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()