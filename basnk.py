from utlis.rank import setrank,isrank,remrank,remsudos,setsudo, GPranks,IDrank
from utlis.send import send_msg, BYusers, GetLink,Name,Glang
from utlis.locks import st,getOR
from utlis.tg import Bot
from config import *


import telebot,random,time, json,random
from datetime import datetime,timedelta
with open("data.json","w") as f :
	f.write("{}")
with open("timer.json","w") as f :
	f.write("{}") 
aksht = {"":""}
akshtt = [""]
rateb_list = ["الوظيفة : رائد فضاء 👨‍🚀  \n الراتب : 20000 ريال","الوظيفة : مبرمج 👨‍💻  \n الراتب : 13000 ريال(","الوظيفة : مصاص دماء 🧛‍♂️  \n الراتب : 7500 ريال","الوظيفة : قاضي 👨‍⚖️  \n الراتب : 8600 ريال","الوظيفة : ملازم 👮‍♂️  \n الراتب : 9000 ريال","الوظيفة : طيار 👨‍✈️  \n الراتب : 12000 ريال"]

def timer_set(item,user_id,data,timer,time_type,time):
	now = datetime.now()
	if time_type == "min" :
		delta =now + timedelta(minutes=time)
	elif time_type == "sec" :
		delta =now + timedelta(seconds=time)
	else :
		delta =now + timedelta(minutes=time)
	y = int(delta.year)
	m = int(delta.month)
	d = int(delta.day)
	h = int(delta.hour)
	min = int(delta.minute)
	s = int(delta.second)
	timer[user_id][item] = {
	"y":y,
	"m":m,
	"d":d,
	"h":h,
	"min":min,
	"s":s
	}

def items(item,user_id,data,timer):
	cash = data[user_id]["cash"]
	cash += 50
	data[user_id]["cash"] = cash
	timer_set(item,user_id,data,timer,"minutes",10)
	return data[user_id]["cash"]
def item_timer(item,user_id,data,timer):
	if user_id in timer :
		if "y" in timer[user_id][item]:
			now = datetime.now()
			y = timer[user_id][item]["y"]
			m = timer[user_id][item]["m"]
			d = timer[user_id][item]["d"]
			h = timer[user_id][item]["h"]
			min = timer[user_id][item]["min"]
			s = timer[user_id][item]["s"]
			if (datetime(y,m,d,h,min,s)) < now :
				return True
			else :
				return False
		else :
			return True
	else :
		timer[user_id] = {
		"item1":{},
		"item2":{},
		"item3":{},
		"item4":{},
		"item5":{},
		"item6":{},
		"itemm6":{}
		}
		return True
		
@bot.message_handler(func=lambda message: True)
def _(msg):
	with open("data.json","r") as f :
		data = json.load(f)
		f.close()
	with open("timer.json","r") as f :
		timer = json.load(f)
		f.close()
	masg = msg.text
	massg = masg.split()
	idd = msg.from_user.id
	user_id = str(msg.from_user.id)
	cid = msg.chat.id
	item1 = item_timer("item1",user_id,data,timer)
	item2 = item_timer("item2",user_id,data,timer)
	item3 = item_timer("item3",user_id,data,timer)
	item4 = item_timer("item4",user_id,data,timer)
	item5 = item_timer("item5",user_id,data,timer)
	item6 = item_timer("item6",user_id,data,timer)
	
	if masg == "الاوامر" :
		if user_id == str(dev) :
			bot.reply_to(msg,'''
- راتب | لزيادو فلوسك
- بخشيش | لزيادة فلوسك
زرف (بلرد) | لزرف الفلوس
فلوسي | لعرض فلوسك
زرفي | لعرض الفلوس يلي زرفتهم
- مضاربه (العدد) | ياتفوز 0-90% ياتخسر 0-90%
- استثمار (العدد) | تزيد الفلوس بنسبة 0-15%
- حظ (العدد) | ياتدبل الفلوس ياتخسرهم
- اصنعي (الفلوس) |  علشان تصنع كود اكشط 
- ترسيت البنك | عشان تصفر لعبة البنك
- اكشط (الكود) | علشان تاخذ كود اكشط 
''')
		else :
			bot.reply_to(msg,'''
- راتب | لزيادو فلوسك
- بخشيش | لزيادة فلوسك
زرف (بلرد) | لزرف الفلوس
فلوسي | لعرض فلوسك
زرفي | لعرض الفلوس يلي زرفتهم
- مضاربه (العدد) | ياتفوز 0-90% ياتخسر 0-90%
- استثمار (العدد) | تزيد الفلوس بنسبة 0-15%
- حظ (العدد) | ياتدبل الفلوس ياتخسرهم
- اكشط (الكود) | علشان تاخذ كود اكشط 
''')
	if "حسابي" == masg :
		if user_id in data :
			bot.reply_to(msg,data[user_id]["code"])
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if "انشاء حساب بنكي" == masg :
		if user_id in data :
			bot.reply_to(msg,"عندك حساب بنكي")
		else :
			r = ("411"+"".join(random.choices(abc,k=13)))
			data[user_id] = {"code" : r,"cash":50,"zrf":0}
			bot.reply_to(msg,"تم انشاء حساب بنكي")
	if masg == "فلوسي" :
		if user_id in data :
			bot.reply_to(msg,f'فلوسك هي `{data[user_id]["cash"]}` ريال',parse_mode="markdown")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if masg == "زرفي" :
		if user_id in data :
			bot.reply_to(msg,f'الفلوس يلي زرفتهم هي : `{data[user_id]["zrf"]}` ريال' ,parse_mode="markdown")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if masg == "راتب" :
		if user_id in data :
			if item1 == True :
				job = random.choice(rateb_list)
				cash = job.split("الراتب : ")[1].split()[0]
				res = int(data[user_id]["cash"]) + int(cash)
				data[user_id]["cash"] = res
				timer_set("item1",user_id,data,timer,"minutes",10)
				bot.reply_to(msg,f"ايداع راتب لـ{msg.from_user.first_name} : \n{job}")
			else :
				now = datetime.now()
				y = timer[user_id]["item1"]["y"]
				m = timer[user_id]["item1"]["m"]
				d = timer[user_id]["item1"]["d"]
				h = timer[user_id]["item1"]["h"]
				min = timer[user_id]["item1"]["min"]
				s = timer[user_id]["item1"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تاخذ راتب، انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	
	if masg == "بخشيش" :
		if user_id in data :
			if item2 == True :
				cash = random.randint(20,2000)
				res = int(data[user_id]["cash"]) + int(cash)
				data[user_id]["cash"] = res
				timer_set("item1",user_id,data,timer,"minutes",10)
				bot.reply_to(msg,f'عطيتك بخشيش بقيمة {cash} ريال')
				
			else :
				now = datetime.now()
				y = timer[user_id]["item2"]["y"]
				m = timer[user_id]["item2"]["m"]
				d = timer[user_id]["item2"]["d"]
				h = timer[user_id]["item2"]["h"]
				min = timer[user_id]["item2"]["min"]
				s = timer[user_id]["item2"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تاخذ بخشيش انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if massg[0] == "حظ" :
		if user_id in data :
			if item3 == True :
				try :
					cash = int(massg[1])
					user_cash = int(data[user_id]["cash"])
					if cash > user_cash :
						bot.reply_to(msg,"فلوسك ماتكفي")
					elif cash < 0 :
						bot.reply_to(msg,"اقل عدد هو صفر ترا")
					else :
						r = random.choice("122")
						if r == "1" :
							user_cash = user_cash - cash
							cash *= 2
							res = cash + user_cash
							data[user_id]["cash"] = res
							bot.reply_to(msg,f'مبروك فزت بالحظ ، فلوسك الحين : {data[user_id]["cash"]}')
						else :
							user_cash = user_cash - cash
							cash -= cash
							res = cash + user_cash
							data[user_id]["cash"] = res
							bot.reply_to(msg,f'للاسف خسرت بلحظ ، فلوسك الحين : {data[user_id]["cash"]}',parse_mode="markdown")
						timer_set("item3",user_id,data,timer,"minutes",20)
				except :
					bot.reply_to(msg,"استعمل الامر كذا - حظ 500")
			else :
				now = datetime.now()
				y = timer[user_id]["item3"]["y"]
				m = timer[user_id]["item3"]["m"]
				d = timer[user_id]["item3"]["d"]
				h = timer[user_id]["item3"]["h"]
				min = timer[user_id]["item3"]["min"]
				s = timer[user_id]["item3"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تلعب حظ انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if massg[0] == "مضاربه" :
		if user_id in data :
			if item4 == True :
				try :
					cash = int(massg[1])
					user_cash = int(data[user_id]["cash"])
					if cash > user_cash :
						bot.reply_to(msg,"فلوسك ماتكفي")
					elif cash < 200 :
						bot.reply_to(msg,"اقل عدد هو 200 ترا")
					else :
						r = random.choice("122")
						if r == "1" :
							percent = random.randint(0,90)
							res = int(cash) / int(100) * int(percent) 

							res = int(res+cash)
							data[user_id]["cash"] = res
							bot.reply_to(msg,f'''مضاربه ناجح بنسبة {percent}% !
فلوسك الحين : `{res}`''',parse_mode="markdown")
						else :
							percent = random.randint(0,90)
							res = int(cash) / int(100) * int(percent)
							res = int(cash-res)
							data[user_id]["cash"] = res
							bot.reply_to(msg,f'''للاسف خسرت بنسبة {percent}% !
فلوسك الحين : `{res}`''',parse_mode="markdown")
						timer_set("item4",user_id,data,timer,"minutes",1)
				except :
					bot.reply_to(msg,"استعمل الامر كذا - مضاربه 500")
			else :
				now = datetime.now()
				y = timer[user_id]["item4"]["y"]
				m = timer[user_id]["item4"]["m"]
				d = timer[user_id]["item4"]["d"]
				h = timer[user_id]["item4"]["h"]
				min = timer[user_id]["item4"]["min"]
				s = timer[user_id]["item4"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تلعب مضاربه انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if massg[0] == "المطور" :
		bot.reply_to(msg,"مطور السورس : @Dar4k")
	if massg[0] == "استثمار" :
		if user_id in data :
			if item5 == True :
				try :
					cash = int(massg[1])
					user_cash = int(data[user_id]["cash"])
					if cash > user_cash :
						bot.reply_to(msg,"فلوسك ماتكفي")
					elif cash < 200 :
						bot.reply_to(msg,"اقل عدد هو 200 ترا")
					else :
						percent = random.randint(0,15)
						res = int(cash) / int(100) * int(percent)
						res = int(res+cash)
						data[user_id]["cash"] = res
						timer_set("item5",user_id,data,timer,"minutes",20)
						bot.reply_to(msg,f'''استثمار ناجح بنسبة {percent}% !
فلوسك الحين : `{res}`''',parse_mode="markdown")
				except :
					bot.reply_to(msg,"استعمل الامر كذا - استثمار 500")
			else :
				now = datetime.now()
				y = timer[user_id]["item5"]["y"]
				m = timer[user_id]["item5"]["m"]
				d = timer[user_id]["item5"]["d"]
				h = timer[user_id]["item5"]["h"]
				min = timer[user_id]["item5"]["min"]
				s = timer[user_id]["item5"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تستثمر انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if massg[0] == "تحويل" :
		if user_id in data :
			try :
				cash = int(massg[1])
				user_cash = int(data[user_id]["cash"])
				if cash > user_cash :
					bot.reply_to(msg,"فلوسك ماتكفي")
				elif cash < 200 :
					bot.reply_to(msg,"اقل عدد هو 200 ترا")
				else :
					masg = bot.reply_to(msg,'ارسل رقم الحساب الان : ')
					codee = []
					def codrr(msg) :
						if str(msg.from_user.id) == user_id :
							codee = msg.text
							for user_id2 in data :
								code = data[user_id2]["code"]
								if code == codee:
									if str(user_id2) == str(user_id) :
										bot.reply_to(msg,"تبي تحول لنفسك ?")
									else :
										cash2 = int(data[user_id2]["cash"])
										res1 = user_cash - cash
										res2 = cash + cash2
										data[user_id]["cash"] = res1
										data[user_id2]["cash"] = res2
										with open("data.json","w") as f :
											json.dump(data,f,indent=6)
											f.close()
										bot.reply_to(msg,f"تم تحويل{cash} الى حساب رقم {data[user_id2]['code']}")
										break
						else:
							pass
					bot.register_next_step_handler(masg, codrr)
					
			except Exception as e:
				bot.reply_to(msg,"استعمل الامر كذا - تحويل 500")
	if massg[0] == "زرف" :
		if user_id in data :
			if item6 == True:
				try :
					user_id2 = str(msg.reply_to_message.from_user.id)
					itemm6 = item_timer("itemm6",user_id2,data,timer)
					if itemm6 == True :
						cash = random.randint(20,1700)
						user_cash = int(data[user_id]["cash"])
						if user_id == user_id2 :
							bot.reply_to(msg,"شفيك تبي تزرف نفسك")
						else :
							for i in data :
								if str(i) == str(user_id2) :
									code = data[user_id2]["code"]
									cash2 = int(data[user_id2]["cash"])
									if cash2 <= 2000 :
										bot.reply_to(msg,"فلوسه اقل من 2000")
										break
									else :
										res1 = user_cash + cash
										res2 = cash2 - cash
										res3 = cash
										data[user_id]["cash"] = res1
										data[user_id2]["cash"] = res2
										data[user_id]["zrf"] = res3
										bot.reply_to(msg,f"تم زرفه {cash}")
										timer_set("item6",user_id,data,timer,"minutes",10)
										timer_set("itemm6",user_id2,data,timer,"minutes",10)
										break
					else :
						now = datetime.now()
						y = timer[user_id2]["itemm6"]["y"]
						m = timer[user_id2]["itemm6"]["m"]
						d = timer[user_id2]["itemm6"]["d"]
						h = timer[user_id2]["itemm6"]["h"]
						min = timer[user_id2]["itemm6"]["min"]
						s = timer[user_id2]["item6"]["s"]
						delt = str((datetime(y,m,d,h,min,s)) - now)
						s = delt.split(":")[2].split(".")
						min = delt.split(":")[1]
						bot.reply_to(msg,f"مسكين توه مزروف انتضر {min}:{s[0]} وتعال")
				except Exception as e:
					bot.reply_to(msg,"استعمل الامر كذا - زرف (بلرد)")
			else :
				now = datetime.now()
				y = timer[user_id]["item6"]["y"]
				m = timer[user_id]["item6"]["m"]
				d = timer[user_id]["item6"]["d"]
				h = timer[user_id]["item6"]["h"]
				min = timer[user_id]["item6"]["min"]
				s = timer[user_id]["item6"]["s"]
				delt = str((datetime(y,m,d,h,min,s)) - now)
				s = delt.split(":")[2].split(".")
				min = delt.split(":")[1]
				bot.reply_to(msg,f"ماتقدر تزرف انتضر {min}:{s[0]} وتعال")
		else :
			bot.reply_to(msg,"ماعندك حساب بنكي")
	if masg == "توب الفلوس" :
		list1 = []
		list2 = []
		for i in data :
			cash = int(data[i]["cash"])
			list1.append(cash)
		list1.sort(reverse=True)
		for i in list1 :
			cashh = i
			for j in data :
				cash = int(data[j]["cash"])
				if cashh == cash :
					name = bot.get_chat_member(msg.chat.id,j).user.first_name 
					list2.append(name)
				else :
					continue
		try :
			bot.reply_to(msg,f'''
🏅 - {list1[0]} 💵 | {list2[0]}
🥈 - {list1[1]} 💵 | {list2[1]}
🥉 - {list1[2]} 💵 | {list2[2]}
4 - {list1[3]} 💵 | {list2[3]}
5 - {list1[4]} 💵 | {list2[4]}
6 - {list1[5]} 💵 | {list2[5]}
7 - {list1[6]} 💵 | {list2[6]}
8 - {list1[7]} 💵 | {list2[7]}
9 - {list1[8]} 💵 | {list2[8]}
10 - {list1[9]} 💵 | {list2[9]}
''',parse_mode="markdown")
		except :
			bot.reply_to(msg,"لايوجد لاعبين كافيين لعرض التوب !")
	if masg == "توب الزرف" :
		list1 = []
		list2 = []
		for i in data :
			cash = int(data[i]["zrf"])
			list1.append(cash)
		list1.sort(reverse=True)
		for i in list1 :
			cashh = i
			for j in data :
				cash = int(data[j]["zrf"])
				if cashh == cash :
					name = bot.get_chat_member(msg.chat.id,j).user.first_name 
					list2.append(name)
				else :
					continue
		try :
			bot.reply_to(msg,f'''
🏅 - {list1[0]} 💵 | {list2[0]}
🥈 - {list1[1]} 💵 | {list2[1]}
🥉 - {list1[2]} 💵 | {list2[2]}
4 - {list1[3]} 💵 | {list2[3]}
5 - {list1[4]} 💵 | {list2[4]}
6 - {list1[5]} 💵 | {list2[5]}
7 - {list1[6]} 💵 | {list2[6]}
8 - {list1[7]} 💵 | {list2[7]}
9 - {list1[8]} 💵 | {list2[8]}
10 - {list1[9]} 💵 | {list2[9]}
''',parse_mode="markdown")
		except :
			bot.reply_to(msg,"لايوجد لاعبين كافيين لعرض التوب !")
	if massg[0] == "اصنعي"  :
		if msg.from_user.id == dev :
			try :
				cash = int(massg[1])
				code = "".join(random.choices(abc,k=6))
				akshtt.append(code)
				aksht[code] = cash
				bot.reply_to(msg,f'تم صنع `{code}` بقيمة {cash} !',parse_mode="markdown")
			except :
				pass
	if masg == "رستي الملفات"  :
		if msg.from_user.id == dev :
			with open("timer.json","w") as f :
				f.write("{}")
				bot.reply_to(msg,"تم ترسيت الملفات ! ")
				return
	if masg == "رستي البنك"  :
		if msg.from_user.id == dev :
			with open("data.json","w") as f :
				f.write("{}")
				bot.reply_to(msg,"تم ترسيت البنك !")
				return
	if massg[0] == "اكشط"  :
		for i in akshtt :
			if massg[1] == i :
				code = massg[1]
				akshtt.remove(code)
				cash = int(aksht[code])
				user_cash = int(data[user_id]["cash"])
				res = cash+user_cash
				data[user_id]["cash"] = res
				bot.reply_to(msg,f"مبروك ! ، كشطتها واخذت `{cash}` .",parse_mode="markdown")
	time.sleep(0.1)
	with open("data.json","w") as f :
		json.dump(data,f,indent=6)
		f.close()
	with open("timer.json","w") as f :
		json.dump(timer,f,indent=6)
		f.close()