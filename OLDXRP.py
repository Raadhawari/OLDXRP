import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual BotFather token
TOKEN = "7784400136:AAG0V0XYWli-GMP2kkVjPj82ip6oxdTJVHk"
bot = telebot.TeleBot(TOKEN)

# Replace with your actual website/domain
MINING_URL = "https://t.me/xrpmin_bot?startapp"

# Welcome message function
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name  # Get user's first name
    
    # If the user has no first name, use "ضيف" (guest)
    if not user_first_name:
        user_first_name = "ضيف"

    # Arabic welcome message with user's first name
    welcome_text = f"""
👋 مرحباً {user_first_name}!

🚀 بوت تعدين XRP الأول من نوعه!

💰 اربح أكثر من 2000$ يومياً من خلال نظام التعدين المتطور
⏱️ يعمل تلقائياً بدون مجهود منك - 24 ساعة يومياً
💎 تقنية تعدين سحابية متطورة بأعلى سرعة وكفاءة
✅ سحب فوري للأرباح عبر محفظتك الخاصة

⚡ اضغط على الزر أدناه لبدء الربح الآن!
"""

    # Inline keyboard with a button that opens the website
    keyboard = InlineKeyboardMarkup()
    button_mining = InlineKeyboardButton("🔥 ابدأ التعدين الآن", url=MINING_URL)
    keyboard.add(button_mining)

    # Send message with button
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

# Run the bot
print("Bot is running...")
bot.polling()

