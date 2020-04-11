
import discord, asyncio
import os
import random
import time
from random import *


client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("코딩"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
  
    #made by LandmineSoldier (지뢰군인)
    
    if message.content.startswith("!도와줘"):
        embed=discord.Embed(title="지뢰봇", description="지뢰봇 명령어들", color=0xff6600)
        embed.set_author(name="made by 지뢰군인", url="https://steamcommunity.com/id/LandmineSoldier/", icon_url="https://cdn.discordapp.com/app-icons/681470208648544279/3194ed1f665a08c5431ff9f009b5dd61.png?size=64")
        embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/681470208648544279/3194ed1f665a08c5431ff9f009b5dd61.png?size=256")
        embed.add_field(name="너는 이미 죽어있다", value="단순반응", inline=True)
        embed.add_field(name="!지뢰봇", value="단순반응", inline=True)
        embed.add_field(name="!콜라", value="코카콜라vs펩시", inline=True)
        embed.add_field(name="!니 내 누군지 아니", value="단순반응", inline=True)
        embed.add_field(name="!앙 지뢰띠", value="단순반응", inline=True)
        embed.add_field(name="!탈모측정기 (이름)", value="0~100%확률", inline=True)
        embed.add_field(name="!누가 기침소리를 내었어", value="단순반응", inline=True)
        embed.add_field(name="!가위바위보", value="봇과 가위바위보", inline=True)
        embed.add_field(name="!슬롯머신", value="슬롯머신을 돌립니다", inline=True)
        embed.set_footer(text="추가 하고 싶은 명령어는 DM으로")
        await message.channel.send(embed=embed)

    if message.content.startswith("너는 이미 죽어있다"):
        await message.channel.send("뭣이이이이이")

    if message.content == "!지뢰봇":
        await message.channel.send("옛설!")

    if message.content == "!콜라":
        a = randint(0,1)
        if a == 0:
            embed=discord.Embed(title="코카콜라", description="", color=0xFF7F7F)
            embed.set_thumbnail(url="https://3z61v51uhgnmmsubi1n0uv6r-wpengine.netdna-ssl.com/wp-content/uploads/2020/02/what-you-can-see-from-coca-colas-digital-marketing-strategy-840x400.jpg")
            embed.add_field(name="나이스!", value="콜라는 역시", inline=True)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="펩시", description="", color=0x7F7FFF)
            embed.set_thumbnail(url="https://thehealthradar.com/wp-content/uploads/2020/01/pepsi-thats-what-i-like-videos.jpg")
            embed.add_field(name="하하!", value=" ( ͡° ͜ʖ ͡°)", inline=True)
            await message.channel.send(embed=embed)

    if message.content == "!니 내 누군지 아니":
        await message.channel.send("값 저장도 안하고 대답만 하는 봇인데 그거까지 알아야겠니")
        
    if message.content == "!앙 지뢰띠":
        await message.channel.send("앙 지뢰봇")

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
    
    if message.content == "!슬롯머신":
        message = message.channel

        r1 = randint(0,5)
        r2 = randint(0,5)
        r3 = randint(0,5)
        shape = ['[☆]','[♤]','[♡]','[♧]','[★]','[7]']

        await message.send(shape[r1])
        await message.send(shape[r2])
        await message.send(shape[r3])

        if (r1 == r2 and r2 == r3):
            await message.send("★ JACKPOT! ★")
        else:
            await message.send("FAILED")

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
