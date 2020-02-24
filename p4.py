from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import time
import sys
import re
import csv

def gotopage(url):
	driver = webdriver.Chrome('/Users/abhinavkumar/Downloads/chromedriver')
	driver.get(url)
	# time.sleep(3)
	# driver.find_element_by_css_selector('.ma0.tc.pointer.tracked-sm.outline-0.b--solid.no-user-select.dn.flex-l.bg-white.school-blue.bn.br-pill.ph4.pv2.ml4-l.ml-auto.mr3.ttu.f5').click()
	# inp = driver.find_elements_by_css_selector('.auth__field.outline-0.f6.db.w-100.pv2.bb.br-0.bt-0.bl-0.b--black-10')
	# inp[0].send_keys('abhinavkumar333.ak@gmail.com')
	# inp[1].send_keys('qwerty123')	
	# driver.find_element_by_css_selector('.btn.pv3.auth__button.w-100.w-40-l.white.bn.db.fw1.outline-0.tc.pointer.bg-blue-gradient').click()	
	# time.sleep(3)
	chap = driver.find_element_by_css_selector('.mid-gray.flex-grow-1.overflow-ellipsis.fw7').text
	data = []	
	prev_d = {}
	coun = driver.find_elements_by_css_selector('.ba.b--black-10.silver.flex.grow-large.items-center.justify-center.w2-l.h2-l.w2-5.h2-5.border-box.f7.br-100.mt3.no-underline.ml3.overflow-ellipsis')
	coun = coun[-1].text
	# print coun.text
	while 1:		
		try:
			time.sleep(2)
			# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.flex.dark-gray.ma0.mb1.flex-shrink-0.ques-label')))			
			cn = driver.find_element_by_css_selector('.bg-gradient-blue.white.selected-question.flex.grow-large.items-center.justify-center.w2-l.h2-l.w2-5.h2-5.border-box.f7.br-100.mt3.no-underline.ml3.overflow-ellipsis').text
			# print cn
			# print coun.text
			# print cn==coun.text
			if(len(driver.find_elements_by_css_selector('.flex.flex-row.w-100'))>0):
				driver.find_element_by_css_selector('.js-close-auth.db.pointer.login-dismiss.absolute.right-2.top-2.z-13').click()
			d={}
			content = driver.page_source
			soup = BS(content,'lxml')
			qno = driver.find_element_by_css_selector('.flex.dark-gray.ma0.mb1.flex-shrink-0.ques-label')
			
			quest = soup.find('h1',attrs={'class':"dark-gray ma0 custom-html-style pv2 ques-title"})
			qt = ''		
			for q in quest:
				q = q.encode('utf-8')
				# q= q.replace('<span>','')
				# q= q.replace('</span>','')
				# q= q.replace('<p>','')
				# q= q.replace('</p>','')
				# q= q.replace('<br/>','')
				# q= q.replace('<span lang="EN-US">','')
				# q= q.replace('<sup>','')
				# q= q.replace('<sub>','')
				q = re.sub(r'(?i)<(?!img|/img).*?>', '', q)
				qt = qt + q + '\n'
			# for q in quest:
			# 	print q
			# 	if(q==None or q==''):
			# 		continue
			# 	print q
				# for i in q:
				# 	print i
				# 	if(i.find('img')):	
				# 		print i
				# print q.text
				# if(q.find('img')):
					# print q.find('img')['src']
			# for q in quest.findAll(['span','p']):			
			# 	if(q.find('img')):
			# 		# if(q.text!=''):
			# 		# 	qt = qt + q.text + '\n'
			# 		img_src = q.find('img')['src']
			# 		if(q_img_src==img_src):
			# 			print 'skip'
			# 			continue
			# 		global q_img_src	
			# 		q_img_src = img_src			
			# 		img = '<p><img src="'+img_src+'"/></p>'
			# 		qt = qt + img + '\n'
			# 	else:				
			# 		if(q_t==q.text):
			# 			continue
			# 		global q_t
			# 		q_t = q.text
			# 		qt = qt + q.text + '\n'

			ans = soup.find('div',attrs={'class':'mt2 mid-gray f4 custom-html-style pv2'})
			at = ''		
			for a in ans:
				a = a.encode('utf-8')
				# a= a.replace('<span>','')
				# a= a.replace('</span>','')
				# a= a.replace('<p>','')
				# a= a.replace('</p>','')
				# a= a.replace('<br/>','')
				a = re.sub(r'(?i)<(?!img|/img).*?>', '', a)
				at = at + a + '\n'
			# for a in ans:
			# 	print a.text
			# 	if(a.find('img')):
			# 		print a.find('img')['src']
				# print '----------------------------------------------'
			# for a in ans.findAll(['span','p']):
			# 	if(a.find('img')):
			# 		if(a_t==a.text):
			# 			continue
			# 		global a_t
			# 		a_t = a.text
			# 		at = at + a.text + '\n'	
			# 		img_src = a.find('img')['src']
			# 		if(a_img_src==img_src):
			# 			print 'skip'
			# 			continue
			# 		global a_img_src
			# 		a_img_src = img_src
			# 		img = '<p><img src="'+img_src+'"/></p>'
			# 		at = at + img + '\n'
			# 	else:
			# 		if(a_t==a.text):
			# 			continue
			# 		global a_t
			# 		a_t = a.text
			# 		at = at + a.text + '\n'	

			if 'A. ' in qt:
				opt = re.split('[A-Z]\.\s*',qt)
				# print len(opt)
				if(len(opt)==5):
					options = 'A.' + qt.split('A.')[1]			
					d['question_text'] = qt.split('A.')[0]
				else:
					options = 'NA'
					d['question_text'] = qt
			# elif '(a) ' in t:
			# 	options = '(a) ' + t.split('(a) ')[1]
			# 	d['question_text'] = t.split('(a) ')[0].encode('utf-8')
			# elif 'a) ' in t:
			# 	options = 'a) ' + t.split('a) ')[1]
			# 	d['question_text'] = t.split('a) ')[0].encode('utf-8')
			else:
				options = 'NA'
				d['question_text'] = qt

			
			d['options'] = options
			d['solution_text'] = at
			d['question_no'] = qno.text.split('\n')[0]
			d['book'] = 'NCERT Exemplar Class 12 Biology'
			d['grade'] = 'Grade 12'
			d['subject'] = 'Biology'
			d['path'] = driver.current_url
			d['chapter'] = chap
			print d['question_no']
			# print d['question_text']
			# print d['solution_text']
		
			driver.find_element_by_css_selector('.fw7.ph2.pv3.pv2-l.flex.border-box.no-underline.self-end.ml-auto.ma0-l.pl3-l.w-50.items-center.hover-bg-washed-blue').click()			
		except Exception as e:
			print e
			if(prev_d!=d):			
				data.append(d)
				prev_d = d			
			# print "".join(cn.split())==str(coun)
			if(cn==coun):
				break
			driver.get(driver.current_url)
		if(prev_d!=d):
			data.append(d)
			prev_d = d
		# break
	with open("bio12-15.csv",'wb') as f:
		writer = csv.DictWriter(f, ['question_text','options','solution_text','question_no','book','grade','subject','path','chapter'])
		writer.writeheader()
		for da in data:		
			if(da==''):
				continue
			# print da	
			try:		
				# da.to_csv(f, header=False,  index=False, encoding="utf-8")
				writer.writerow(da)
			except Exception as e:
				print e

url = sys.argv[1]
gotopage(url)