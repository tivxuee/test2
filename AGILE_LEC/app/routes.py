from flask import flash, redirect, render_template, url_for, request
from app import flaskapp, db
from app.model import Group, Student
from .forms import CreateGroupForm, LoginForm
from flask_login import login_user,logout_user
from flask_login import login_required



@flaskapp.route('/')
@flaskapp.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html',form=form)

    studentID = form.uwa_id.data
    student = Student.query.get(studentID)
    if not student:
        flash(f'Student {studentID} not found','error')
        return render_template('login.html',form=form)


    password = form.password.data
    if not student.check_password(password):
        flash('Incorrect password','error')
        return render_template('login.html',form=form)

    
    login_user(student)
    return redirect(url_for('groups'))

@flaskapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@flaskapp.route('/groups')
#for the flaskapp object, we are defining a route
@login_required
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html',groups=all_groups)

@flaskapp.route('/create')
@login_required
def create():
    form = CreateGroupForm()
    return render_template('createGroup.html',form=form)

@flaskapp.route('/submit', methods=['POST'])

def submit():
    form = CreateGroupForm()
    if not form.validate_on_submit():
        return render_template('createGroup.html',form=form)

    groupSize = int(form.groupSize.data)
    studentIDs = [
        form.student1.data,
        form.student2.data,
        form.student3.data,
        form.student4.data
    ][:groupSize]

    students=[find_student_By_id(id) for id in studentIDs]
    
    if not all(students):
        return render_template('createGroup.html',form=form)
    
    all_unique = len(set(students))==len(students)
    if not all_unique:
        flash('All students must be unique','error')
        return render_template('createGroup.html',form=form)

    all_free=True
    for student in students:
        if student.group:
            flash(f'Student {student} is already in a group','error')
            all_free=False

    if not all_free:
        return render_template('createGroup.html',form=form)
            
    group=Group()
    group.students=students

   
    db.session.add(group)
    db.session.commit()

def find_student_By_id(id:str):
    student = Student.query.get(id)
    if not student:
        flash(f'Student 1 not found: {id}', 'error')
    return student