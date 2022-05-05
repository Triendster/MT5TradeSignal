from subprocess import Popen
import constants

filename = constants.RUN
while True:
    p = Popen("python " + filename, shell=True)
    p.wait()
