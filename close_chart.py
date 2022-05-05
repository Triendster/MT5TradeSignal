import MetaTrader5 as mt5
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import time
import constants
import os
from open_positions import initialize_mt5

# Hiermit soll ein Bild des Charts generiert werden
def create_close_chart(cp):
    register_matplotlib_converters()
    initialize_mt5()

    # Wichtig für korrekte Anzeige
    type = 'bid' if cp[0].type == mt5.ORDER_TYPE_BUY else 'ask'
    title = cp[0].symbol + constants.ARROW_DICT[cp[0].type] + '\n' + str(cp[1].volume) + ' × ' + str(constants.LEVERAGE)

    # Um ein Chart zu erzeugen, greife auf die Tickdaten des Symbols im Zeitraum des Trades zu, lege daraus einen Dataframe an
    dt1 = datetime.datetime.fromtimestamp(cp[0].time)
    dt2 = datetime.datetime.fromtimestamp(cp[1].time)
    ticks = mt5.copy_ticks_range(cp[0].symbol, dt1, dt2, mt5.COPY_TICKS_ALL)
    ticks_frame = pd.DataFrame(ticks)
    ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')

    # Erzeuge Figur und lege Einstellungen fest
    fig = plt.figure(figsize=(constants.CHART_WIDTH/constants.DPI, constants.CHART_HEIGHT/constants.DPI), dpi=constants.DPI)
    ax  = fig.add_subplot(1, 1, 1)
    plt.rcParams['savefig.facecolor'] = "0.15"
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.xaxis.label.set_color('yellow')
    ax.yaxis.label.set_color('yellow')
    ax.set_facecolor((0.15, 0.15, 0.15))
    ax.tick_params(axis='x', colors='yellow')
    ax.tick_params(axis='y', colors='yellow')
    ax.set_xlabel('ZEIT')
    ax.set_ylabel(type.upper())
    ax.set_title(title, fontsize=15, color='white', fontweight='bold')

    # Diese Werten dienen zur Reduzierung des Darstellungsbereiches
    be = cp[0].price
    d = (ticks_frame[type].max() - be) if type == 'ask' else (be - ticks_frame[type].min())
    pad = (ticks_frame[type].max() - ticks_frame[type].min()) * 0.5
    plt.ylim(be - d - pad, be + d + pad)

    # Eigentlicher Plot der entsprechenden Preislinie, Buy-Order -> Bid, Sell-Order -> Ask
    plt.plot(ticks_frame['time'], ticks_frame[type], 'y-', linewidth=2.5)

    # Dient zum Färben der Bereiche unter der Kurve, falls Profit negativ -> rot, positiv -> grün
    if type == 'bid':
        plt.fill_between(
            ticks_frame['time'],
            ticks_frame[type],
            where =  ticks_frame[type] <= cp[0].price,
            color = 'r',
            alpha = 0.15,
        )
        plt.fill_between(
            ticks_frame['time'],
            ticks_frame[type],
            where =  ticks_frame[type] > cp[0].price,
            color = 'g',
            alpha = 0.15,
        )
    else:
        plt.fill_between(
            ticks_frame['time'],
            ticks_frame[type],
            where =  ticks_frame[type] >= cp[0].price,
            color = 'r',
            alpha = 0.15,
        )
        plt.fill_between(
            ticks_frame['time'],
            ticks_frame[type],
            where =  ticks_frame[type] < cp[0].price,
            color = 'g',
            alpha = 0.15,
        )

    # Die Linie die den Einstiegspreis und Break Even Point darstellt (wenn der Spread überwunden wird)
    plt.axhline(y=be, color='r', linestyle='--', label='Einstiegspreis', linewidth=4)

    # Anzeigen des Charts
    plt.grid(True)
    plt.legend(loc='upper left')

    # Dateipfad des Charts wird in .json-Datei bei Abschluss der Position abgespeichert
    filepath = os.path.join(os.getcwd(), constants.SENDS, 'jpg', str(abs(hash(str(time.time())))) + constants.JPEG)
    fig.savefig(filepath, dpi=constants.DPI)
    return filepath
