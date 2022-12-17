from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#enter item table. need to enter all the parameter and then press enter and the item will add to table
class RegisterForm(FlaskForm):
    id = StringField(label='id')
    name = StringField(label='name')
    price = StringField(label= 'price')
    submit = SubmitField(label='Add Item')

