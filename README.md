# simple-tg-bot

## Requirements

Python 3.12.5

## Launch

Clone and install:
```
git clone https://github.com/cianoid/domclick-tg-bot.git
cd domclick-tg-bot/

python3.12 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.template .env
```

Fill up .env file with your bot token (you should get it from @BotFather)

Now launch bot with command:
`python -m app`
