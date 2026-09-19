// Find Healthcare button

const findButton = document.getElementById("findButton");

if (findButton) {

    findButton.addEventListener("click", function () {

        window.location.href = "facilities.html";

    });

}


// Request Consultation button

const consultationButton = document.getElementById("consultationButton");

if (consultationButton) {

    consultationButton.addEventListener("click", function () {

        const urlParams = new URLSearchParams(window.location.search);
        const facilityId = urlParams.get("id");

        window.location.href = "appointment.html?facility_id=" + facilityId;

    });

}


// Appointment form

const appointmentForm = document.getElementById("appointmentForm");

if (appointmentForm) {

    appointmentForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const name = document.getElementById("name").value;
        const age = document.getElementById("age").value;
        const phone = document.getElementById("phone").value;
        const service = document.getElementById("service").value;
        const preferred_date = document.getElementById("date").value;
        const preferred_time = document.getElementById("time").value;
        const urlParams = new URLSearchParams(window.location.search);
        const facility_id = urlParams.get("facility_id");


        fetch("http://127.0.0.1:5000/api/appointments", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                name: name,
                age: age,
                phone: phone,
                service: service,
                preferred_date: preferred_date,
                preferred_time: preferred_time,
                facility_id: facility_id

            })

        })

        .then(response => response.json())

        .then(data => {

            alert(data.message);

            appointmentForm.reset();

        })

        .catch(error => {

            console.error("Error:", error);

            alert("Unable to submit consultation request.");

        });

    });

}