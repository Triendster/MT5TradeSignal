import signalclient as sc
import open_positions
import close_positions
import datetime
import os
import constants
import logging

'''Voller Durchlauf zum Erstellen von Signalen, Fehler werden in logs hinterlegt'''
try:
    client = sc.SignalClient()
    open_positions.manage_open_positions(client)
    close_positions.manage_close_positions(client)
except Exception as Argument:
    filename = os.path.join(os.getcwd(), constants.LOGS, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3] + constants.LOG)
    print(Argument)
    with open(filename, 'w') as errorFile:
        errorFile.write(str(Argument))
