from telegram import Update
from telegram.ext import CallbackContext

entries = []

def add_entry(title: str, content: str):
    entry_id = len(entries) + 1
    entries.append({'id': entry_id, 'title': title, 'content': content})

def view_entries():
    return "\n".join([f"{entry['id']}: {entry['title']} - {entry['content']}" for entry in entries])

def handle_add_entry(update: Update, context: CallbackContext):
    title = context.args[0] if context.args else "Untitled"
    content = " ".join(context.args[1:]) if len(context.args) > 1 else "No content provided"
    add_entry(title, content)
    update.message.reply_text(f"Entry added: {title}")

def handle_view_entries(update: Update, context: CallbackContext):
    if entries:
        update.message.reply_text(view_entries())
    else:
        update.message.reply_text("No entries found.")