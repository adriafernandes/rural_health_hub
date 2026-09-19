from flask import Flask, jsonify
from database import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return "Rural Health Hub Backend is running!"


@app.route("/api/facilities")
def get_facilities():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM facilities")
    facilities = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(facilities)


if __name__ == "__main__":
    app.run(debug=True)