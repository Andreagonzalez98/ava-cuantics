from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')
