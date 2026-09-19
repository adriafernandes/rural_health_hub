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
    facility_id = data["facility_id"]

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
    "message": "Consultation request submitted successfully!",
    "patient_id": patient_id
}), 201

@app.route("/api/health-history/<int:patient_id>")
def get_health_history(patient_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            appointments.id,
            facilities.name AS facility_name,
            appointments.service,
            appointments.preferred_date,
            appointments.preferred_time,
            appointments.status
        FROM appointments
        JOIN facilities
            ON appointments.facility_id = facilities.id
        WHERE appointments.patient_id = %s
        ORDER BY appointments.preferred_date DESC
        """,
        (patient_id,)
    )

    history = cursor.fetchall()

    cursor.close()
    connection.close()

    for appointment in history:
        appointment["preferred_time"] = str(appointment["preferred_time"])

    return jsonify(history)
@app.route("/api/facilities/<int:facility_id>")
def get_facility(facility_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM facilities WHERE id = %s",
        (facility_id,)
    )

    facility = cursor.fetchone()

    cursor.close()
    connection.close()

    if facility is None:
        return jsonify({"error": "Facility not found"}), 404

    return jsonify(facility)
if __name__ == "__main__":
    app.run(debug=True)