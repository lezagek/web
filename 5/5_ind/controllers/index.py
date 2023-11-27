import constants
import calculation

from app import app 
from flask import render_template, request  

@app.route('/', methods=['GET', 'POST'])  

def index():

    num = 2
    vector_first = []
    vector_second = []
    # список из номеров выбранных пользователем операций     
    operations_id = []     
    # список из выбранных пользователем операций     
    operations_select = []

    res = []


    if request.method == "POST":
        if request.form['action'] == 'Показать':
            num = request.values.get('num')
            vector_first = request.values.getlist('vector_first')
            vector_second = request.values.getlist('vector_second')
            operations_id = []
            operations_select = []
            res = []

        if request.form['action'] == 'Вычислить':
            num = request.values.get('num')
            vector_first = request.values.getlist('vector_first')
            vector_second = request.values.getlist('vector_second')
            operations_id = request.values.getlist('operations_list')    
            operations_select = [constants.operations[int(i)] for i in operations_id]
            res = calculation.calculations(operations_select, vector_first, vector_second)

        elif request.form['action'] == 'Очистить':
            num = 2
            vector_first = []
            vector_second = []    
            operations_id = []       
            operations_select = []
            res = []

    html = render_template(         
        'index.html',
        num = num,
        vector_first = vector_first,
        vector_second = vector_second,
        len = len,
        int = int,
        operations_list = constants.operations,
        operations_select = operations_select,
        res = res,
        enumerate = enumerate
    )


    return html