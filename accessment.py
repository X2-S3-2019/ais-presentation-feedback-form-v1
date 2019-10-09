# -*- coding: utf-8 -*-


from __future__ import print_function	# For Py2/3 compatibility
import eel, json, os, datastore, sys
from mailmerge import MailMerge
from datetime import date
import tkinter as tk
from tkinter import filedialog
import names, time
import smtplib, webbrowser
from email.mime.text import MIMEText
from email.header import Header



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

template = resource_path("./template/Template.docx")
db_name = os.path.expanduser('~') + "/.ais.db"
file_path = os.getcwd()

eel.init('web')
datastore.initDb(db_name);


mail_host = 'smtp.gmail.com'  
mail_user = 'wangdw2012'  
mail_pass = '@Shaswsm15'
sender = 'wangdw2012@gmail.com'  
receivers = ['shasw2006@163.com',"cm2001218@gmail.com", "fach340@ess.ais.ac.nz", "alba632@ess.ais.ac.nz"]


#set([
# 'ideas_3', 'ideas_1', 'ideas_4', 'ideas_2',
# 'research_4', 'research_1', 'research_2', 'research_3',
# 'enthusiasm_4', 'enthusiasm_2', 'enthusiasm_3', 'enthusiasm_1',
# 'argument_2', 'argument_1', 'argument_4', 'argument_3',
# 'elocution_2', 'elocution_3', 'elocution_1', 'elocution_4',
# 'focus_2', 'focus_3','focus_4', 'focus_1',
# 'eye_contact_4', 'eye_contact_2', 'eye_contact_3', 'eye_contact_1',
# 'visual_aids_2', 'visual_aids_3',  'visual_aids_1',  'visual_aids_4',
# 'knownlege_2', 'knownlege_3', 'knownlege_1', 'knownlege_4',
# 'questions_1', 'questions_4', 'questions_2', 'questions_3',
# 'QA_4', 'QA_3', 'QA_2', 'QA_1',
# 'organization_4',  'organization_2', 'organization_3',  'organization_1'
# # 'SID', 'SNAME', 'content_total',  'date', 'score', technical_total', 'TOPIC',  'lang_total',])

#{"content":{"focus":"4","organization":"3","visual_adis":"2","QA":"1"},
#"lang":{"eye_contact":"2","enthusiasm":"3","elocution":"4"},
#"technical":{"knowledge":"3","research":"2","ideas":"1","argument":"2","questions":"3"}}

#def initDb():
#    try:
#        conn = sqlite3.connect(db_name)
#    except Error:
 
#        print(Error)
 
#    finally:
 
#        con.close()
#    return True

@eel.expose
def createCourse(course_name, course_id):
    datastore.createCourse(course_name, course_id)
    return True

@eel.expose
def getCourses():
    return datastore.getCourses()

@eel.expose
def createPresentation(course_id, presentation_date, presentation_name):
    datastore.createPresentation(course_id, presentation_date, presentation_name)
    return True

@eel.expose
def getPresentations(course_id):
    return datastore.getPresentations(course_id)

@eel.expose
def setFolder():
	global file_path
	application_window = tk.Tk()
	try:
		application_window.withdraw()
		application_window.wm_attributes('-topmost',1)
		application_window.update()
		file_path = filedialog.askdirectory(
						parent=application_window,
						initialdir=os.getcwd(),
						title="Please select a folder:")
		application_window.quit()
		print(file_path)
	except Exception as e:
		print(e)
		return False
	return True

@eel.expose
def getRandomStudentFullName():
    return names.getRandomFullName()

@eel.expose
def generdate_word(options, header):
	data = json.loads(options)
	topzone = json.loads(header)

	document = MailMerge(template)

	names = {}

	content_total = 0
	print(data)

	for tmp in data["content"]:
		content_total += int(data["content"][tmp])
		for i in range(1,5):
			names[tmp + "_" + str(i)] = ""
		names[tmp + "_" + data["content"][tmp]] = "SELECTED"

	lang_total = 0
	for tmp in data["lang"]:
		lang_total += int(data["lang"][tmp])
		for i in range(1,5):
			if str(i) == data["lang"][tmp]:
				continue
			names[tmp + "_" + str(i)] = ""
		names[tmp + "_" + data["lang"][tmp]] = "SELECTED"


	technical_total = 0
	for tmp in data["technical"]:
		technical_total += int(data["technical"][tmp])
		for i in range(1,5):
			names[tmp + "_" + str(i)] = ""
		names[tmp + "_" + data["technical"][tmp]] = "SELECTED"

	score = content_total + lang_total + technical_total

	print(document.get_merge_fields())
	print(len(document.get_merge_fields()))


	document.merge(
		SNAME = topzone['sname'],
		SID = topzone['sid'],
		TOPIC = topzone['topic'],
		date='{:%d-%b-%Y}'.format(date.today()),
		technical_total = str(technical_total),
		content_total = str(content_total),
		lang_total = str(lang_total),
		score = str(score),
		score_percentage = str(topzone['score_percentage']) + '%',
		ideas_1 = names['ideas_1'],
		ideas_2 = names['ideas_2'],
		ideas_3 = names['ideas_3'],
		ideas_4 = names['ideas_4'],
		research_1 = names['research_1'],
		research_2 = names['research_2'],
		research_3 = names['research_3'],
		research_4 = names['research_4'],
		enthusiasm_1 = names['enthusiasm_1'],
		enthusiasm_2 = names['enthusiasm_2'],
		enthusiasm_3 = names['enthusiasm_3'],
		enthusiasm_4 = names['enthusiasm_4'],
		argument_1 = names['argument_1'],
		argument_2 = names['argument_2'],
		argument_3 = names['argument_3'],
		argument_4 = names['argument_4'],
		elocution_1 = names['elocution_1'],
		elocution_2 = names['elocution_2'],
		elocution_3 = names['elocution_3'],
		elocution_4 = names['elocution_4'],
		focus_1 = names['focus_1'],
		focus_2 = names['focus_2'],
		focus_3 = names['focus_3'],
		focus_4 = names['focus_4'],
		eye_contact_1 = names['eye_contact_1'],
		eye_contact_2 = names['eye_contact_2'],
		eye_contact_3 = names['eye_contact_3'],
		eye_contact_4 = names['eye_contact_4'],
		visual_aids_1 = names['visual_aids_1'],
		visual_aids_2 = names['visual_aids_2'],
		visual_aids_3 = names['visual_aids_3'],
		visual_aids_4 = names['visual_aids_4'],
		knowledge_1 = names['knowledge_1'],
		knowledge_2 = names['knowledge_2'],
		knowledge_3 = names['knowledge_3'],
		knowledge_4 = names['knowledge_4'],
		questions_1 = names['questions_1'],
		questions_2 = names['questions_2'],
		questions_3 = names['questions_3'],
		questions_4 = names['questions_4'],
		QA_1 = names['QA_1'],
		QA_2 = names['QA_2'],
		QA_3 = names['QA_3'],
		QA_4 = names['QA_4'],
		organization_1 = names['organization_1'],
		organization_2 = names['organization_2'],
		organization_3 = names['organization_3'],
		organization_4 = names['organization_4']
	);
	filename = file_path + "/" + 'result-' + topzone['sname'] + '(' + topzone['sid'] + ')-' + '{:%d-%b-%Y}'.format(date.today()) + '.docx'
	print(filename)

	try:
		document.write(filename)
		pass
	except Exception as e:
		eel.AisAlert("error occures!" + e)
		pass
	# eel.showSurvey()
	eel.showSuccessfulSave(filename)

	# print(document.get_merge_fields())
	# print(options)
	# print(header)
	# print(data)
	# print(topzone)

@eel.expose
def sendRating(rating):
	message = MIMEText('We have a new rating!! The rating is ' + str(rating), 'plain', 'utf-8')
	message['From'] = Header(sender, 'utf-8')
	message['To'] =  Header(", ".join(receivers), 'utf-8')
	subject = 'AIS evaluation desk top apprating result!!'
	message['Subject'] = Header(subject, 'utf-8')
	try:
		smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
		# smtpObj.connect(mail_host)
		# smtpObj.ehlo()
		# smtpObj.starttls()
		smtpObj.login(mail_user,mail_pass) 
		smtpObj.sendmail(sender,receivers, message.as_string())
		smtpObj.quit() 
	except smtplib.SMTPException as e:
		print('error',e) 
	return True

@eel.expose
def openURL():
	url = "https://sites.google.com/view/evaluate-app/feedback-forms"
	webbrowser.open(url);



@eel.expose
def say_hello_py(x):
   print('Hello from %s' % x)
   time.sleep(0.5)

   
say_hello_py('Python World!');
eel.say_hello_js('Python World!')
print(names.getRandomName() + ' ' + names.getRandomSurName())

#print(datastore.getPresentations('wd40'))
eel.start('splash.html', size=(1000, 600), disable_cache=True)




