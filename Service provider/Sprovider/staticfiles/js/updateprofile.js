document.addEventListener("DOMContentLoaded", function () {
    // Validate phone number
    document.querySelectorAll("input[name='phone_number']").forEach(input => {
        input.addEventListener("input", function () {
            const regex = /^\+?\d{10,15}$/;
            if (!regex.test(this.value)) {
                this.style.border = "2px solid red";
            } else {
                this.style.border = "1px solid #ccc";
            }
        });
    });

    // Ensure user form submits correctly
    document.getElementById("userUpdateForm").addEventListener("submit", function (event) {
        const email = document.getElementById("email").value;
        if (!email.includes("@")) {
            alert("Please enter a valid email!");
            event.preventDefault();
        }
    });

    // Provider and Customer forms: Add form validation
    ["providerUpdateForm", "customerUpdateForm"].forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener("submit", function (event) {
                const phone = form.querySelector("input[name='phone_number']").value;
                const regex = /^\+?\d{10,15}$/;
                if (!regex.test(phone)) {
                    alert("Invalid phone number format!");
                    event.preventDefault();
                }
            });
        }
    });
});
