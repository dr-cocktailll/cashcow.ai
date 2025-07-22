from telegram import Update
from telegram.ext import CallbackContext

def accounts_handler(update: Update, context: CallbackContext) -> None:
    """Handles the /accounts command and displays account information."""
    user = update.effective_user
    account_info = get_account_info(user.id)  # Function to retrieve account info
    message = format_account_info(account_info)  # Function to format the account info for display

    update.message.reply_text(message)

def get_account_info(user_id):
    # Placeholder function to simulate fetching account info
    return {
        "user_id": user_id,
        "balance": 100.0,
        "transactions": [
            {"date": "2023-01-01", "amount": -50.0, "description": "Purchase"},
            {"date": "2023-01-02", "amount": 150.0, "description": "Deposit"},
        ]
    }

def format_account_info(account_info):
    # Format the account information for display
    formatted_info = f"Account ID: {account_info['user_id']}\n"
    formatted_info += f"Balance: ${account_info['balance']:.2f}\n"
    formatted_info += "Recent Transactions:\n"
    
    for transaction in account_info['transactions']:
        formatted_info += f"{transaction['date']}: ${transaction['amount']:.2f} - {transaction['description']}\n"
    
    return formatted_info