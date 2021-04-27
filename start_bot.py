# Library for command line arguments parsing
import argparse

# Import our library
import image_to_text_bot

if __name__ == "__main__":
    # Parse arguments (keys for telegram and google cloud)
    parser = argparse.ArgumentParser(description="Image-to-text telegram bot")
    parser.add_argument(
        "--telegram_key", type=str, default="", help="Telegram key from BotFather"
    )
    parser.add_argument(
        "--google_keys_json_path",
        type=str,
        default="google_keys.json",
        help="Path to json file from google cload vision api",
    )
    args = parser.parse_args()

    # Start the bot, add google vision api connection
    image_to_text_bot.start(args.__dict__)
