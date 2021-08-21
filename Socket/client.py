# coding: utf-8

import socket
from tkinter import *
from tkinter.messagebox import *

#address and port
hote = "localhost"
port = 15556

#socket config
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hote, port))


#téléchargement
def getFile():
    res = myEntry.get()
    if res != '':
        myEntry.delete(0, END)
        file_name = res
        s.send(file_name.encode())
        trouve = s.recv(255).decode("utf-8")
        if trouve == 'T':
            file_name = 'dataClient/%s' % (file_name,)
            r = s.recv(9999999)
            with open(file_name, 'wb') as _file:
                _file.write(r)
            label = Label(frame, text="Le fichier a été correctement copié dans : %s" % file_name)
            label.pack()
            label.after(5000, lambda: label.destroy())
        elif trouve == 'F':
            showwarning('Error', 'Aucun fichier trouvé avec ce nom, réessayez !')
    else:
        showwarning('Error', 'Aucun nom entré, réessayez !')




#gui

#design
client = Tk()
client.minsize(400, 150)
client.maxsize(400,150)
client.title("Client side")
client.tk.call('wm', 'iconphoto', client._w, PhotoImage(file='dataClient/img/client.png'))
#client.config(background='code couleur')

#frame
frame = Frame(client)

#label
label = Label(frame, text="Entrez le nom du fichier demandé")

#entrée
valeur = StringVar()
myEntry = Entry(frame, textvariable=valeur, width=30)

#button
btn1 = Button(frame, height=1, width=10, text="Télécharger", command=getFile)

#affichage
label.pack()
myEntry.pack(pady=10)
btn1.pack(pady=10)
frame.pack(expand=YES)
client.mainloop()