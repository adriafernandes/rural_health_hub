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
        window.location.href = "appointment.html";
    });
}