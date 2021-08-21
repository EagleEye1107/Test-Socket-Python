from tkinter import *
from tkinter.messagebox import *

phase = 0 #0 recherche, 1 téléchargement


def getEntry():
    global res
    res = myEntry.get()
    if res != '':
        myEntry.delete(0, END)
    else:
        showwarning('Error', 'Aucun nom entré, réessayez !')


'''
def getFile(trouve):
    # trouve viens du coté serveur
    if trouve:
        print()
    else:
        showwarning('Error', 'Aucun fichier trouvé, réessayez !')
'''

'''
#if trouvé
print("Fichier trouvé, voulez-vous le télécharger ?")
bouton2=Button(fenetre, text="Télécharger")
bouton2.pack()

#else
print("Fichier introuvable")
'''



#design
client = Tk()
client.geometry("300x100")
client.minsize(300, 150)
client.maxsize(300,150)
client.title("Client side")
client.tk.call('wm', 'iconphoto', client._w, PhotoImage(file='img/client.png'))
#client.config(background='code couleur')

#frame
frame = Frame(client)

#label
label = Label(frame, text="Entrez le nom du fichier demandé")

#entrée
valeur = StringVar()
myEntry = Entry(frame, textvariable=valeur, width=30)

#button
btn1 = Button(frame, height=1, width=10, text="Rechercher", command=getEntry)\

#affichage
label.pack()
myEntry.pack(pady=10)
btn1.pack(pady=10)
frame.pack(expand=YES)
client.mainloop()

print(res)