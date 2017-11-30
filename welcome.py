import discord
from discord.ext import commands

class Welcome:

    """My custom cog that does stuff!"""
    # test

    def __init__(self, bot):
        self.bot = bot

    # Sends a private message to a user that just joined the server
    async def on_member_join(self, member):
        """Adds a game role to gain access to certian channels"""
        print("It worked!")
        msg = "(This is a test message, please ignore for now) Welcome " +member.mention +", please visit <#339228390605193216> for  a bunch of stuff **Lord CommanderDerpy** is god"
        await self.bot.send_message(member, msg)

    @commands.command(no_pm=True, pass_context=True)
    async def games(self, ctx, *, game = ""):
        """Assigns a game role to you so you can view certain channels"""

        listOfGames = ["Rainbow Siege","Warframe"]

        if game == "":
            await self.bot.say("Here is a list of games we support \n" +
                "```" +
                "Rainbow Siege\n" +
                "Warframe\n" +
                "```\n" +
                "Type `!game [name of game]` to gain access to game related channels")
        elif game in listOfGames:
            server = ctx.message.server
            roles = server.roles
            member = ctx.message.author
            role = discord.utils.get(roles, name=game)
            await self.bot.say(role.id)
            await self.bot.add_roles(member, role)
            await self.bot.say("You now have the `" +game +"` role")
        else:
            await self.bot.say("Sorry but that game is not supported here, you can ask us to add it tho.")

    @commands.command(no_pm=True, pass_context=True)
    async def helper(self, ctx):
        """Assigns a game role to you so you can view certain channels"""
        name = ctx.message.author.name
        await self.bot.say(name)
        thing = ctx.message.server
        await self.bot.say(thing.roles)

def setup(bot):
    bot.add_cog(Welcome(bot))
