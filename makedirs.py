import os
import constants


os.mkdir(os.path.join(os.getcwd(), constants.OPEN))
os.mkdir(os.path.join(os.getcwd(), constants.HISTORY))
os.mkdir(os.path.join(os.getcwd(), constants.LOGS))
os.mkdir(os.path.join(os.getcwd(), constants.SENDS))
os.mkdir(os.path.join(os.getcwd(), constants.SENDS, 'json'))
os.mkdir(os.path.join(os.getcwd(), constants.SENDS, 'jpg'))
