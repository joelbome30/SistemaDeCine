from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DATABASE = "cine.db"
SQL_INIT_FILE = "table.sql"

# Ejecutar table.sql si cine.db no existe
def ejecutar_sql_desde_archivo(db_path, sql_file):
    if not os.path.exists(db_path):
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        with sqlite3.connect(db_path) as conn:
            conn.executescript(sql_script)

def get_sillas():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ocupada FROM sillas ORDER BY id")
        return [bool(row[0]) for row in cursor.fetchall()]

def ocupar_silla(num):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ocupada FROM sillas WHERE id = ?", (num,))
        resultado = cursor.fetchone()
        if resultado is None:
            return "❌ La silla no existe."
        elif resultado[0]:
            return f"🚫 La silla {num} ya está ocupada."
        else:
            cursor.execute("UPDATE sillas SET ocupada = 1 WHERE id = ?", (num,))
            conn.commit()
            return f"✅ Ocupaste la silla {num}."

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        try:
            num = int(request.form["numero"])
            if 1 <= num <= 34:
                mensaje = ocupar_silla(num)
            else:
                mensaje = "Ingresa un número válido entre 1 y 34."
        except ValueError:
            mensaje = "Entrada inválida."

    sillas = get_sillas()
    return render_template("index.html", sillas=sillas, mensaje=mensaje)

if __name__ == "__main__":
    ejecutar_sql_desde_archivo(DATABASE, SQL_INIT_FILE)
    app.run(debug=True)
