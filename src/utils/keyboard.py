from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("/accounts", callback_data='accounts')],
        [InlineKeyboardButton("+", callback_data='add_entry')]
    ]
    return InlineKeyboardMarkup(keyboard)