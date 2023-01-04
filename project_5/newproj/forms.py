from flask_wtf import Form
from wtforms import TextAreaField, IntegerField, TextAreaField, SubmitField, RadioField,   SelectField, StringField

from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextAreaField("Name Of Student",[validators.DataRequired("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = TextAreaField("Email",[validators.DataRequired("Please enter your email address."),
      validators.DataRequired("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")