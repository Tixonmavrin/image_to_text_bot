# python-telegram-bot library
from telegram import Update, ForceReply, File
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# google library for communication with google vision api
from google.oauth2 import service_account
from google.cloud import vision

# ocr_api.py file, work with google vision api
from .ocr_api import Ocr


class Commands:
    """Telegram bot commands"""

    @staticmethod
    def start_command(update: Update, _: CallbackContext) -> None:
        """Send a message when user cliked /start"""

        # Get user info
        user = update.effective_user

        # Send message
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\! Send me picture that contains text',
        )

    @staticmethod
    def help_command(update: Update, _: CallbackContext) -> None:
        """Send a message when user cliked /help"""

        # Send message
        update.message.reply_text('To get started, just send me a picture containing text in any language')

    @staticmethod
    def text_command(update: Update, _: CallbackContext) -> None:
        """Reply to user message"""

        # Send message
        update.message.reply_text('To get started, just send me a picture containing text in any language')

    @staticmethod
    def document_command(update: Update, _: CallbackContext) -> None:
        """Get text (from document) from google vision and return it to user"""

        # Get text from google vision api
        text = Ocr.get_text_from_image(update.message.document.get_file())

        # Send message
        if not text:
            # If image is empty or file is not correct
            update.message.reply_text("Please, try again...")
        else:
            update.message.reply_text(text)

    @staticmethod
    def image_command(update: Update, _: CallbackContext) -> None:
        """Get text (from image) from google vision and return it to user"""

        # Get text from google vision api
        text = Ocr.get_text_from_image(update.message.photo[-1].get_file())

        # Send message
        if not text:
            # If image is empty or file is not correct
            update.message.reply_text("Please, try again...")
        else:
            update.message.reply_text(text)


def start(args: dict) -> None:
    """Start the bot and google api connection"""

    # Connect to telegram. Get updater
    updater = Updater(token=args['telegram_key'])
    dispatcher = updater.dispatcher

    # Add command handlers - simple text answers
    dispatcher.add_handler(CommandHandler("start", Commands.start_command))
    dispatcher.add_handler(CommandHandler("help", Commands.help_command))

    # Add message handlers - simple answer for text message
    # Use google's api for image or doc message
    dispatcher.add_handler(MessageHandler(Filters.text, Commands.text_command))
    dispatcher.add_handler(MessageHandler(Filters.document, Commands.document_command))
    dispatcher.add_handler(MessageHandler(Filters.photo, Commands.image_command))

    # Connect to google vision api
    credentials = service_account.Credentials.from_service_account_file(args['google_keys_json_path'])
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # Add client field to Ocr class
    Ocr.client = client

    # Start the bot
    updater.start_polling()

    # Gracefully stop the bot on errors
    updater.idle()
