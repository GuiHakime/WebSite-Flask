from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('name', validators = [DataRequired(), Length(min = 2, max = 50)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    mensagem = TextAreaField("Mensagem", validators = [DataRequired(), Length(min = 5, max = 500)])
    submit = SubmitField("Enviar")