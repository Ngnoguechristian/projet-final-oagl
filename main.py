from tkinter import *

from pages.connexion.login import Login

windows = Tk()
# dinmensionner sa fenetre
windows.geometry("1000x600+200+40")

# changer le titre de la fenetre
windows.title('Gestion de taches')

# zone des pages de l'app
page = Canvas(windows,width=1000,height=600)

# transition pour le login
Login(page,1000,600)

page.place(x=0,y=0)

# afficher la fenetre
windows.mainloop()
