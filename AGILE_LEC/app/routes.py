from flask import redirect, render_template, url_for, request
from app import flaskapp
from app.model import Group, Student

tom = Student(uwaID='12345678', name='Tom')
jerry = Student(uwaID='87654321', name='Jerry')
cardi = Student(uwaID='12348765', name='Cardi')
talor = Student(uwaID='87654321', name='Talor')

group1 = Group([tom, jerry, cardi, talor])

projectGroups = [group1]


@flaskapp.route('/')
@flaskapp.route('/groups')
#for the flaskapp object, we are defining a route
def groups():
    return render_template('listGroups.html',groups=projectGroups)

@flaskapp.route('/create')
def create():
    return render_template('createGroup.html')

@flaskapp.route('/submit', methods=['POST'])
def submit():
    print(request.method)
    print(request.form)
    print(request.form['numberOfstudents'])
    print('submitted!')
    return redirect(location=url_for('groups')) 