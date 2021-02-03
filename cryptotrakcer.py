import discord
import cryptocompare
import asyncio
import datetime
import json

client = discord.Client()

config = {}
channel_id=0
token = ''
with open('config.json') as f:
        config = json.load(f)
        channel_id = config['channel_id']
        token = config['token']

@client.event
async def on_ready():        

    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(channel_id)
    while(True):
        embed=discord.Embed(title="Etherum", description=str(cryptocompare.get_price('ETH','USD')['ETH']['USD'])+"$")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png")
        embed.add_field(name = "24h change ",value=str(cryptocompare.get_price('ETH','USD')['ETH']['USD']/(cryptocompare.get_historical_price('ETH', 'USD', datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day-1))['ETH']['USD']))[:4]+"%", inline=False)
        embedBTC=discord.Embed(title="Bitcoin", description=str(cryptocompare.get_price('BTC','USD')['BTC']['USD'])+"$")
        embedBTC.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png")
        await channel.send(embed=embed)
        await channel.send(embed=embedBTC)
        await asyncio.sleep(60)


client.run(token)