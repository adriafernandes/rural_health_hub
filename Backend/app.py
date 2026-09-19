from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_db_connection

app = Flask(__name__)
CORS(app)


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


@app.route("/api/appointments", methods=["POST"])
def create_appointment():

    data = request.get_json()

    name = data["name"]
    age = data["age"]
    phone = data["phone"]
    service = data["service"]
    preferred_date = data["preferred_date"]
    preferred_time = data["preferred_time"]

    connection = get_db_connection()
    cursor = connection.cursor()

    # Create patient
    cursor.execute(
        """
        INSERT INTO patients (name, age, phone)
        VALUES (%s, %s, %s)
        """,
        (name, age, phone)
    )

    patient_id = cursor.lastrowid

    # For now, use Primary Health Centre
    facility_id = 1

    # Create appointment
    cursor.execute(
        """
        INSERT INTO appointments
        (patient_id, facility_id, service, preferred_date, preferred_time)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            patient_id,
            facility_id,
            service,
            preferred_date,
            preferred_time
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Consultation request submitted successfully!"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)