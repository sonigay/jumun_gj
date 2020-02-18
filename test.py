import discord
import asyncio
import random
import os
import datetime
from time import sleep
import arrow
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gjhelper-cc7069273059.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1PA2WP-aQ-d8TlGubOSpUJwHoH8VZfiTwIFPO3eYGnIs')

client = discord.Client()
@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("----------------")
    await client.change_presence(game=discord.Game(name='메세지 전달', type=1))


@client.event
async def on_member_join(member):
    sleep(1)	
    fmt = '{1.name} 에 오신것을 환영합니다.\n{0.mention} 님!! \n매장이름/직급/성함/연락처 이렇게 남겨주시면 \n확인후 권한을 승인해드리겠습니다. '
    channel = member.server.get_channel("679365866000875602")
    return await client.send_message(channel, fmt.format(member, member.server))




@client.event
async def on_message(message):
    global gc #정산
    global creds #정산
    

    if message.content.startswith('!그레이드'):
        gc = gspread.authorize(creds)
        wks = gc.open('GJ재고관리').worksheet('그레이드')
        result = wks.acell('B1').value
        embed1 = discord.Embed(
            title = ' 파트너 그레이드 안내!! ',
            description= '**```css\n' + result + ' ```**',
            color=0x7fffd4
            )
        embed2 = discord.Embed(
            title = ' 파트너 그레이드 조회!! ',
            description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
            color=0x00ffff
            )
        await client.send_message(message.channel, embed=embed1)
        await client.send_message(client.get_channel("679369629172498474"), embed=embed2)


    if message.content.startswith('!주문'):
        
        curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
        krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
        gc = gspread.authorize(creds)
        wks = gc.open('GJ재고관리').worksheet('디스코드주문내역')
        wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
        embed1 = discord.Embed(
            title = message.author.display_name + "님 의 주문 ",
            description= '```fix\n' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed1.add_field(
            name=" 주문접수 확인... ",
            value= '```diff\n!주문내용이 전달되어 정상적으로\n!접수되었습니다. 부득이한경우\n!개인답변 드리겠습니다.```'
            )
        embed2 = discord.Embed(
            title = message.author.display_name + "님 의 주문내용 ",
            description= '```' + message.content[4:] + '```',
            color=0xCBFF75
            )
        embed2.add_field(
            name=" 주문 접수처... ",
            value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
            )
        await client.send_message(message.channel, embed=embed1)
        await client.send_message(client.get_channel("679376089885310997"), embed=embed2)
            
	
    if message.content.startswith('!답변'):
        member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
        neyongdabtotal = message.content[23:]
        neyongdab = neyongdabtotal.split("/")
        neyong = neyongdab[0]
        dab = neyongdab[1]
	
        embed = discord.Embed(
            title = "주문내용",
            description= '```fix\n' + neyong + '```',
            color=0xFF0000
            )
        embed.add_field(
            name = message.author.display_name + "님 답변",
            value= '```Tex\n' + '$' + dab + '```'
	        )
        await client.send_message(member, embed=embed)
	
	
	
    if message.content.startswith('!공지'):
       # message.author = member
        if member.roles.name == "관리자" :  # 관리자역할
            embed = discord.Embed(    
                title = "📌 공지사항",
                description= '```' + message.content[4:] + '```',
                color=0xFF0000	
                )
            await client.send_message(client.get_channel("679379752318009352"), embed=embed)
            await client.send_message(client.get_channel("679402498607546398"), embed=embed)

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
