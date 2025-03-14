from rubpy import Client, filters

from rubpy.types import Update

import requests as r



app = Client('h_o')





@app.on_message_updates(filters.is_private)

def jok(m:Update):

 if m.text=="جوک":

     a = r.get('https://alanbecker.pythonanywhere.com/webservices/jok').json()['result']

     m.reply(f"{a}")

     

@app.on_message_updates(filters.is_private)

def random_music(m:Update):

 if m.text=="بیو":

     a = r.get('https://alanbecker.pythonanywhere.com/webservices/bio').json()['result']

     m.reply(f"{a}") 

     

app.run()
