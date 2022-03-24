from itertools import count
from operator import contains
import time
from pyrogram import Client

api_id = 17929586
api_hash = "3f983dcbcf5b8e51eebbba3da15e82b4"
message =''''''

with Client("my_account", api_id, api_hash) as app:
    contactss = app.get_contacts()
for contact in contactss : 
    print(contact['first_name'], contact['last_name'])
