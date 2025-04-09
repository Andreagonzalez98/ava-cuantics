from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario
from .forms import RegistroForm, LoginForm
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['GET', 'POST'])
def auth():
    login_form = LoginForm(prefix='login')
    registro_form = RegistroForm(prefix='registro')

    # Login
    if login_form.submit.data and login_form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=login_form.correo.data).first()
        if usuario and check_password_hash(usuario.contrasena, login_form.contrasena.data):
            login_user(usuario)
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('main.dashboard'))
        flash('Correo o contraseña incorrectos.')

    # Registro
    if registro_form.submit.data and registro_form.validate_on_submit():
        existe = Usuario.query.filter_by(correo=registro_form.correo.data).first()
        if existe:
            flash('El correo ya está registrado.')
        else:
            nuevo_usuario = Usuario(
                nombre=registro_form.nombre.data,
                correo=registro_form.correo.data,
                contrasena=generate_password_hash(registro_form.contrasena.data)
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Registro exitoso. Ahora inicia sesión.')

    return render_template('auth.html', login_form=login_form, registro_form=registro_form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.')
    return redirect(url_for('auth.auth'))
