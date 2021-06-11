import telebot
import pyscp
from random import randint
from googlesearch import search
scp = "scp-"
bot = telebot.TeleBot("1822055365:AAGuy2zwaxZkZIHad_HGRyEUUXmt0LVzOXE")
ru_wiki = pyscp.wikidot.Wiki('scpfoundation.net')
def extract_arg(arg):
    return arg.split()[1:]
@bot.message_handler(commands=['o'])
def o(message):
   global status
   status = extract_arg(message.text)
   try:
    object = status[0]
   except Exception as e:
    object ="7777"
   l = scp + object
   url = "scpfoundation.net/" + l
   p = ru_wiki(l)
   try:
    k = ('{}'.format(p.title))
    text = (f'<a href="{url}">{k}</a>')
   except Exception as e:
    text="Простите, этот номер не присвоен не одному из объектов"
    if (status =="/o 2998"):
    	text = (f'<a href="http://scpfoundation.net/scp-2998">"Аномальная трансляция, 2485 МГц"</a>')
    else:
    	pass
   bot.send_message(message.chat.id, text,parse_mode='HTML')
def extract_argument(argument):
    return argument.split()[3:]
@bot.message_handler(commands=['s'])
def s(m):
    status1 = m.text
    status2 = status1.replace('/s', "")
    f = open("base.txt", "r")
    searchlines = [line.strip() for line in f.readlines() if line.strip()]
    g, nm, count, count1, gey =[], int("0"), int("0"), int("0"), []
    out, out1 = [], []
    url = 'http://scpfoundation.net/'
    f.close()
    try:
        for i, line in enumerate(searchlines):
                if status2.lower() in line.lower():
                            for l in searchlines[i : i + 1]:
                                    out.append(l.split(maxsplit=1)[0])
                                    out1.append(l.split(maxsplit=1)[1])
    except Exception as e:
        bot.send_message(m.chat.id, "Раз вам нечего искать, то почитайте мои любимые статьи.",parse_mode='HTML')
        pass
    finalout = list(set(out))
    number = len(finalout)
    g, nm, count, count1, gey =[], int("0"), int("0"), int("0"), []
    url = 'http://scpfoundation.net/'
    while (nm<number):
        try:
            p = ru_wiki(finalout[count])
            k = ('{}'.format(p.title))
            result = " ".join ([url, finalout[count]])
            gey.append(k)
            g.append(f'<a href="{result}">{k}</a>')
        except Exception as e:
            pass
        count+=1
        count1+=1
        nm+=1
    numbeer=int('0')
    counter=int('0')
    ka = search(f'{status2} site:scpfoundation.net', num_results=6)
    while (numbeer<7):
        try:
            p = ru_wiki(ka[counter])
            kj = ('{}'.format(p.title))
            if(kj not in gey and "forum" not in ka[counter] and "draft" not in ka[counter]):
            	result = ka[counter]
            	g.append(f'<a href="{result}">{kj}</a>')
        except Exception as e:
            pass
        numbeer+=1
        counter+=1
     
    story = '\n'.join(g)
    try:
        bot.send_message(m.chat.id, story,parse_mode='HTML')
    except Exception as e:
        bot.send_message(m.chat.id, "Ничего не найдено.", parse_mode='HTML')
@bot.message_handler(commands=['help'])
def help(t):
    bot.send_message(t.chat.id, "/o — поиск по номеру; /s — поиск по названию; /help — это сообщение; /join — присоеденится к сообществу; /faq — ответы на частые вопросы; /r — рандомная статья.",parse_mode='HTML')
@bot.message_handler(commands=['join'])
def join(j):
    joiner=(f'<a href="http://scpfoundation.net/system:join">Подай простую заявку!</a>')
    bot.send_message(j.chat.id, joiner,parse_mode='HTML')
@bot.message_handler(commands=['faq'])
def faq(f):
    faqer=(f'<a href="http://scpfoundation.net/faq">Читать тут.</a>')
    bot.send_message(f.chat.id, faqer,parse_mode='HTML')
@bot.message_handler(commands=['r'])
def r(ran):
	nk=str(randint(2, 5999))
	urler ="http://scpfoundation.net/"
	scpurl=urler+scp+nk
	bot.send_message(ran.chat.id, scpurl,parse_mode='HTML')
bot.polling()