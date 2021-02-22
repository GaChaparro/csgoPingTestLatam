###############################################################################
#  _____  _____  _____  ____    _____ _                                       #
# / ____|/ ____|/ ____|/ __ \  |  __ (_)                                      #
#| |    | (___ | |  __| |  | | | |__) | _ __   __ _                           #
#| |     \___ \| | |_ | |  | | |  ___/ | '_ \ / _` |                          #
#| |____ ____) | |__| | |__| | | |   | | | | | (_| |                          #
# \_____|_____/ \_____|\____/  |_|   |_|_| |_|\__, |                          #
#                                              __/ |                          #
#                                             |___/                           #
# _______        _                                                            #
#|__   __|      | |                                                           #
#   | | ___  ___| |_ ___ _ __                                                 #
#   | |/ _ \/ __| __/ _ \ '__|                                                #
#   | |  __/\__ \ ||  __/ |                                                   #
#   |_|\___||___/\__\___|_|                                                   #
#                                                                             #
###############################################################################

#Esta Version es apenas una vil copia del proyecto original:
#https://defirence.github.io/CSGO-Ping-Tester/
#Solamente me base en el codigo, y el resto en la configuración publica de SteamDataBase en Github:
#https://github.com/SteamDatabase/SteamTracking/blob/master/Random/NetworkDatagramConfig.json
#Todos los derechos a su respectivo creador
#Esto es solo una forma de testear nuestro ping en lo servidores oficiales de MM de CSGO
#Hecha para y por la comunidad



from tkinter import *
import tkinter.messagebox
import os


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title('CSGO Ping Tester v0.01 by Fullbrito')

        self.pack(fill=BOTH, expand=1)

        #  button label length determines button size
        #Boton de exit no funciona

        """ quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=514, y=0) """

         ##############################
        # BUTTONS FOR VALVE FUNCTIONS #
         ##############################

        eseagermanytwoButton = Button(self, text="Valve MM Buenos Aires", command=self.valve_eze_one)
        eseagermanytwoButton.place(x=0, y=0)

        gboneButton = Button(self, text="Valve MM Sao Paulo", command=self.valve_gru_one)
        gboneButton.place(x=0, y=24)

        gbtwoButton = Button(self, text="Valve MM Santiago", command=self.valve_scl_one)
        gbtwoButton.place(x=0, y=48)

        francetwoButton = Button(self, text="Valve MM Lima", command=self.valve_lim_one)
        francetwoButton.place(x=0, y=72)



    ###############################
    # VALVE MATCHMAKING FUNCTIONS #
    ###############################

    def valve_eze_one(self):

        print("Pinging Valve Buenos Aires 1 Relay")
        hostname = "155.133.255.98"
        response = os.system("ping " + hostname)
        if response == 0:
            result = "Ping Successful"
        else:
            result = "Ping Unsuccessful"
        tkinter.messagebox.showinfo("Complete", result)

    def valve_gru_one(self):

        print("Pinging Valve Sao Paulo Relay 1")
        hostname = "205.185.194.34"
        response = os.system("ping " + hostname)
        if response == 0:
            result = "Ping Successful"
        else:
            result = "Ping Unsuccessful"
        tkinter.messagebox.showinfo("Complete", result)

    def valve_scl_one(self):

        print("Pinging Valve Santiago Relay 1")
        hostname = "155.133.249.162"
        response = os.system("ping " + hostname)
        if response == 0:
            result = "Ping Successful"
        else:
            result = "Ping Unsuccessful"
        tkinter.messagebox.showinfo("Complete", result)

    def valve_lim_one(self):

        print("Pinging Valve Lima Relay 1")
        hostname = "190.217.33.34"
        response = os.system("ping " + hostname)
        if response == 0:
            result = "Ping Successful"
        else:
            result = "Ping Unsuccessful"
        tkinter.messagebox.showinfo("Complete", result)

    def client_exit(self):
        sys.exit()


root = Tk()
root.geometry("400x150")
app = Window(root)
root.mainloop()

# Thanks for using my program
