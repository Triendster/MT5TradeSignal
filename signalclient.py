import configurator
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import PeerChannel
import asyncio
import constants
import json
import time
import os

class SignalClient:
    '''Klasse die den Client enthält und Signale in die Gruppe postet'''
    def __init__(self):
        # Liest Konfigurationsdatei aus und speichert Werte wie api_id in self.config_data.api_id
        self.config_data = configurator.ConfigData(constants.CONFIG)
        self.client      = TelegramClient(self.config_data.username, self.config_data.api_id, self.config_data.api_hash)
    async def send_signal(self, position_filepath, sltp, close):
        # Wandle .json-Datei am angegebenen Pfad in Signal für Telegram um
        await self.client.start()
        print('Client erfolgreich gestartet...')
        # Authorisierung gewährleisten
        if await self.client.is_user_authorized() == False:
            await self.client.send_code_request(self.config_data.phone)
            try:
                await self.client.sign_in(self.config_data.phone, input('Bitte den Code von Telegram eingeben: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Passwort: '))
        channel= await self.client.get_entity(PeerChannel(self.config_data.channel_id))
        dis_ch = await self.client.get_entity(PeerChannel(self.config_data.discuss_id))
        send_dict = {}
        with open(position_filepath, 'r') as positionRead:
            position_data = json.load(positionRead)
        if sltp:
            send_dict['type'] = constants.CHANGE_SLTP
            send_dict['otype']= position_data['otype']
            send_dict['sl'], send_dict['tp'] = position_data['sl'], position_data['tp']
            message = constants.SLTP_SIGNAL.format(
            position_data['description'],
            position_data['sl'],
            position_data['tp']
            )

        elif close:
            send_dict['type'] = position_data['type']
            send_dict['otype']= position_data['otype']
            message = constants.CLOSE_SIGNAL.format(
            position_data['description'],
            position_data['profit'],
            constants.PROMOTION
            )
        else:
            send_dict['type'] = position_data['type']
            message = constants.OPEN_SIGNAL.format(
            constants.TYPE_DICT[position_data['type']],
            position_data['description'],
            position_data['price_open'],
            constants.PROMOTION
            )
        send_dict['symbol'] = position_data['symbol']
        send_dict['send_id']= position_data['send_id']
        send_filepath = os.path.join(os.getcwd(), constants.SENDS, 'json', str(abs(hash(str(time.time())))) + constants.JSON)
        with open(send_filepath, 'w') as writeSend:
            json.dump(send_dict, writeSend, indent=6)
        if not close:
            await self.client.send_message(channel, message, file=send_filepath, link_preview=False)
        else:
            await self.client.send_message(channel, message, file=send_filepath, link_preview=False)
            if constants.SEND_CHART:
                await self.client.send_message(dis_ch, constants.CHART_SIGNAL, file=position_data['chart'])

    def run_send_signal(self, position_filepath, sltp, close):
        with self.client:
            self.client.loop.run_until_complete(self.send_signal(position_filepath, sltp, close))
