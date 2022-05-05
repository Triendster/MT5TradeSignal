import MetaTrader5 as mt5
import os
import constants
import signalclient
import json
import random
import hashlib
import binascii

# Gib Beschreibung für Signal-Nachricht zurück
def return_description(position):
    position_info = mt5.symbol_info(position.symbol).description
    return position_info.upper()

# Überprüfe, ob der Mt5 geöffnet ist, falls nicht gebe Fehlercode aus
def initialize_mt5():
    if not mt5.initialize():
        print("initialize() fehlgeschlagen, Fehlercode =",mt5.last_error())
        quit()

# Generiere Dateipfad für Positionen in 'open'
def return_JSON_filepath(ticket, path):
    filename = str(ticket) + constants.JSON
    return os.path.join(os.getcwd(), path, filename)


# Erzeuge Transaktionswörter (0->Buy, 1->Sell)
def return_type(type):
    if type == mt5.ORDER_TYPE_BUY:
        return constants.BUY
    else:
        return constants.SELL

# Erzeuge Position in 'open'
def to_position_dict(position):
    position_file_dict = {
        'id'         : position.identifier,
        'send_id'    : binascii.hexlify(hashlib.sha256(bytes(str(position.identifier), 'ascii')).digest()).decode('ascii')[:31],
        'volume'     : position.volume,
        'price_open' : position.price_open,
        'sl'         : position.sl,
        'tp'         : position.tp,
        'type'       : return_type(position.type),
        'otype'      : position.type,
        'symbol'     : position.symbol,
        'description': return_description(position),
    }
    return position_file_dict

# Überprüfe alle geöffneten Positionen im Handelsfenster des MT5
# Falls Positionen mit Tickets geöffnet wurden, die nicht in "open" enthalten sind, füge diese hinzu
# Falls Änderungen gemacht wurden, durch Ändern des TP/SL,
def manage_open_positions(client : signalclient.SignalClient):
    initialize_mt5()
    open_positions = mt5.positions_get()
    if not open_positions:
        return
    for op in open_positions:
        position_filepath = return_JSON_filepath(op.ticket, constants.OPEN)
        position_dict     = to_position_dict(op)
        # Falls die Position noch geöffnet werden muss
        if not os.path.isfile(position_filepath):
            with open(position_filepath, 'w') as writePosition:
                json.dump(position_dict, writePosition, indent=6)
            client.run_send_signal(position_filepath, False, False)
        else:
            with open(position_filepath, 'r') as readPosition:
                ref_position = json.load(readPosition)
            if position_dict == ref_position:
                continue
            else:
                # In diesem Fall wurde der SLTP geändert
                with open(position_filepath, 'w') as writePosition:
                    json.dump(position_dict, writePosition, indent=6)
                client.run_send_signal(position_filepath, True, False)
