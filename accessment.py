# -*- coding: utf-8 -*-


from __future__ import print_function	# For Py2/3 compatibility
import eel, json
from mailmerge import MailMerge
from datetime import date
import tkinter as tk
from tkinter import filedialog

eel.init('web')


template = "Template.docx"

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

file_path = "~/Downloads/"


@eel.expose
def setFolder():
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()


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
		names[tmp + "_" + data["content"][tmp]] = "selected"

	lang_total = 0
	for tmp in data["lang"]:
		lang_total += int(data["lang"][tmp])
		for i in range(1,5):
			if str(i) == data["lang"][tmp]:
				continue
			names[tmp + "_" + str(i)] = ""
		names[tmp + "_" + data["lang"][tmp]] = "selected"


	technical_total = 0
	for tmp in data["technical"]:
		technical_total += int(data["technical"][tmp])
		for i in range(1,5):
			names[tmp + "_" + str(i)] = ""
		names[tmp + "_" + data["technical"][tmp]] = "selected"

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
	document.write('result' + topzone['sname'] + '(' + topzone['sid'] + ')- ' + '{:%d-%b-%Y}'.format(date.today()) + '.docx')

	print(document.get_merge_fields())
	print(options)
	print(header)
	print(data)
	print(topzone)

eel.start('main.html', block=False, size=(1000, 600))
