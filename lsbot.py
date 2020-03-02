
import discord, asyncio
import os
import random
import time
from random import *


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
    
    if message.content == "!지뢰봇":
        await message.channel.send("옛설!")
        
    if message.content == "!넘패드카타나":
        await message.channel.send("자네.. 진심인가..! (3초 내에 '그렇다'라고 치세요)")
        time.sleep(3)
        if message.content == "그렇다":
            await message.channel.send("좋다!")
            await message.channel.send("(지뢰봇이 공격하면 1초 내에 맞받아 치면 됩니다.)")
            await message.channel.send("가로 공격은 좌우 반전")
            await message.channel.send("세로 공격은 상하 반전")
            await message.channel.send("대각선은 상하좌우반전")
            await message.channel.send("예시:0 123 0 -> 0 321 0")
            await message.channel.send("예시:0 741 0 -> 0 147 0")
            await message.channel.send("예시:0 159 0 -> 0 753 0")
            await message.channel.send("띄어쓰기는 하지마십시오")
            await message.channel.send("준비되었다면 3초 내에 'ready' 라고 하세요")
            time.sleep(3)
            if message.content == "ready":
                await message.channel.send("3초뒤 봇의 공격이 시작됩니다!")
                time.sleep(3)
                s = 0
                while True:
                    r = randint(1,16)
                    if r == 1:
                        await message.channel.send("0 123 0")
                        time.sleep(1)
                        if message.content == "03210":
                            s += 1
                        else:
                            break
                    if r == 2:
                        await message.channel.send("0 456 0")
                        time.sleep(1)
                        if message.content == "06540":
                            s += 1
                        else:
                            break
                    if r == 3:
                        await message.channel.send("0 789 0")
                        time.sleep(1)
                        if message.content == "09870":
                            s += 1
                        else:
                            break
                    if r == 4:
                        await message.channel.send("0 321 0")
                        time.sleep(1)
                        if message.content == "01230":
                            s += 1
                        else:
                            break
                    if r == 5:
                        await message.channel.send("0 654 0")
                        time.sleep(1)
                        if message.content == "04560":
                            s += 1
                        else:
                            break
                    if r == 6:
                        await message.channel.send("0 987 0")
                        time.sleep(1)
                        if message.content == "07890":
                            s += 1
                        else:
                            break


                    if r == 7:
                        await message.channel.send("0 147 0")
                        time.sleep(1)
                        if message.content == "07410":
                            s += 1
                        else:
                            break
                    if r == 8:
                        await message.channel.send("0 258 0")
                        time.sleep(1)
                        if message.content == "08520":
                            s += 1
                        else:
                            break
                    if r == 9:
                        await message.channel.send("0 369 0")
                        time.sleep(1)
                        if message.content == "09630":
                            s += 1
                        else:
                            break
                    if r == 10:
                        await message.channel.send("0 741 0")
                        time.sleep(1)
                        if message.content == "01470":
                            s += 1
                        else:
                            break
                    if r == 11:
                        await message.channel.send("0 852 0")
                        time.sleep(1)
                        if message.content == "02580":
                            s += 1
                        else:
                            break
                    if r == 12:
                        await message.channel.send("0 963 0")
                        time.sleep(1)
                        if message.content == "03690":
                            s += 1
                        else:
                            break


                    if r == 13:
                        await message.channel.send("0 159 0")
                        time.sleep(1)
                        if message.content == "07530":
                            s += 1
                        else:
                            break
                    if r == 14:
                        await message.channel.send("0 951 0")
                        time.sleep(1)
                        if message.content == "03570":
                            s += 1
                        else:
                            break
                    if r == 15:
                        await message.channel.send("0 357 0")
                        time.sleep(1)
                        if message.content == "09510":
                            s += 1
                        else:
                            break
                    if r == 16:
                        await message.channel.send("0 753 0")
                        time.sleep(1)
                        if message.content == "01590":
                            s += 1
                        else:
                            break
            await message.channel.send("좋은싸움이었다..")
            await message.channel.send("당신은 봇의 공격을 총")
            await message.channel.send(s)
            await message.channel.send("번 튕겨냈습니다!")
        

    if message.content == "!콜라":
        a = randint(0,1)
        if a == 0:
            await message.channel.send("https://3z61v51uhgnmmsubi1n0uv6r-wpengine.netdna-ssl.com/wp-content/uploads/2020/02/what-you-can-see-from-coca-colas-digital-marketing-strategy-840x400.jpg")
        else:
            await message.channel.send("https://thehealthradar.com/wp-content/uploads/2020/01/pepsi-thats-what-i-like-videos.jpg")
            await message.channel.send("( ͡° ͜ʖ ͡°)")

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

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
