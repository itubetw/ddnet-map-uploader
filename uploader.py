import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Set the path where you want to save the file.. Example:
save_path = '/home/itube/ddnet/build/data/maps/'

# Only People with the role 'Mapper' can upload maps
def has_mapper_role(ctx):
    return discord.utils.get(ctx.guild.roles, name='Mapper') in ctx.author.roles

@bot.command()
@commands.check(has_mapper_role)
async def save_file(ctx, *, file: discord.Attachment):
    try:
        await file.save(save_path + file.filename)
    except Exception as e:
        print(e)
        await ctx.send('An error occurred while saving the file.')
    else:
        await ctx.send(f'File saved to {save_path}')

# Run the bot
bot.run('your-token')
