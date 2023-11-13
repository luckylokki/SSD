from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,SelectField

class SelfPriceForm(FlaskForm):
    grade_choices = [('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')]
    grade = SelectField('Grade', choices=grade_choices)
    item_price = IntegerField('Item Price')
    cry_amount = IntegerField('Cry Amount')
    submit = SubmitField('Calculate')

class ShotForm(FlaskForm):
    grade_choices = [('D', 'D'), ('C', 'C'), ('B', 'B'), ('A', 'A'), ('S', 'S')]
    grade = SelectField('Grade', choices=grade_choices)
    cry = IntegerField('Cry')
    submit = SubmitField('Calculate')


