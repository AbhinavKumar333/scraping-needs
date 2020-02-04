import time
import csv
import re

#----------------------csv file details-------------------------
# URL = 'https://www.upboardsolutions.com/class-4-evs'
file = 'maths_sol_9'
book = 'Balaji Publication Mathematics Grade 9 Hindi'
grade = '9'
subject = 'Maths'
chapter = ''
exercise = ''
question_no = ''
question = ''
answer = ''
link = ''
description = ''
#---------------------hindi text unicode--------------------
prashna = u'\u092A\u094D\u0930\u0936\u094D\u0928'
par = u'\u092A\u094D\u0930'
hal = u'\u0939\u0932'#\u0903
utar = u'\u0909\u0924\u094D\u0924\u0930'
ans2 = u'\u0939\u0941\u0932'#\u0903
abhyas = u'\u0905\u092D\u094D\u092F\u093E\u0938'
kitna = u'\u0915\u093F\u0924\u0928\u093E'
sikha = u'\u0938\u0940\u0916\u093E'
project = u'\u092A\u094D\u0930\u094B\u091C\u0947\u0915\u094D\u091F'
karya = u'\u0915\u093E\u0930\u094D\u092F'
humne = u'\u0939\u092e\u0928\u0947'
tum = u'\u0924\u0941\u092E'
type = 'Answer Type Questions'
bhi = u'\u092D\u0940'
karo = u'\u0915\u0930\u094B'
ka = u'\u0915'
kha = u'\u0916'
ga = u'\u0917'
#-----------------------extracting data from file------------
content=""
data=[]
with open(file+'.txt','r') as f1:
	content = f1.read().decode("utf-8")

qflag=0
aflag=0
qqflag=0
aaflag=0
d={}
count =0
cont = content.split('\n')
for c in cont:
	# print c

	chap = re.findall('Chapter\s\d+',c)
	# q = re.findall(re.compile(prashna+'\s\d+\.'+'|\('+ka+'\)|\('+kha+'\)|\('+ga+'\)'),c)
	q = re.findall(re.compile('^'+par+'\.\s'+'|'+prashna+'\.'+'|'+prashna+'\:'+'|'+'^'+prashna+'\s'),c)
	# q = re.findall(re.compile(prashna+'\s\d+\.'),c)
	a = re.findall(re.compile('^'+hal+'|'+'^'+utar),c)
	ex = re.findall(re.compile(type+'|'+abhyas+'\s'+prashna+'|'+'^'+abhyas+'|'+abhyas+'$'+'|'+kitna+'\s'+sikha+'|'+'^'+project+'\s'+karya+'|'+humne+'\s'+sikha+'|'+tum+'\s'+bhi+'\s'+karo),c)

	if(chap and description!=""):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = ""
		d['Question number']= question_no
		d['Question']= description
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		# link = ''
		description = ""
		aaflag=0
		qqflag=0
		# qflag=0
		aflag=0

	if(chap and aaflag==1 and qqflag==1):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = exercise
		d['Question number']= question_no
		d['Question']= question
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		description = ''
		# link = ''
		aaflag=0
		qqflag=0
		qflag=0
		aflag=0

	if(chap and aaflag==0 and qqflag==1):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = exercise
		d['Question number']= question_no
		d['Question']= question
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		description = ''
		# link = ''
		aaflag=0
		qqflag=0
		qflag=0
		aflag=0

	if(chap):
		count += 1
		chapter = c.encode("utf-8")
		link =''
		# link = URL + '-chapter-'+str(count)
		# link = 'https://www.upboardsolutions.com/balaji-class-10-maths-solutions-chapter-'+str(ce[0])+'-ex-'+str(ce[0])+'-'+str(ce[1])
		# print c
		continue

	if(ex and qqflag==1):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = exercise
		d['Question number']= question_no
		d['Question']= question
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		description = ''
		# link = ''
		aaflag=0
		qqflag=0
		# qflag=0
		aflag=0

	if(ex and description!=""):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = ""
		d['Question number']= question_no
		d['Question']= description
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		# link = ''
		description = ""
		aaflag=0
		qqflag=0
		# qflag=0
		aflag=0

	if(ex):
		exercise = c.encode("utf-8")
		# print c
		continue

	if(qflag==0 and aflag==0 and ex==None and chap==None):
		description += c.encode("utf-8")

	if q:
		if(qqflag==1 and aaflag==0):
			d={}
			d['Book'] = book
			d['Grade'] = grade
			d['Subject'] = subject
			d['Chapter']= chapter
			d['Exercise'] = exercise
			d['Question number']= question_no
			d['Question']= question
			d['Answer']= answer
			d['Link'] = link
			data.append(d)
			# chapter = ''
			# exercise = ''
			# question_no = ''
			question = ''
			answer = ''
			# link = ''
			aaflag=0
			qqflag=0
			qflag=0
			aflag=0
		aflag=0


	if a:
		qflag=0

	if(aaflag==1 and qqflag==1 and aflag==0):
		d={}
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter
		d['Exercise'] = exercise
		d['Question number']= question_no
		d['Question']= question
		d['Answer']= answer
		d['Link'] = link
		data.append(d)
		# chapter = ''
		# exercise = ''
		question_no = ''
		question = ''
		answer = ''
		# link = ''
		aaflag=0
		qqflag=0
		# qflag=0
		aflag=0

	if(qflag==1):
		question += c.encode("utf-8").lstrip() + '\n'
		qqflag=1
		# print c

	if(aflag==1 and qqflag==1):
		answer += c.encode("utf-8").lstrip() + '\n'
		aaflag=1
		# print c

	if(aflag==1 and qqflag==0):
		description += c.encode("utf-8").lstrip() +'\n'

	if(q):
		question_no = c.encode("utf-8")
		qflag=1
		aflag=0

	if(a):
		aflag=1
		qflag=0

d={}
d['Book'] = book
d['Grade'] = grade
d['Subject'] = subject
d['Chapter']= chapter
d['Exercise'] = exercise
d['Question number']= question_no
d['Question']= question
d['Answer']= answer
d['Link'] = link
data.append(d)

with open(file+'.csv','wb') as f:
	w = csv.DictWriter(f,['Book','Grade','Subject','Chapter','Exercise','Question number','Question','Answer','Link'])
	w.writeheader()
	for da in data:
		w.writerow(da)
