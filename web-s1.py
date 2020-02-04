from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
import csv
import re
# URL = 'https://www.upboardsolutions.com/class-2-maths'
# URL = 'https://www.upboardsolutions.com/class-3-maths'
# URL = 'https://www.upboardsolutions.com/class-3-evs'
# URL = 'https://www.upboardsolutions.com/class-4-maths'
# URL = 'https://www.upboardsolutions.com/class-4-evs'
# URL = 'https://www.upboardsolutions.com/class-4-science'
# URL = 'https://www.upboardsolutions.com/class-5-maths'
# URL = 'https://www.upboardsolutions.com/class-5-evs'
# URL = 'https://www.upboardsolutions.com/class-5-science'
# URL = 'https://www.upboardsolutions.com/class-6-maths'
# URL = 'https://www.upboardsolutions.com/class-6-science'
# URL = 'https://www.upboardsolutions.com/class-7-maths'
# URL = 'https://www.upboardsolutions.com/class-7-science'
# URL = 'https://www.upboardsolutions.com/class-8-maths'
# URL = 'https://www.upboardsolutions.com/class-8-science'
# URL = 'https://www.upboardsolutions.com/class-10-maths'
# URL = 'https://www.upboardsolutions.com/class-10-science'
# URL = 'https://www.upboardsolutions.com/class-9-maths'
# URL = 'https://www.upboardsolutions.com/class-9-science'
# URL = 'https://www.upboardsolutions.com/class-12-maths'
# URL = 'https://www.upboardsolutions.com/class-12-physics'
# URL = 'https://www.upboardsolutions.com/class-12-chemistry'
# URL = 'https://www.upboardsolutions.com/class-12-biology'
# URL = 'https://www.upboardsolutions.com/class-11-maths'
# URL = 'https://www.upboardsolutions.com/class-11-physics'
# URL = 'https://www.upboardsolutions.com/class-11-chemistry'
# URL = 'https://www.upboardsolutions.com/class-11-biology'
# URL = 'https://www.upboardsolutions.com/balaji-publications-mathematics-class-10-solutions/'
URL = 'https://www.upboardsolutions.com/balaji-publications-mathematics-class-9-solutions/'
# file = '3_evs.csv'
file = 'maths_sol_9'
book = 'Balaji Publication Mathematics Grade 9 Hindi'
grade = '9'
subject = 'Maths'
#----------------------connection--------------------------------------
browser = webdriver.Chrome(executable_path='/home/abhinav/chromedriver')
browser.get(URL)
time.sleep(1.5)
#----------------------get chapters------------------------------------
chapters=[]
content = browser.page_source
soup = BS(content,'html5lib')
clas = soup.find('div',attrs={'class':'entry-content'})
ul = clas.findAll('ul')
for u in ul:
	li = u.findAll('li')
	for l in li:
		a = l.find('a')
		if(a):
			t = a.text
			if(re.findall('Click to',t)):
				continue
			chapters.append(t)
#---------------------hindi text unicode--------------------
prashna = u'\u092A\u094D\u0930\u0936\u094D\u0928'
par = u'\u092A\u094D\u0930'
hal = u'\u0939\u0932'#\u0903
utar = u'\u0909\u0924\u094D\u0924\u0930-'
ans2 = u'\u0939\u0941\u0932'#\u0903
abhyas = u'\u0905\u092D\u094D\u092F\u093E\u0938'
kitna = u'\u0915\u093F\u0924\u0928\u093E'
sikha = u'\u0938\u0940\u0916\u093E'
project = u'\u092A\u094D\u0930\u094B\u091C\u0947\u0915\u094D\u091F'
karya = u'\u0915\u093E\u0930\u094D\u092F'
type = 'Answer Type Questions'
ka = u'\u0915'
kha = u'\u0916'
ga = u'\u0917'
#--------------------calling chapter------------------------
data=[]
count=0
enter=""
print chapters
for chapter in chapters:
		qflag=0
		aflag=0
		aaflag=0
		qqflag=0
		eflag=0
		content = ""
		exercise = ""
		d={}
		t = chapter.split('Ex ')
		ce = t[1].split('.')
		# print ce
		count += 1
		# tURL = URL+'-chapter-'+str(count)
		tURL = 'https://www.upboardsolutions.com/balaji-class-9-maths-solutions-chapter-'+str(ce[0])+'-ex-'+str(ce[0])+'-'+str(ce[1])
		# tURL = 'https://www.upboardsolutions.com/class-3-maths-chapter-2'
		gu = browser.get(tURL)
		time.sleep(1)
		new_content = browser.page_source
		soup1 = BS(new_content,'html5lib')
		clas = soup1.find('div',attrs={'class':'entry-content'})
		tags = clas.findAll(re.compile(r'p|ol|ul'))
# -----------------------------------extracting book data----------------------------
		for tag in tags:
			content = content + tag.text + "\n"
			if(tag.find('img')):
				img_src = tag.find('img')['src']
				img = '<p><img src="'+img_src+'"/></p>'
				content = content + img + "\n"
		cont = content.split('\n')
		d['Question'] = ""
		d['Answer'] = ""
		d['Book'] = book
		d['Grade'] = grade
		d['Subject'] = subject
		d['Chapter']= chapter.encode("utf-8")
		d['Exercise'] = exercise
		d['Link'] = tURL
# -----------------------------scraping------------------------
		enter += chapter + '\n'
		for c in cont:
			# print c+"---------"
			if(re.findall(r'Click to|adsbygoogle|UP Board|upboardsolutions',c)):
				continue
			if(c):
				enter += c+'\n'
			ex = re.findall(re.compile(abhyas+'|'+kitna+'\s'+sikha+'|'+project+'\s'+karya),c)
			if(ex):
				if(eflag==1):
						exercise = ex[0].encode("utf-8")
						continue
				# print ex
				exercise = ex[0].encode("utf-8")
				d['Exercise'] = exercise
				eflag = 1
			if(eflag==0):
				continue

			# break
			# q = re.findall(re.compile(prashna+'\s\d+\.'+'|\('+ka+'\)|\('+kha+'\)|\('+ga+'\)'),c)
			q = re.findall(re.compile(prashna+'\s\d+\.'+'|'+par+'\s'),c)
			q = re.findall(re.compile(prashna+'\s\d+\.'),c)
			if q:
				aflag=0
				# if(qflag==1):
				# 	d['Question']=""
				# print q[0]
			a = re.findall(re.compile(hal+':'+'|'+utar),c)
			if a:
				qflag=0
				# print a[0]
			if(aaflag==1 and qqflag==1 and aflag==0):
				# print d
				data.append(d)
				d={}
				d['Book'] = book
				d['Grade'] = grade
				d['Subject'] = subject
				d['Chapter']= chapter.encode("utf-8")
				d['Exercise'] = exercise
				d['Link'] = tURL
				d['Question']=""
				d['Answer']=""
				d['Question number']=""
			if(qflag==1):
				# print c
				d['Question'] += c.encode("utf-8").lstrip() + '\n'
				qqflag=1
			if(aflag==1):
				d['Answer'] += c.encode("utf-8").lstrip() + '\n'
				aaflag=1
				# print c
			if(q):
				# print "q"
				d['Question number'] = q[0].encode("utf-8")
				qflag=1
				aflag=0
				aaflag=0
				qqflag=0
			if(a):
				# print "a"
				aflag=1
				qflag=0
		data.append(d)
		# break
#------------------------------------ end --------------------------------------
# with open(file,'wb') as f:
# 	w = csv.DictWriter(f,['Book','Grade','Subject','Chapter','Exercise','Question number','Question','Answer','Link'])
# 	w.writeheader()
# 	for da in data:
# 		w.writerow(da)

with open(file+'.txt','w') as f:
	f.write(enter.encode("utf-8"))
