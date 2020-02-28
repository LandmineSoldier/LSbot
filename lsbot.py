
import discord, asyncio
import random
from random import *


token = "NjgxNDcwMjA4NjQ4NTQ0Mjc5.XlO_vg.4kexYlLMkqn1chxSWiMQHnyOMWc"
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("에헥따"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "!콜라":
        a = randint(0,1)
        if a == 0:
            await message.channel.send("https://3z61v51uhgnmmsubi1n0uv6r-wpengine.netdna-ssl.com/wp-content/uploads/2020/02/what-you-can-see-from-coca-colas-digital-marketing-strategy-840x400.jpg")
        else:
            await message.channel.send("https://thehealthradar.com/wp-content/uploads/2020/01/pepsi-thats-what-i-like-videos.jpg")
            await message.channel.send("( ͡° ͜ʖ ͡°)")

    if message.content == "!니 내 누군지 아니":
        await message.channel.send("값 저장도 안하고 대답만 하는 봇인데 그거까지 알아야겠니")

    if message.content == "!탈모측정기":
        b = randint(0,10)
        await message.channel.send("너님은..")
        await message.channel.send(b*10)
        await message.channel.send("%확률로 탈모입니다!")

    if message.content == "!누가 기침소리를 내었어":
        await message.channel.send("너님이옵니다 전하 어훏")

    if message.content == "!가위바위보":
        await message.channel.send("승부를 받아들이지!")
        await message.channel.send("(예:!가위)")
    if message.content == "!가위":
            a = randint(0,2)
            if a == 0:
                await message.channel.send("가위!")
                await message.channel.send("쳇.. 비겼군 다음에 보도록하지..")
            if a == 1:
                await message.channel.send("바위!")
                await message.channel.send("핳 나의 승리다ㅏㅇ!")
            if a == 2:
                await message.channel.send("보!")
                await message.channel.send("흐아아ㅏ 앙대ㅐ애ㅐㅐ 나으ㅣ 패배라늬")
            
    if message.content == "!바위":
            a = randint(0,2)
            if a == 0:
                await message.channel.send("가위!")
                await message.channel.send("Aㅏ")
            if a == 1:
                await message.channel.send("바위!")
                await message.channel.send("아 ㄲㅂ")
            if a == 2:
                await message.channel.send("보!")
                await message.channel.send("푸하핳")
    if message.content == "!보":
            a = randint(0,2)
            if a == 0:
                await message.channel.send("가위!")
                await message.channel.send("훗.. 강해져서 돌아와라 애송이")
            if a == 1:
                await message.channel.send("바위!")
                await message.channel.send("어째서 늦게 냈는데도 진단 말이냐아앍!")
            if a == 2:
                await message.channel.send("보!")
                await message.channel.send("훗.. 강하군..")

    

client.run(token)