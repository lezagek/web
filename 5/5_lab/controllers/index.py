import constants

from app import app 
from flask import render_template, request  

@app.route('/', methods=['GET', 'POST'])  

def index():
    # для каждого передаваемого параметра формы  нужно установить    
    # значение по умолчание, на случай если пользователь ничего не введет     
    name = ""   
    gender = ""    
    program_id = 0    
    # список из номеров выбранных пользователем дисциплин     
    subject_id = []     
    # список из выбранных пользователем дисциплин     
    subjects_select = []

    if request.method == "POST":
        if request.form['action'] == 'Отправить':
            # получаем параметр из формы     
            name = request.values.get('username')       
            gender = request.values.get('gender')
            program_id = request.values.get('program')
            subject_id = request.values.getlist('subject_list')     
            # формируем список из выбранных пользователем дисциплин     
            subjects_select = [constants.subjects[int(i)] for i in subject_id]
            
        if request.form['action'] == 'Очистить':
            name = ""   
            gender = ""    
            program_id = 0    
            # список из номеров выбранных пользователем дисциплин     
            subject_id = []     
            # список из выбранных пользователем дисциплин     
            subjects_select = []
        

    html = render_template(         
        'index.html',         
        name = name,
        gender = gender,
        program = constants.programs[int(program_id)],         
        program_list = constants.programs,
        len = len,         
        subjects_select = subjects_select,         
        subject_list = constants.subjects
    )
    
    return html

    