from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_flask_2025'
DATABASE = 'empleados.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            cedula TEXT NOT NULL UNIQUE,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    empleados = conn.execute('SELECT * FROM empleados ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', empleados=empleados)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        cedula = request.form['cedula'].strip()
        telefono = request.form['telefono'].strip()
        direccion = request.form['direccion'].strip()
        
        if not all([nombre, apellido, cedula, telefono, direccion]):
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('crear'))
        
        try:
            conn = get_db()
            conn.execute(
                'INSERT INTO empleados (nombre, apellido, cedula, telefono, direccion) VALUES (?, ?, ?, ?, ?)',
                (nombre, apellido, cedula, telefono, direccion)
            )
            conn.commit()
            conn.close()
            flash('Empleado registrado exitosamente', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('La cédula ya existe en el sistema', 'error')
            return redirect(url_for('crear'))
    
    return render_template('crear.html')

@app.route('/ver/<int:id>')
def ver(id):
    conn = get_db()
    empleado = conn.execute('SELECT * FROM empleados WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if not empleado:
        flash('Empleado no encontrado', 'error')
        return redirect(url_for('index'))
    
    return render_template('ver.html', empleado=empleado)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db()
    empleado = conn.execute('SELECT * FROM empleados WHERE id = ?', (id,)).fetchone()
    
    if not empleado:
        conn.close()
        flash('Empleado no encontrado', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        cedula = request.form['cedula'].strip()
        telefono = request.form['telefono'].strip()
        direccion = request.form['direccion'].strip()
        
        if not all([nombre, apellido, cedula, telefono, direccion]):
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('editar', id=id))
        
        try:
            conn.execute(
                'UPDATE empleados SET nombre=?, apellido=?, cedula=?, telefono=?, direccion=? WHERE id=?',
                (nombre, apellido, cedula, telefono, direccion, id)
            )
            conn.commit()
            conn.close()
            flash('Empleado actualizado exitosamente', 'success')
            return redirect(url_for('ver', id=id))
        except sqlite3.IntegrityError:
            flash('La cédula ya existe en el sistema', 'error')
            return redirect(url_for('editar', id=id))
    
    conn.close()
    return render_template('editar.html', empleado=empleado)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM empleados WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Empleado eliminado exitosamente', 'success')
    return redirect(url_for('index'))

@app.route('/buscar')
def buscar():
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect(url_for('index'))
    
    conn = get_db()
    empleados = conn.execute(
        '''SELECT * FROM empleados 
           WHERE nombre LIKE ? OR apellido LIKE ? OR cedula LIKE ?
           ORDER BY id DESC''',
        (f'%{query}%', f'%{query}%', f'%{query}%')
    ).fetchall()
    conn.close()
    
    return render_template('index.html', empleados=empleados, busqueda=query)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)