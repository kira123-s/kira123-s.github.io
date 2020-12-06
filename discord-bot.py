import discord
import requests, json
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged on as', bot.user)


@bot.event
async def on_message(message):
    # don't respond to ourselves

    if message.author == bot.user:
        return

    await bot.process_commands(message)
    if message.content.startswith('!Игорь'):
        await message.channel.send('<:Ntrcn1min:785204022168125510> <:Ntrcn1min:785204022168125510> <:Ntrcn1min:785204022168125510> <:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510><:Ntrcn1min:785204022168125510>')
    if message.content.startswith('!Настя'):
        await message.channel.send('<:Nastya:771823801050726460>  <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460> <:Nastya:771823801050726460>')
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Admin'):
        await message.channel.send('ВК создателя https://vk.com/igorexe')
    if message.content.startswith('Friend'):
        await message.channel.send('ВК Друзей  \n https://vk.com/id594291267 \n https://vk.com/id385908240')
    if message.content.startswith('!команды'):
        await message.channel.send('Команды бота \n  Friend \n  Admin \n  hello \n  !weather ')

    # if message.content.startswith("!Настя"):

    #     await message.channel.send(':Nastya:')
    # if message.content.find('выгу'):
    #     await message.channel.send( '<:Nastya:771823801050726460>')
    # if message.content.startswith('!Настя'):
    #     for x in discord.client.get_all_emojis():
    #         if x.id == '<:Nastya:771823801050726460>':
    #             return await discord.client.add_reaction(message, x, x, x, x, x, x,x)

@bot.command()
async def weather(ctx, *, city: str):
    api_key = "7f1e23163b47cbf21184f339f5c8eaf9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"# if message.content.startswith('Настя'):


    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        async with ctx.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                                  color=ctx.guild.me.top_role.color,
                                  timestamp=ctx.message.created_at, )
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    else:
        print('error')


bot.run('Nzc3MjU5OTYxNzA0MzgyNDY0.X7A1vw.ykTPEIFvgaKt3PiMtqssL3pQtys')










