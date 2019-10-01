# -*- coding: utf-8 -*-



import json, sqlite3
from sqlite3 import Error
db = ''
def initDb(db_name):
    global db
    db = db_name
    try:
        con = sqlite3.connect(db_name)
    except Error:
        print(Error)
        con.close()
    
    crs = con.cursor()    
    crs.execute('create table if not exists courses (id integer primary key autoincrement, course_id, course_name)')
    crs.execute('create table if not exists presentations (id integer primary key autoincrement, p_name, p_date, course_id)')
    crs.execute('create table if not exists students (id integer primary key autoincrement, student_id, student_fname, student_sname)')
    crs.execute('create table if not exists course_students (id integer primary key autoincrement, student_id, course_id)')
    crs.execute('create table if not exists marks (id integer primary key autoincrement, student_id, course_id, presentation_id, content_focus, content_organization, content_visual, content_qa, lang_eye, lang_enth, lang_eloc, tech_knowl, tech_research, tech_discus, tech_atgument, tech_quest)')
    return True

def getCourses():
    try:
        con = sqlite3.connect(db)
    except Error:
        print(Error)
        con.close()
    
    crs = con.cursor()    
    crs.execute('select id as id, course_id, course_name as couse_name from courses') 
    courses = crs.fetchall() 
    return courses

def createCourse(course_name, course_id):
    try:
        con = sqlite3.connect(db)
    except Error:
        print(Error)
        con.close()

    crs = con.cursor()    
    crs.execute('insert into courses values (?, ?, ?)', (None, course_id, course_name))
    con.commit()
    con.close();
    return True

def createPresentation(course_id, presentation_date, presentation_name):
    try:
        con = sqlite3.connect(db)
    except Error:
        print(Error)
        con.close()

    crs = con.cursor()    
    crs.execute('insert into presentations values (?, ?, ?, ?)', (None, presentation_name, presentation_date, course_id))
    con.commit()
    con.close();
    return True

def getPresentations(course_id):
    try:
        con = sqlite3.connect(db)
    except Error:
        print(Error)
        con.close()
    
    crs = con.cursor()    
    crs.execute('select id, p_name, p_date from presentations where course_id = :course_id', {'course_id': course_id}) 
    presentations = crs.fetchall()

    return presentations