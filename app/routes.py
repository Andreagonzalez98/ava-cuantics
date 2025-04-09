from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Modulo, Contenido, Carrito
from . import db
import os
from werkzeug.utils import secure_filename
from config import Config

main = Blueprint('main', __name__)

@main.route('/')
def home():
    modulos = Modulo.query.all()
    return "¡Bienvenido al AVA Cuántico!"

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', usuario=current_user)

@main.route('/modulo/<int:modulo_id>')
@login_required
def ver_modulo(modulo_id):
    modulo = Modulo.query.get_or_404(modulo_id)
    contenidos = Contenido.query.filter_by(modulo_id=modulo.id).all()
    return render_template('modulo.html', modulo=modulo, contenidos=contenidos)

@main.route('/carrito')
@login_required
def carrito():
    items = Carrito.query.filter_by(usuario_id=current_user.id).all()
    return render_template('carrito.html', items=items)

@main.route('/admin/cargar_modulo', methods=['GET', 'POST'])
@login_required
def cargar_modulo():
    if not current_user.es_admin:
        flash('Acceso restringido')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        nuevo_modulo = Modulo(titulo=titulo, descripcion=descripcion)
        db.session.add(nuevo_modulo)
        db.session.commit()
        flash('Módulo cargado correctamente')
        return redirect(url_for('main.index'))
    
    return render_template('admin/cargar_modulo.html')

@main.route('/admin/cargar_contenido/<int:modulo_id>', methods=['GET', 'POST'])
@login_required
def cargar_contenido(modulo_id):
    if not current_user.es_admin:
        flash('Acceso restringido')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        archivo = request.files['archivo']
        if archivo:
            filename = secure_filename(archivo.filename)
            archivo.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            nuevo_contenido = Contenido(titulo=titulo, archivo=filename, modulo_id=modulo_id)
            db.session.add(nuevo_contenido)
            db.session.commit()
            flash('Contenido cargado')
            return redirect(url_for('main.index'))
    
    return render_template('admin/cargar_contenido.html')
