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
        if message.author.id == '315237238940106754' : #관리자아이디
            embed = discord.Embed(    
                title = "📌 공지사항",
                description= '```' + message.content[4:] + '```',
                color=0xFF0000	
                )
            await client.send_message(client.get_channel("679379752318009352"), embed=embed)
            await client.send_message(client.get_channel("679402498607546398"), embed=embed)
            await client.send_message(client.get_channel("680081617083170818"), embed=embed)
            await client.send_message(client.get_channel("680081729452507193"), embed=embed)
            await client.send_message(client.get_channel("680081795349217303"), embed=embed)
            await client.send_message(client.get_channel("680081829029609521"), embed=embed)
            await client.send_message(client.get_channel("680081863255130121"), embed=embed)
            await client.send_message(client.get_channel("680081902295580728"), embed=embed)
            await client.send_message(client.get_channel("680081929671933972"), embed=embed)
            await client.send_message(client.get_channel("680081956171808788"), embed=embed)
            await client.send_message(client.get_channel("680081978116014110"), embed=embed)
            await client.send_message(client.get_channel("680082009976209444"), embed=embed)
            await client.send_message(client.get_channel("680082046282104863"), embed=embed)
            await client.send_message(client.get_channel("680082075352825992"), embed=embed)
            await client.send_message(client.get_channel("680082122270179361"), embed=embed)
            await client.send_message(client.get_channel("680082158261633025"), embed=embed)
            await client.send_message(client.get_channel("680082168483020800"), embed=embed)
            await client.send_message(client.get_channel("680082314901979226"), embed=embed)
            await client.send_message(client.get_channel("680082355666681889"), embed=embed)
            await client.send_message(client.get_channel("680082398498783249"), embed=embed)
            await client.send_message(client.get_channel("680082433307050009"), embed=embed)
            await client.send_message(client.get_channel("680082468761632774"), embed=embed)
            await client.send_message(client.get_channel("680082525028089879"), embed=embed)
            await client.send_message(client.get_channel("680082555080540231"), embed=embed)
            await client.send_message(client.get_channel("680082578228772864"), embed=embed)
            await client.send_message(client.get_channel("680082598206505015"), embed=embed)
            await client.send_message(client.get_channel("680082619484209409"), embed=embed)
            await client.send_message(client.get_channel("680082641269424128"), embed=embed)
            await client.send_message(client.get_channel("680082664069660821"), embed=embed)
            await client.send_message(client.get_channel("680082711733338120"), embed=embed)
            await client.send_message(client.get_channel("680082735603384366"), embed=embed)
            await client.send_message(client.get_channel("680082759892729856"), embed=embed)
            await client.send_message(client.get_channel("680082802875695151"), embed=embed)
            await client.send_message(client.get_channel("680082833464623106"), embed=embed)
            await client.send_message(client.get_channel("680082853941608530"), embed=embed)
            await client.send_message(client.get_channel("680082876246786130"), embed=embed)
            await client.send_message(client.get_channel("680082896434102300"), embed=embed)
            await client.send_message(client.get_channel("680082919007584261"), embed=embed)
            await client.send_message(client.get_channel("680082938762756096"), embed=embed)
            await client.send_message(client.get_channel("680082967284285537"), embed=embed)
            await client.send_message(client.get_channel("680082990973583364"), embed=embed)
            await client.send_message(client.get_channel("680083018932813825"), embed=embed)
            await client.send_message(client.get_channel("680083045398741038"), embed=embed)
            await client.send_message(client.get_channel("680083066353352748"), embed=embed)
            await client.send_message(client.get_channel("680083086872281276"), embed=embed)
            await client.send_message(client.get_channel("680083109181652998"), embed=embed)
            await client.send_message(client.get_channel("680083128831836210"), embed=embed)
            await client.send_message(client.get_channel("680083167457443897"), embed=embed)
            await client.send_message(client.get_channel("680083575793778828"), embed=embed)
            await client.send_message(client.get_channel("680083622300352588"), embed=embed)
            await client.send_message(client.get_channel("680083653245534324"), embed=embed)
            await client.send_message(client.get_channel("680083686460620871"), embed=embed)
            await client.send_message(client.get_channel("680083730349555789"), embed=embed)
            await client.send_message(client.get_channel("680083754768662594"), embed=embed)
            await client.send_message(client.get_channel("680083782870761513"), embed=embed)
            await client.send_message(client.get_channel("680083809928216682"), embed=embed)
            await client.send_message(client.get_channel("680083836465446939"), embed=embed)
            await client.send_message(client.get_channel("680083862365274160"), embed=embed)
            await client.send_message(client.get_channel("680083887720103976"), embed=embed)
            await client.send_message(client.get_channel("680083926382936073"), embed=embed)
            await client.send_message(client.get_channel("680083970624323618"), embed=embed)
            await client.send_message(client.get_channel("680084002148843520"), embed=embed)
            await client.send_message(client.get_channel("680084027872510002"), embed=embed)
            await client.send_message(client.get_channel("680084054644883476"), embed=embed)
            await client.send_message(client.get_channel("680084082830737459"), embed=embed)
            await client.send_message(client.get_channel("680084108050956289"), embed=embed)
            await client.send_message(client.get_channel("680084134223413273"), embed=embed)
            await client.send_message(client.get_channel("680084156398829574"), embed=embed)
            await client.send_message(client.get_channel("680084191450365961"), embed=embed)
            await client.send_message(client.get_channel("680084278604070949"), embed=embed)
            await client.send_message(client.get_channel("680084325475024932"), embed=embed)
            await client.send_message(client.get_channel("680084419901522029"), embed=embed)
            await client.send_message(client.get_channel("680084446241882119"), embed=embed)
            await client.send_message(client.get_channel("680084470958784556"), embed=embed)
            await client.send_message(client.get_channel("680084501501968386"), embed=embed)
            await client.send_message(client.get_channel("680084528957620396"), embed=embed)
            await client.send_message(client.get_channel("680084563438993439"), embed=embed)
            await client.send_message(client.get_channel("680084633458835554"), embed=embed)
            await client.send_message(client.get_channel("680084662210920478"), embed=embed)
            await client.send_message(client.get_channel("680084689234821198"), embed=embed)
            await client.send_message(client.get_channel("680084713347743792"), embed=embed)
            await client.send_message(client.get_channel("680084738702311545"), embed=embed)
            await client.send_message(client.get_channel("680084763712946256"), embed=embed)
            await client.send_message(client.get_channel("680084786815303913"), embed=embed)
            await client.send_message(client.get_channel("680084809166749706"), embed=embed)
            await client.send_message(client.get_channel("680084834798010417"), embed=embed)
            await client.send_message(client.get_channel("680084861054222348"), embed=embed)
            await client.send_message(client.get_channel("680084887771938817"), embed=embed)
            await client.send_message(client.get_channel("680084913730748423"), embed=embed)
            await client.send_message(client.get_channel("680084946408439827"), embed=embed)
            await client.send_message(client.get_channel("680085001706274881"), embed=embed)
            await client.send_message(client.get_channel("680085026288828426"), embed=embed)
            await client.send_message(client.get_channel("680085050255081475"), embed=embed)
            await client.send_message(client.get_channel("680085077417525302"), embed=embed)
            await client.send_message(client.get_channel("680085105976672311"), embed=embed)
            await client.send_message(client.get_channel("680085132228558964"), embed=embed)
            await client.send_message(client.get_channel("680085156358258708"), embed=embed)
            await client.send_message(client.get_channel("680085181922803737"), embed=embed)
            await client.send_message(client.get_channel("680085206358818853"), embed=embed)
            await client.send_message(client.get_channel("680085231419785216"), embed=embed)
            await client.send_message(client.get_channel("680475870938529834"), embed=embed)
            await client.send_message(client.get_channel("680476192281067520"), embed=embed)
            await client.send_message(client.get_channel("680476223066996945"), embed=embed)
            await client.send_message(client.get_channel("680476264242348050"), embed=embed)
            await client.send_message(client.get_channel("680476288603127831"), embed=embed)
            await client.send_message(client.get_channel("680476310853910529"), embed=embed)
            await client.send_message(client.get_channel("680476332089671689"), embed=embed)
            await client.send_message(client.get_channel("680476363030921320"), embed=embed)
            await client.send_message(client.get_channel("680476384283590659"), embed=embed)
            await client.send_message(client.get_channel("680476421201985585"), embed=embed)
            await client.send_message(client.get_channel("680476494199259172"), embed=embed)
            await client.send_message(client.get_channel("680476524427870218"), embed=embed)
            await client.send_message(client.get_channel("680476545382481940"), embed=embed)
            await client.send_message(client.get_channel("680476566689808582"), embed=embed)
            await client.send_message(client.get_channel("680476586591780961"), embed=embed)
            await client.send_message(client.get_channel("680476609190690888"), embed=embed)
            await client.send_message(client.get_channel("680476629318762566"), embed=embed)
            await client.send_message(client.get_channel("680476653536673910"), embed=embed)
            await client.send_message(client.get_channel("680476683618353193"), embed=embed)
            await client.send_message(client.get_channel("680476708864131150"), embed=embed)
            await client.send_message(client.get_channel("680476762463141918"), embed=embed)
            await client.send_message(client.get_channel("680476786974261258"), embed=embed)
            await client.send_message(client.get_channel("680476806934953999"), embed=embed)
            await client.send_message(client.get_channel("680476825180438623"), embed=embed)
            await client.send_message(client.get_channel("680476846336507911"), embed=embed)
            await client.send_message(client.get_channel("680476874706649097"), embed=embed)
            await client.send_message(client.get_channel("680476529998037180"), embed=embed)
            await client.send_message(client.get_channel("680478520568578091"), embed=embed)
            await client.send_message(client.get_channel("680478561504722944"), embed=embed)
            await client.send_message(client.get_channel("680478588981870592"), embed=embed)
            await client.send_message(client.get_channel("680478614290038926"), embed=embed)
            await client.send_message(client.get_channel("680478645995044909"), embed=embed)
            await client.send_message(client.get_channel("680478666643341352"), embed=embed)
            await client.send_message(client.get_channel("680478688617300018"), embed=embed)
            await client.send_message(client.get_channel("680478765402685446"), embed=embed)
            await client.send_message(client.get_channel("680478787108208661"), embed=embed)
            await client.send_message(client.get_channel("680478819945152586"), embed=embed)
            await client.send_message(client.get_channel("680478855437484161"), embed=embed)
            await client.send_message(client.get_channel("680478881488437254"), embed=embed)
            await client.send_message(client.get_channel("680478909611245627"), embed=embed)
            await client.send_message(client.get_channel("680478934047260724"), embed=embed)
            await client.send_message(client.get_channel("680478953751969829"), embed=embed)
            await client.send_message(client.get_channel("680478974392270884"), embed=embed)
            await client.send_message(client.get_channel("680478992968581201"), embed=embed)
            await client.send_message(client.get_channel("680479013600362513"), embed=embed)
            await client.send_message(client.get_channel("680479033707986997"), embed=embed)
            await client.send_message(client.get_channel("680479063504322561"), embed=embed)
            await client.send_message(client.get_channel("680479082768760870"), embed=embed)
            await client.send_message(client.get_channel("680479103778029592"), embed=embed)
            await client.send_message(client.get_channel("680479149944602732"), embed=embed)
                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
