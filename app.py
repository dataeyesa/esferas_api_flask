from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Ruta del archivo .db (ajustar si lo moviste a una carpeta diferente)
DB_PATH = os.path.join(os.path.dirname(__file__), 'base_datos.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/buscar', methods=['GET'])
def buscar():
    palabra = request.args.get('palabra')
    if not palabra:
        return jsonify({'error': 'Debe proporcionar una palabra para buscar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tu_tabla WHERE columna LIKE ?', ('%' + palabra + '%',))
    resultados = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in resultados])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)