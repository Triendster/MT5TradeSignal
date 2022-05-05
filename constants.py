import MetaTrader5 as mt5

# Numerische Konstanten können je nach Nutzer geändert werden
mt5.initialize()
LEVERAGE        = mt5.account_info().leverage
DPI             = 120
CHART_WIDTH     = 1500
CHART_HEIGHT    = 750

# Gibt an, ob Charts nach Abschluss gesendet werden sollen
SEND_CHART      = False

#Ordnet im Chart-Titel entsprechend des Order-Typs ein Symbol zu
ARROW_DICT      = {mt5.ORDER_TYPE_BUY:'↑', mt5.ORDER_TYPE_SELL:'↓'}

# String Konstanten, die sich auf das zur Anwendung gehörige Dateisystem beschränken
OPEN            = 'open'
HISTORY         = 'history'
LOGS            = 'logs'
SENDS           = 'sends'
JSON            = '.json'
JPEG            = '.jpg'
INIFILE         = '.ini'
LOG             = '.log'

# String Konstanten, die angeben, welche Dateien für Konfiguration und den Endless-Loop verwendet werden
CONFIG          = 'config.ini'
RUN             = 'signal_check.py'

# String Konstanten, die den Typ der Order betreffen und wie dieser in den .json-Dateien angezeigt wird
BUY             = 'BUY'
SELL            = 'SELL'
CHANGE_SLTP     = 'CHANGE_SLTP'
CLOSE           = 'CLOSE'
CLOSE_REASONS   = {
    mt5.DEAL_REASON_CLIENT:'Der Abschluss wurde infolge der Auslösung einer Order ausgeführt, die in einem Desktop-Terminal platziert wurde.',
    mt5.DEAL_REASON_MOBILE:'Der Abschluss wurde infolge der Auslösung einer Order ausgeführt, die in einer mobilen Anwendung platziert wurde.',
    mt5.DEAL_REASON_WEB   :'Der Abschluss wurde infolge der Auslösung einer Order ausgeführt, die auf der Webplattform platziert wurde.',
    mt5.DEAL_REASON_EXPERT:'Der Abschluss wurde infolge der Auslösung einer Order ausgeführt, die durch ein MQL5-Programm - einen Expert Advisor oder ein Script platziert wurde.',
    mt5.DEAL_REASON_SL: 'Der Abschluss wurde infolge der Auslösung von Stop Loss ausgeführt.',
    mt5.DEAL_REASON_TP: 'Der Abschluss wurde infolge der Auslösung von Take Profit ausgeführt.',
    mt5.DEAL_REASON_SO: 'Der Abschluss wurde infolge des Ereignisses Stop Out ausgeführt.',
    mt5.DEAL_REASON_ROLLOVER: 'Der Abschluss wurde infolge der Verschiebung einer Position ausgeführt.',
    mt5.DEAL_REASON_VMARGIN:'Der Abschluss wurde infolge der Anrechnung/Abbuchung der Variation Margin ausgeführt.',
    mt5.DEAL_REASON_SPLIT:'Der Abschluss wurde infolge eines Splits (Preissenkung) eines Symbols, auf welchem im Moment des Splits eine offene Position vorhanden war.'
    }

# String Konstanten, die als Schablone für Signale dienen sollen und Strings, die in den Signalen immer verwendet werden
TYPE_DICT       = {'BUY':'KAUFE', 'SELL':'VERKAUFE'}
PROMOTION       = 'https://cutt.ly/tradecfd'
OPEN_SIGNAL     = u"\U0001F6A6" + 'LIVE TREND' + u"\U0001F6A6" + '\nICH {0} {1} (EK: {2})\nHier traden: {3}'
CLOSE_SIGNAL    = 'ICH SCHLIEßE {0}'  + u"\u2757" + '{1}€ GEWINN' + u"\U0001F389" + u"\U0001F911" + u"\U0001F4C8" + u"\U0001F4C9" + '\nGlückwunsch an alle, die dabei waren' + u"\u2705" + '\nHier kannst du mittraden: {2}'
SLTP_SIGNAL     = 'ICH ÄNDERE MEINE SLTP-SETTINGS BEI {0} WIE FOLGT:\n\nSL: {1}\nTP: {2}'
CHART_SIGNAL    = 'HIER DAS ENTSPRECHENDE CHART:'
