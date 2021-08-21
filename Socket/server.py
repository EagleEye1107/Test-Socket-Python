# coding: utf-8

import os
import socket
import threading


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 15556))


def connect():
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    print("Connected")
    newthread.start()



class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))


    def run(self):
        while True:
            print("Connexion de %s %s" % (self.ip, self.port,))
            print("Verify the presence of the file")
            file_name = self.clientsocket.recv(2048).decode("utf-8")
            e = os.path.exists('dataServer/%s' %file_name)
            if e:
                self.clientsocket.send("T".encode())
                r = 'dataServer/%s' %file_name
                print("Ouverture du fichier: ", r, "...")
                fp = open(r, 'rb')
                self.clientsocket.send(fp.read())
                print("Client déconnecté...")
            else:
                self.clientsocket.send("F".encode())
                print("Fichier introuvable.")




while True:
    connect()