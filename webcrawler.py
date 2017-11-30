import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False

import aiohttp

class WebCrawler:

    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def WarframeEvent(self):
        """How many players are online atm?"""
        url = "http://warframe.wikia.com/wiki/Category:Event" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:

            parent = soupObject.find_all('dl')
            last = len(parent) - 1
            
            # print(last)
            # print(parent[last])

            eventTitle = parent[last].find('dt').get_text()
            # print("1: " +eventTitle)

            eventTime = parent[last].find('i').get_text()
            # print("2: " +eventTime)

            eventDesc = parent[last].find_all('dd')[1].get_text()
            # print("3: " +eventDesc)

            await self.bot.say("**Event Title:** " +eventTitle +"\n"
            	+"**Event Timeline:** " +eventTime +"\n"
            	+"**Event Description:** " + eventDesc)
        except:
            await self.bot.say("There was an error")

def setup(bot):
    bot.add_cog(WebCrawler(bot))

   