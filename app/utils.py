import os
from werkzeug.utils import secure_filename
from config import Config

def guardar_archivo(archivo):
    filename = secure_filename(archivo.filename)
    ruta = os.path.join(Config.UPLOAD_FOLDER, filename)
    archivo.save(ruta)
    return filename
