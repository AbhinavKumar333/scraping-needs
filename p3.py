from selenium import webdriver
import time
import sys
import re
import csv

def gotopage(url):
	driver = webdriver.Chrome('/Users/abhinavkumar/Downloads/chromedriver')
	driver.get(url)
	time.sleep(30)
	data = []	
	while 1:
		d = {}			
		time.sleep(3)
		qno = driver.find_element_by_css_selector('.flex.dark-gray.ma0.mb1.flex-shrink-0.ques-label')		

		a = ''
		ans = driver.find_element_by_css_selector(".mt2.mid-gray.f4.custom-html-style.pv2")		
		if(len(ans.find_elements_by_css_selector('img'))>0):
			j = ans.find_elements_by_css_selector('img')
			for an in j:
				global a
				a = a +'<img src="'+ an.get_attribute('src') +'"/>' + '\n'
		a = a + ans.text

		t = ''
		quest = driver.find_element_by_css_selector(".dark-gray.ma0.custom-html-style.pv2.ques-title")		
		if(len(quest.find_elements_by_css_selector('img'))>0):
			k = quest.find_elements_by_css_selector('img')
			for que in k:
				global t
				t = t +'<img src="'+ que.get_attribute('src') +'"/>' + '\n'				
		t = t + quest.text
		
		if 'A. ' in t:
			options = 'A.' + t.split('A.')[1]
			d['question_text'] = t.split('A.')[0].encode('utf-8')
		elif '(a) ' in t:
			options = '(a) ' + t.split('(a) ')[1]
			d['question_text'] = t.split('(a) ')[0].encode('utf-8')
		elif 'a) ' in t:
			options = 'a) ' + t.split('a) ')[1]
			d['question_text'] = t.split('a) ')[0].encode('utf-8')
		else:
			options = 'NA'

		
		d['options'] = options.encode('utf-8')
		d['solution_text'] = a.encode('utf-8')
		d['question_no'] = qno.text.split('\n')[0].encode('utf-8')
		print d['question_no']
		# print d['question_text']
		# print d['solution_text']

		try:
			driver.find_element_by_css_selector('.fw7.ph2.pv3.pv2-l.flex.border-box.no-underline.self-end.ml-auto.ma0-l.pl3-l.w-50.items-center.hover-bg-washed-blue').click()
		except Exception as e:
			print e			
			data.append(d)
			break
		data.append(d)
		# break
	with open("science6-12.csv",'wb') as f:
		writer = csv.DictWriter(f, ['question_text','options','solution_text','question_no'])
		writer.writeheader()
		for da in data:		
			# print da			
			writer.writerow(da)

url = sys.argv[1]
gotopage(url)


# gotopage('https://school.gradeup.co/ex-1-q1-the-product-of-the-place-values-of-two-2-s-in-428721-i-1nklcf')
# gotopage('https://school.gradeup.co/the-number-of-significant-figures-in-0-06900-is-i-1nm11h')
# c = 1
# def signup():
# 	driver.find_element_by_css_selector('.ma0.tc.pointer.tracked-sm.outline-0.b--solid.no-user-select.dn.flex-l.bg-white.school-blue.bn.br-pill.ph4.pv2.ml4-l.ml-auto.mr3.ttu.f5').click()
# 	driver.find_element_by_css_selector('.blue.f6.mb0.underline').click()
# 	inp = driver.find_elements_by_css_selector('.auth__field.outline-0.f6.db.w-100.pv2.b--black-10.bb.br-0.bt-0.bl-0')
# 	inp[0].send_keys('qwerty')	
# 	inp[1].send_keys('qwerty'+c+'@mail.com')
# 	inp[2].send_keys('qwerty123')
# 	driver.find_element_by_css_selector('.btn.auth__button.js-auth-register.white.bn.db.pv3.outline-0.w-100.w-40-l.tc pointer.bg-silver').click()
# 	global c
# 	c = c+1
