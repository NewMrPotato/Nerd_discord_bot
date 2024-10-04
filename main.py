t = 'TOKEN'

# Libs for bots
import asyncio

# Libs for api discord
import discord
from discord.ext import commands


if __name__ == '__main__':
    # Создайте объект Intents с включенными необходимыми событиями
    intents = discord.Intents.default()
    intents.members = True  # Включите отслеживание событий о членах сервера

    client = commands.Bot(command_prefix='?', intents=intents)

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    #@commands.has_permissions(administrtor=True)
    async def clear(ctx, amount=10):
        await ctx.channel.purge(limit=amount)

    @client.event
    async def on_voice_state_update(member, before, after):
        if after.channel.id == 1260263569329492019:
            for guild in client.guilds:
                maincategory = discord.utils.get(guild.categories, id=1260888682504654859)

                if member.id == 259356565407137802:
                    channel_name = 'Dexter\'s Fun Club'
                elif member.id == 1139771223866355744:
                    channel_name = 'Young Tycoon'
                else:
                    channel_name = f'Public {member.display_name}'

                channel_p = await guild.create_voice_channel(name=channel_name, category=maincategory)

                await channel_p.set_permissions(member, connect=True, mute_members=True, move_members=True, manage_channels=True)
                await member.move_to(channel_p)

                def check(x, y, z):
                    return len(channel_p.members) == 0

                await client.wait_for('voice_state_update', check=check)
                await channel_p.delete()

        elif after.channel.id == 1260888339717034015:  # ID канала, где создаются приватные комнаты
            for guild in client.guilds:
                maincategory = discord.utils.get(guild.categories, id=1260888682504654859)  # ID категории для приватных комнат

                if member.id == 259356565407137802:
                    channel_name = 'Dexter\'s Fun Club'
                elif member.id == 1139771223866355744:
                    channel_name = 'Young Tycoon'
                else:
                    channel_name = f'Private {member.display_name}'

                channel_p = await guild.create_voice_channel(name=channel_name, category=maincategory)

                # Настройте права с помощью overwrites
                await channel_p.set_permissions(member, connect=True, mute_members=True, move_members=True, manage_channels=True)  # Установка прав для создателя
                await channel_p.set_permissions(guild.default_role, connect=False)  # Запретить доступ для всех остальных (кроме создателя)
                await channel_p.set_permissions(member, connect=True, speak=True)

                await member.move_to(channel_p)

                def check(x, y, z):
                    return len(channel_p.members) == 0

                await client.wait_for('voice_state_update', check=check)
                await channel_p.delete()


    token = t
    client.run(token)

