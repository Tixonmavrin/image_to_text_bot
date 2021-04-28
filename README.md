# Image to text telegram bot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<a href="https://github.com/Tixonmavrin/image_to_text_bot/actions"><img alt="Actions Status" src="https://github.com/Tixonmavrin/image_to_text_bot/workflows/Test/badge.svg"></a>
<a href="https://github.com/Tixonmavrin/image_to_text_bot/actions"><img alt="Actions Status" src="https://github.com/Tixonmavrin/image_to_text_bot/workflows/Lint/badge.svg"></a>
<a href="https://github.com/Tixonmavrin/image_to_text_bot/actions"><img alt="Actions Status" src="https://github.com/Tixonmavrin/image_to_text_bot/workflows/Changelog/badge.svg"></a>

# Get started
```
python3 -m venv --system-site-packages ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python start_bot.py --telegram_key YOUR_TELEGRAM_KEY --google_keys_json_path YOUR_GOOGLE_KEYS_JSON_PATH
deactivate
rm -rf venv
```

# Options
```
python main.py --telegram_key 123:AA_BB_CC_DD \
               --google_keys_json_path google_keys.json
```
- telegram_key: telegram api key for your bot. Write @BotFather in telegram to get it.
- google_keys_json_path: google cloud vision api keys json file path (you can download json file from their site).

# Requirements
```
google-cloud-vision==2.3.1
python-telegram-bot==13.4.1
```
