from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="notesuser",
    password="password",
    database="notesdb"
)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor = db.cursor()
    if request.method == "POST":
        note = request.form["note"]
        cursor.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
        db.commit()

    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    return render_template("index.html", notes=notes)

app.run(host="0.0.0.0", port=80)
