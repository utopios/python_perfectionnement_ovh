from threading import Thread

# ma_liste = []

# def ajouter_elements():
#     for _ in range(1000):
#         ma_liste.append(1)

# threads = [Thread(target=ajouter_elements) for _ in range(10)]

# for t in threads: t.start()
# for t in threads: t.join()

# print("Taille réelle : ", len(ma_liste))

import random
# from threading import Thread
import time
# def print_vide():
#     print("Bonjour !")
# def print_avec_texte(text):
#     time.sleep(random.random()*3)
#     print("Mon texte:", text)
# for i in range(3):
#     t = Thread(target= print_vide)
#     t.start()
# for i in range(3):
#     t = Thread(target= print_avec_texte, args= (i,))
#     t.start()

# class LogiqueCustomThread(Thread):
#     def __init__(self, str):
#         super().__init__()
#         self.str = str
#     def run(self):
#         for i in range(6):
#             print(self.str, i)
#             time.sleep(random.random()*3)


# customThread = LogiqueCustomThread("Hello ")
# customThread.start()
# customThread.join()

# ## Lire un fichier texte:
# with open("file.txt", 'r') as ficher:
#     contenu = ficher.read()

from threading import *
from time import sleep
class Railway:
    #Constructor that accepts no. of available berths  
    def __init__(self, available):
        self.available = available
        #Create a lock Object  
        self.lock = Lock()
    def reserve(self, wanted): #A method that reserves berth  
        self.lock.acquire() #lock the current object 
        print("Available no. of berths = ", self.available)
        tName = current_thread().name #Find the thread name 
        if (self.available >= wanted):
            print(f"{wanted} berths are alloted for {tName}")
            sleep(1.5) #Make time delay so that ticket is printed 
            self.available -= wanted #Decrease the number of available berths 
        else:
            #If available < wanted, then say sorry  
            print(tName, ": Sorry, no berths to allot")
        self.lock.release() #Task is completed, release the lock 
 
obj = Railway(2)
t1 = Thread(target = obj.reserve, args = (1, ), daemon=True)  
t2 = Thread(target = obj.reserve, args = (3, ), daemon=True)
t3 = Thread(target = obj.reserve, args = (1, ), daemon=True)
#Give names to the threads  
t1.name = "First Person"
t2.name = "Second Person"
t3.name = "Third Person"
#Start running the threads  
t1.start()
t2.start()
t3.start()