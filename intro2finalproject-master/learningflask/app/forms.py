from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, required

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UnderValuedForm(FlaskForm):
    ListDepth = PasswordField('How many items would you like to see',
    validators=[DataRequired()])

    SearchType = SelectField('How would you like to search',     choices=[
     ( 'findundervaluedsingleitem', 'Highest individual item profit'),
     ( 'undervaluedstack', 'Highest Stack profit')
     ],   validators=[required()])
    submit = SubmitField('Search Database')
