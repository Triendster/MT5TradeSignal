import configparser
import constants

class ConfigData:
    '''Diese Klasse liest die Informationen aus der Konfigurationsdatei aus'''
    def __init__(self, configfile):
        self.configfile = configfile
        self.set_config_data()
    def set_config_data(self):
        # Check if the specified file is a configuration file
        if constants.INIFILE in self.configfile:
            config      = configparser.ConfigParser()
            config.read(self.configfile)
            self.config = config
            self.api_id = int(self.config['Telegram']['api_id'])
            self.api_hash = self.config['Telegram']['api_hash']
            self.channel_id = int(self.config['Telegram']['channel_id'])
            self.discuss_id = int(self.config['Telegram']['discuss_id'])
            self.phone = self.config['Telegram']['phone']
            self.username = self.config['Telegram']['username']
        else:
            print('Falscher Dateityp.')
