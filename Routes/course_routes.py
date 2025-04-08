from flask import session, redirect, url_for, flash

@course_bp.route('/upload_course', methods=['GET', 'POST'])
def upload_course():
    if 'user_id' not in session:
        flash('Debes iniciar sesión como administrador.')
        return redirect(url_for('auth.login'))

    # ... resto del código para subir curso
