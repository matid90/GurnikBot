import discord
import cryptocompare
import asyncio
import datetime

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel('channel id')
    while(True):
        embed=discord.Embed(title="Etherum", description=str(cryptocompare.get_price('ETH','USD')['ETH']['USD'])+"$")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/1200px-Ethereum-icon-purple.svg.png")
        embedBTC=discord.Embed(title="Bitcoin", description=str(cryptocompare.get_price('BTC','USD')['BTC']['USD'])+"$")
        embedBTC.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png")
        print(cryptocompare.get_historical_price('BTC', 'EUR', datetime.datetime(2020,6,6)))
        await channel.send(embed=embed)
        await channel.send(embed=embedBTC)
        await asyncio.sleep(10)



client.run('')