import telebot
import pyscp
import time
from random import randint
from urllib.request import urlopen
from lxml.html import parse
from googlesearch import search
image='<a href="https://telegra.ph/Pravila-dlya-SCP-Russia-20-06-28">правилами</a>'
def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
def delit(userid):
	with open('b.txt', 'r') as searchfile:
	           for line in searchfile:
	           	if (str(userid) in line):
	           		list=line.split(';')
	           		with open("b.txt", "r") as f:
	           			lines = f.readlines()
	           		with open("b.txt", "w") as f:
	           			for line in lines:
	           				if line.strip("\n") != line:
	           					f.write(line)
def add(userid, numb):
	with open('b.txt', 'a') as the_file:
		the_file.write(f'\n{userid};{numb}')
def randit():
	try:
		nk=str(randint(2, 5999))
		urler ="http://scp-ru.wikidot.com/"
		global scpurl
		scpurl=urler+scp+nk
		page=urlopen(scpurl)
		p=parse(page)
		title=((p.find(".//title").text))
		global kj
		kj = (title.replace('- The SCP Foundation', ""))
	except Exception as e:
		nk=str(randint(2, 5999))
		urler ="http://scp-ru.wikidot.com/"
		scpurl=urler+scp+nk
		page=urlopen(scpurl)
		p=parse(page)
		title=((p.find(".//title").text))
		kj = (title.replace('- The SCP Foundation', ""))
		pass
scp = "scp-"
bot = telebot.TeleBot("1")
ru_wiki = pyscp.wikidot.Wiki('scp-ru.wikidot.com')
def extract_arg(arg):
    return arg.split()[1:]
@bot.message_handler(content_types=['new_chat_members'])
def greeting(massager):
    bot.reply_to(massager, text=f'''Добро пожаловать в чат, читатель, поздравляем с присоединением к нашей уютной группе. Рекомендуем ознакомиться с {image}, а также рассказать о себе и о своем любимом объекте! Для вас также действует Товарищ Роботный, умеющий искать объекты!''', parse_mode='HTML')
    whatweneed=massager.from_user.id
    delit(whatweneed)
    what2='0'
    add(whatweneed, what2)
@bot.message_handler(commands=['o'])
def o(message):
   global status
   status = extract_arg(message.text)
   try:
    object = status[0]
   except Exception as e:
    object ="7777"
   l = scp + object
   url = "http://scp-ru.wikidot.com/" + l
   try:
            page = urlopen(url)
            p = parse(page)
            title=((p.find(".//title").text))
            result = " ".join ([url])
            k = (title.replace('- The SCP Foundation', ""))
            text = (f'<a href="{url}">{k}</a>')
   except Exception as e:
    text="Ничего не найдено."
    pass
   bot.send_message(message.chat.id, text,parse_mode='HTML')
@bot.message_handler(commands=['s'])
def s(m):
    msg=bot.send_message(m.chat.id, 'Обработка...',parse_mode='HTML')
    status1 = m.text
    if('@questionisbot' in status1):
    	status2=status1.replace('/s@questionisbot', "")
    else:
    	status2=status1.replace('/s', "")
    f = open("base.txt", "r", encoding='utf-8')
    searchlines = [line.strip() for line in f.readlines() if line.strip()]
    g, nm, count, count1, gey =[], int("0"), int("0"), int("0"), []
    out, out1 = [], []
    url = 'http://scp-ru.wikidot.com/'
    f.close()
    try:
        for i, line in enumerate(searchlines):
                if status2.lower() in line.lower():
                            for l in searchlines[i : i + 1]:
                                    out.append(l.split(maxsplit=1)[0])
                                    out1.append(l.split(maxsplit=1)[1])
    except Exception as e:
        bot.send_message(m.chat.id, text="Раз вам нечего искать, то почитайте мои любимые статьи. Если вы пытайтесь вставить команду из меню, то вместо нажатия на команду зажмите ее.", parse_mode='HTML')
        pass
    finalout = list(set(out))
    number = len(finalout)
    url = 'http://scp-ru.wikidot.com/'
    while (nm<number):
        try:
            page = urlopen(url+finalout[count])
            p = parse(page)
            title=((p.find(".//title").text))
            result = " ".join ([url+finalout[count]])
            k = (title.replace('- The SCP Foundation', ""))
            gey.append(k)
            if(k!="The SCP Foundation"):
            	g.append(f'<a href="{result}">{k}</a>')
        except Exception as e:
            pass
        count+=1
        count1+=1
        nm+=1
    numbeer=int('0')
    counter=int('0')
    ka = search(f'{status2} site:scp-ru.wikidot.com', num_results=6)
    while (numbeer<7):
        try:
            page = urlopen(ka[counter])
            p = parse(page)
            title=((p.find(".//title").text))
            kj = (title.replace('- The SCP Foundation', ""))
            if(kj not in gey and "forum" not in ka[counter] and "draft" not in ka[counter]and "scp-series" not in ka[counter] and 'The SCP Foundation' not in kj and 'List All Pages' not in kj and 'Свежие правки' not in kj and '2011' not in kj and '2012' not in kj and '2013' not in kj and '2014' not in kj and '2015' not in kj and '2016' not in kj and '2017' not in kj and '2018' not in kj and '2019' not in kj and '2020'not in kj and '2021' not in kj):
            	result = ka[counter]
            	g.append(f'<a href="{result}">{kj}</a>')
        except Exception as e:
            pass
        numbeer+=1
        counter+=1
    story = '\n'.join(g)
    try:
        bot.edit_message_text(chat_id=m.chat.id, text=story, message_id=msg.message_id, parse_mode='HTML')
    except Exception as e:
        bot.edit_message_text(chat_id=m.chat.id, text="Ничего не найдено.", message_id=msg.message_id, parse_mode='HTML')
@bot.message_handler(commands=['help'])
def help(t):
    bot.send_message(t.chat.id, "/o — поиск по номеру; /s — поиск по названию; /help — это сообщение; /join — присоеденится к сообществу; /faq — ответы на частые вопросы; /r — рандомная статья.",parse_mode='HTML')
@bot.message_handler(commands=['join'])
def join(j):
    joiner=(f'<a href="http://scp-ru.wikidot.com/system:join">Подай простую заявку!</a>')
    bot.send_message(j.chat.id, joiner,parse_mode='HTML')
@bot.message_handler(commands=['faq'])
def faq(f):
    faqer=(f'<a href="http://scp-ru.wikidot.com/faq">Читать тут.</a>')
    bot.send_message(f.chat.id, faqer,parse_mode='HTML')
@bot.message_handler(commands=['r'])
def r(ran):
	try:
		randit()
	except Exception as e:
		randit()
		pass
	bot.send_message(ran.chat.id, f'<a href="{scpurl}">{kj}</a>', parse_mode='HTML')
@bot.message_handler(commands=['mute'])
def mute(muter):
    lines=[]
    id=muter.reply_to_message.from_user.id
    ch=muter.chat.id
    with open('b.txt', 'r') as searchfile:
        for line in searchfile:
            lines.append(line)
        if (str(id) in line) and muter.from_user.id in get_admin_ids(bot, ch):
            list=line.split(';')
            if (list[1]=='0'):
                try:
                    bot.restrict_chat_member(muter.chat.id,  muter.reply_to_message.from_user.id, until_date=int(time.time())+86400)
                    bot.send_message(muter.chat.id, "Участник лишен возможности писать на сутки.")
                except Exception as e:
                    bot.send_message(muter.chat.id, "Неудача.")
            if (list[1]=='1'):
                try:
                    bot.restrict_chat_member(muter.chat.id,  muter.reply_to_message.from_user.id, until_date=int(time.time())+604800)
                    bot.send_message(muter.chat.id, "Участник лишен возможности писать на неделю.")
                except Exception as e:
                    bot.send_message(muter.chat.id, "Неудача.")
            if (list[1]=='2'):
                try:
                    bot.restrict_chat_member(muter.chat.id,  muter.reply_to_message.from_user.id, until_date=int(time.time())+2592000)
                    bot.send_message(muter.chat.id, "Участник лишен возможности писать на месяц.")
                except Exception as e:
                    bot.send_message(muter.chat.id, "Неудача.")
            if (int(list[1])>2):
                bot.send_message(muter.chat.id, f'Данный участник был лишен возможности писать 3 раза, последний раз на месяц, пришло время бана!', parse_mode='HTML')
            num=list[1]
            delit(id)
            numb=int(num)
            numb+=1
            numb=str(numb)
            add(id, numb)
        elif (str(id) not in lines):
            usid=muter.reply_to_message.from_user.id
            delit(usid)
            numka='1'
            add(usid, numka)
            with open('b.txt', 'r') as searchfile:
                for line in searchfile:
                    if(str(usid) in line and muter.from_user.id in get_admin_ids(bot, ch)):
                        list=line.split(';')
                        lines.append(str(list[1]))
                        try:
                            bot.restrict_chat_member(muter.chat.id,  muter.reply_to_message.from_user.id, until_date=int(time.time())+86400)
                            bot.send_message(muter.chat.id, "Участник лишен возможности писать на сутки.")
                        except Exception as e:
                            bot.send_message(muter.chat.id, "Неудача")
        with open('b.txt', 'r') as searchfile:
            for line in searchfile:
                if(str(id) in line and muter.from_user.id not in get_admin_ids(bot, ch)):
                    delit(usid)
                    bot.send_message(muter.chat.id, "Вы не администратор.")
bot.polling()