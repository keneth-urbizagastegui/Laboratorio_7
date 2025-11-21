from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# --- CONFIGURACIÓN DE LA BASE DE DATOS (Tus datos reales) ---
DB_HOST = "vehiculos-db.cfs4boqm1wbl.us-east-1.rds.amazonaws.com"
DB_USER = "root"                 # OJO: Es 'root', no 'admin'
DB_PASSWORD = "Ut3c$201810610"   # Tu contraseña exacta
DB_PORT = 3306
DB_NAME = "vehiculos_db"         # Nombre de la BD final

# Función para conectar (con reconexión automática si la BD no existe)
def get_db_connection():
    try:
        # Intentamos conectar directo a la base de datos 'vehiculos_db'
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as e:
        # Si falla porque la BD no existe (Código 1049), conectamos sin DB y la creamos
        if e.args[0] == 1049:
            conn_temp = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
            with conn_temp.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {DB_NAME}")
            conn_temp.close()
            # Ahora sí conectamos bien
            conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT, cursorclass=pymysql.cursors.DictCursor)
        else:
            raise e
    return conn

# Crear tabla si no existe (Automático al iniciar)
def init_db():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehiculos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(50) NOT NULL,
                modelo VARCHAR(50) NOT NULL,
                precio DECIMAL(10, 2) NOT NULL
            )
        """)
    conn.commit()
    conn.close()

# Inicializamos la DB solo una vez al principio (o dentro de las rutas si prefieres)
# En Lambda a veces es mejor llamar a init_db() dentro de una petición si falla,
# pero para este lab, ponlo aquí abajo si lo corres local primero:
try:
    init_db()
    print("✅ Base de datos y tabla conectadas/creadas correctamente.")
except Exception as e:
    print(f"❌ Error de conexión DB: {e}")

# --- RUTAS ---
@app.route('/')
def index():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM vehiculos")
        vehiculos = cursor.fetchall()
    conn.close()
    return render_template('index.html', vehiculos=vehiculos)

@app.route('/agregar', methods=('GET', 'POST'))
def agregar():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO vehiculos (marca, modelo, precio) VALUES (%s, %s, %s)', (marca, modelo, precio))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)