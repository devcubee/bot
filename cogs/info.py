import discord
import datetime
from discord.ext import commands
from discord.app_commands import command

class Info(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client
    

  @command(name="ping", description="Get the current ping")
  async def info(self, interaction: discord.Interaction):
    embed = discord.Embed(title='Pong!')
    embed.add_field(name='Current latency', value=f'{round(self.client.latency * 1000)}ms', inline=True)
    embed.colour = discord.Colour.blurple()
    embed.timestamp = datetime.datetime.now()
    embed.set_footer(text="Information requested by: {}".format(interaction.user.display_name))
    embed.set_author(name=self.client.user.display_name, icon_url=self.client.user.avatar)

    await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Info(client))