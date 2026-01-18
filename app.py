import math
from flask import Flask, render_template, request, redirect, url_for
from linked_list import LinkedList
from infix_postfix import InfixToPostfixConverter

app = Flask(__name__)
ll = LinkedList()
converter = InfixToPostfixConverter()

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/profile')
def profile():
    return render_template('profile.html', active_page='profile')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)
    
@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    area = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        if radius: 
            try:
                radius = float(radius)
                area = round(math.pi * (radius**2), 2)
            except ValueError:
                area = 'Invalid Input. Please Enter a Number.'
    return render_template('areaofcircle.html', area=area)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    area = None
    if request.method == 'POST':
        height = request.form.get('height', '')
        base = request.form.get('base', '')
        if base and height:
            try:
                base = float(base)
                height = float(height)
                area = (base*height)/2
            except ValueError:
                area = 'Invalid Input. Pleae Enter a Number.'
    return render_template('areaoftriangle.html', area=area)
 
@app.route('/works')
def works():
    return render_template('works.html', active_page='works')

@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist():
    return render_template('linked-list.html', linked_list=ll.print_list(), active_page='works')

@app.route('/linked-list/insert_beginning', methods=['POST'])
def insert_beginning():
    data = request.form.get('data')
    if data:
        ll.insert_at_beginning(data)
    return redirect(url_for('linkedlist'))

@app.route('/linked-list/insert_end', methods=['POST'])
def insert_end():
    data = request.form.get('data')
    if data:
        ll.insert_at_end(data)
    return redirect(url_for('linkedlist'))

@app.route('/linked-list/remove_beginning')
def remove_beginning():
    ll.remove_beginning()
    return redirect(url_for('linkedlist'))

@app.route('/linked-list/remove_end')
def remove_end():
    ll.remove_at_end()
    return redirect(url_for('linkedlist'))
    
@app.route('/linked-list/remove_at', methods=['POST'])
def remove_at():
    data = request.form.get('data', '').strip()
    removed = None
    
    if data:
       removed = ll.remove_at(data)
       
    return render_template('linked-list.html',
    linked_list=ll.print_list(),
    remove_data=data,
    remove_result=removed,
    reopen_remove_popup=True,
    active_page='works')
    
@app.route('/linked-list/search', methods=['POST'])
def search():
    query = request.form.get('search_data', '').strip()
    found = None

    if query:
        found = ll.search(query)

    return render_template(
        'linked-list.html',
        linked_list=ll.print_list(),
        search_query=query,
        search_result=found,
        reopen_search_popup=True)

@app.route('/infix-to-postfix', methods=['GET', 'POST'])
def infix_to_postfix_conversion():
    result = None
    if request.method == 'POST':
        infix = request.form.get('inputInfix', '')
        result = converter.convert(infix)
    return render_template('infix_postfix.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == "__main__":
    app.run(debug=True)'
