import MetaTrader5 as mt5
import os
import constants
import signalclient
import json
from open_positions import initialize_mt5, return_description
from open_positions import return_JSON_filepath
from pathlib import Path
from close_chart import create_close_chart
import hashlib
import binascii

def return_diff_positions(op_list):
    '''Diese Funktion gibt eine int-Liste der Tickets zurück, die in 'open' sind, aber nicht unter den offenen Positionen im Mt5'''
    path               = os.path.join(os.getcwd(), constants.OPEN)
    op_local_positions = [int(Path(os.path.join(path, p)).stem) for p in os.listdir(path)]
    return list(set(op_local_positions) - set(op_list))

def to_position_dict(history_position):
    position_file_dict = {
        'id'         : history_position[0].order,
        'send_id'    : binascii.hexlify(hashlib.sha256(bytes(str(history_position[0].order), 'ascii')).digest()).decode('ascii')[:31],
        'volume'     : history_position[0].volume,
        'price_open' : history_position[0].price,
        'price_close': history_position[1].price,
        'type'       : constants.CLOSE,
        'symbol'     : history_position[0].symbol,
        'profit'     : history_position[1].profit,
        'reason'     : constants.CLOSE_REASONS[history_position[1].reason],
        'description': return_description(history_position[0]),
        'otype'      : history_position[1].type,
        'chart'      : create_close_chart(history_position) if constants.SEND_CHART else None,
    }
    return position_file_dict

def manage_close_positions(client : signalclient.SignalClient):
    '''Öffne alle geöffneten Positionen im MetaTrader5 und vergleiche diese anschließend mit Positionen in 'open' '''
    initialize_mt5()
    open_positions = mt5.positions_get()
    op_list = [op.ticket for op in open_positions]
    closed_positions = return_diff_positions(op_list)
    for cp in closed_positions:
        history_position = mt5.history_deals_get(position=cp)
        position_dict = to_position_dict(history_position)
        position_filepath = return_JSON_filepath(cp, constants.HISTORY)
        with open(position_filepath, 'w') as writePosition:
            json.dump(position_dict, writePosition, indent=6)
        os.remove(return_JSON_filepath(cp, constants.OPEN))
        client.run_send_signal(position_filepath, False, True)
