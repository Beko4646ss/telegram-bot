import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7562561587:AAGUP22ZXhvOpOAeUqfcDlJM7HudfEsQy34"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    user = message.new_chat_members[0]
    mention = f"@{user.username}" if user.username else user.first_name or "Yeni Üye"

    welcome_text = (
        f"Merhabalar {mention} 👋\n\n"
        "Almanya Mesleki Denklik sayfasına hoşgeldiniz.\n\n"
        "Almanya yolculuğuna başlamak için aşağıdaki kaynakları kullanabilirsiniz."
    )

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🇩🇪 Almanca’ya Başlayanlar İçin", url="https://t.me/almanyadeneme"),
        InlineKeyboardButton("📘 ÖSD Doküman", url="https://t.me/osddokuman"),
        InlineKeyboardButton("📗 Goethe Doküman", url="https://t.me/goethedokuman"),
        InlineKeyboardButton("ℹ️ Almanya’ya Göç Bilgilendirme", url="https://t.me/almanyadeneme1"),
        InlineKeyboardButton("💼 İş Bulma ve Denklik Hizmetleri", url="https://t.me/saclimehmet1")
    )

    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard, parse_mode="Markdown")

print("✅ Bot aktif. Yeni üyeler karşılanacak.")
bot.infinity_polling()