from flask import redirect, render_template, url_for, request
from app import flaskapp, db
from app.model import Group, Student

@flaskapp.route('/')
@flaskapp.route('/groups')
#for the flaskapp object, we are defining a route
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html',groups=all_groups)

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