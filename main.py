import discord
import requests
from threading import Timer
from keep_alive import keep_alive
import os
from decimal import Decimal
import decimal
from time import sleep
import requests
import json
from rate import rate
import math
    
# print(my_dic)


client = discord.Client()

@client.event
async def on_ready():
  print("Bot is connected. Logged in as {0.user}".format(client))
@client.event
async def on_message(message):
  inp_name = message.content
  



  if inp_name.startswith("/set"):
    set_coin = list(inp_name.split(" "))
    # print(set_coin[1])
    try:
      await message.channel.send(f">Price for {set_coin[1]} set at ₹  {set_coin[2]}\n")
      for i in range(1000000):
          alert_dic = {}
          url = "https://api.coincap.io/v2/assets"
          payload={}
          headers = {}

          response = requests.request("GET", url, headers=headers,      data=payload)

          # print(response.text.encode("utf8"))

          response_json = response.json()

          response_json
          for i in range(100):
              name = response_json['data'][i]['id']
              price = response_json['data'][i]['priceUsd']
              # converts usd to inr
              inr_price = decimal.Decimal(price) * rate
              # print(f"Name: {name} , Rate: {inr_price}")
              inr_price = float(inr_price)
              alert_dic.update({name:inr_price})
          if float(set_coin[2]) < float(alert_dic[set_coin[1]]):
            await message.channel.send(f">Buy {set_coin[1]} at ₹{alert_dic  [set_coin[1]]}")
            break
          sleep(10)
    except:
      await message.channel.send(f">Sorry I don't understand")

  

  elif inp_name.startswith("/help"):
    await message.channel.send("""
    >To set buy price alert -> /set coin price\n>To show top coin prices -> /showtop num\n>To watch price of a coin -> $coin num timeinterval  
    """)



  elif inp_name.startswith("/showtop"):
    top_num = list(inp_name.split(" "))
    await message.channel.send(f">Showing top {top_num[1]} coins")
    price_dic = {}
    url = "https://api.coincap.io/v2/assets"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text.encode("utf8"))
    response_json = response.json()
    response_json
    num = int(top_num[1])
    for i in range(num):
        name = response_json['data'][i]['id']
        price = response_json['data'][i]['priceUsd']
        # converts usd to inr
        inr_price = decimal.Decimal(price) * rate
        final = "{0:.3f}".format(inr_price)
        await message.channel.send(f">Name: {name} , Rate: ₹{final}")
        # print(f"Name: {name} , Rate: {inr_price}")
        inr_price = float(inr_price)
        price_dic.update({name:inr_price})
      
    
  
      
  if inp_name.startswith("$"):
    inp_name = message.content
    set_lst = list(inp_name.split(" "))
    num = int(set_lst[1])
    try:
      for i in range(num):
        my_dic = {}
        url = "https://api.coincap.io/v2/assets"
        payload={}
        headers = {}
  
        response = requests.request("GET", url, headers=headers,    data=payload)
  
        # print(response.text.encode("utf8"))
  
        response_json = response.json()
  
        response_json
        for i in range(100):
            name = response_json['data'][i]['id']
            price = response_json['data'][i]['priceUsd']
            # converts usd to inr
            inr_price = decimal.Decimal(price) * rate
            # print(f"Name: {name} , Rate: {inr_price}")
            inr_price = float(inr_price)
            my_dic.update({"$"+name:inr_price})
  
        if message.author == client.user:
          return
        
        else:
          await message.channel.send(f">Price = ₹{my_dic[set_lst[0]]}")

        print(f"Price = {my_dic[set_lst[0]]}")
        sleep(int(set_lst[2]))
    # get_crypto(inp_name=inp_name, message=message)
    except:
      await message.channel.send("""
      >Sorry I cannot understand

      >coin num sleep
      """)


keep_alive()

BOT_TOKEN = os.environ['TOKEN']
client.run(BOT_TOKEN)
