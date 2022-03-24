from itertools import count
from operator import contains
import time
from tkinter import Y
from pyrogram import Client

api_id = 17929586
api_hash = "3f983dcbcf5b8e51eebbba3da15e82b4"

with Client("my_account", api_id, api_hash) as app:
    contactss = app.get_contacts()
    counter = 0
    sent = []
    reject = []
    for contact in contactss : 
        if contact["is_mutual_contact"] == True : 
            counter += 1 
            print((contact['first_name'], contact['last_name']))
            res = input("do you want to send message y/n : ")
            if res == "y" :
                message = f"""آرزو دارم سال جدید آغاز روز هایی باشه که آرزو داری 
سال نو مبارک  🌹❤️"""
                app.send_message(contact['id'], message)
                sent.append((contact['first_name'], contact['last_name']))
            elif res == "n":
                reject.append((contact['first_name'], contact['last_name'])) 
            elif res == 'q' :
                print(sent)
                print(reject)
            elif res == "r" :
                message = f"""آرزو دارم سال جدید آغاز روز هایی باشد که آرزو دارید 
سال نو مبارک 🌹❤️"""
                app.send_message(contact['id'], message)
                sent.append((contact['first_name'], contact['last_name']))
print(counter)