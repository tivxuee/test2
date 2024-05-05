from wtforms import StringField, SubmitField,SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import PasswordField

class CreateGroupForm(FlaskForm):
    groupSize=SelectField("Group Size",choices=[2,3,4])
    student1 = StringField('Student 1 id',validators=[DataRequired()])
    student2 = StringField('Student 2 id',validators=[DataRequired()])
    student3 = StringField('Student 3 id')
    student4 = StringField('Student 4 id')
    password = PasswordField('Password',validators=[DataRequired()])
    student4 = StringField('Student 4 id')
    submit=SubmitField('Create Group')

class LoginForm(FlaskForm):
    uwa_id = StringField('UWA ID',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')
