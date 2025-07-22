# Telegram Accounts Bot

This project is a mini Telegram bot that provides a user interface for managing accounts and viewing the latest entries. It features a menu bar with an "/accounts" button, a scrollable area for displaying entries, and a button to add new entries.

## Features

- **Menu Bar**: Contains the "/accounts" button to access account information.
- **Scrollable Area**: Displays the latest entries for easy viewing.
- **Add Entry Button**: A green button with a "+" sign to add new entries.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd telegram-accounts-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in the `.env` file:
   ```
   API_TOKEN=your_api_token_here
   ```

## Usage

To run the bot, execute the following command:
```bash
python src/app.py
```

Make sure to replace `your_api_token_here` with your actual Telegram bot API token.

## Contributing

Feel free to submit issues or pull requests for improvements and features.

## License

This project is licensed under the MIT License.