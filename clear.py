import os
import shutil
import constants

# Lösche alle Ordner, zum Beispiel für Reset beim Debuggen, etc.
if os.path.exists(os.path.join(os.getcwd(), constants.OPEN)):
    shutil.rmtree(os.path.join(os.getcwd(), constants.OPEN))

if os.path.exists(os.path.join(os.getcwd(), constants.HISTORY)):
    shutil.rmtree(os.path.join(os.getcwd(), constants.HISTORY))

if os.path.exists(os.path.join(os.getcwd(), constants.LOGS)):
    shutil.rmtree(os.path.join(os.getcwd(), constants.LOGS))

if os.path.exists(os.path.join(os.getcwd(), constants.SENDS, 'json')):
    shutil.rmtree(os.path.join(os.getcwd(), constants.SENDS, 'json'))

if os.path.exists(os.path.join(os.getcwd(), constants.SENDS, 'jpg')):
    shutil.rmtree(os.path.join(os.getcwd(), constants.SENDS, 'jpg'))

if os.path.exists(os.path.join(os.getcwd(), constants.SENDS)):
    shutil.rmtree(os.path.join(os.getcwd(), constants.SENDS))
