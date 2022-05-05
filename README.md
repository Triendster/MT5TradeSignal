# MT5TradeSignalSender

## Automatically gather both opened and closed positions from the MT5 terminal and send them as a signal to a Telegram channel.

### Note that this project is intended for usage with Windows 10 or any other platform that has the MetaTrader5.

Navigate to the directory where you stored this repo and start by installing all the packages necessary for the project to work:

```
pip install -r requirements.txt
```

Create necessary directories by running: 

```
python makedirs.py
```

In order to use this application, you need to create a Telegram Application. In order to do that, visit the following [page](https://core.telegram.org/api/obtaining_api_id).

Once you've created an application, gather your app data and change ```config.ini``` accordingly.
If you do not know your channel id, use [this](https://t.me/jsondumpbot) TelegramBot to find out. 

Note that the MetaTrader5 has to be open to use this application, and AlgoTrading has to be enabled. To do that, press ```CTRL + E```.

Now, you're pretty much ready to go. Navigate to the directory and excecute:

```
python loop.py
```

This script will run indefinitely. Errors will be written to ```logs```.
In order to stop this script, either close the terminal window or press ```CTRL + C```.

If this is your first time running ```loop.py```, you will be asked to enter your phone number and a verification code Telegram sent to you by Telegram upon starting the script.


If you want to reset your history, you can do so by executing:

```
python clear.py
```

This will delete all folders and files inside them.

Regarding to the contens of ```constants.py```, you can change them, according to your needs. 

