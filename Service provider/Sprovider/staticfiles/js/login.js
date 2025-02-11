document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".login-form");
    const button = form.querySelector("button");
    
    // Add a loading effect on submit
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        button.innerHTML = "Logging in...";
        button.disabled = true;
        setTimeout(() => {
            form.submit(); // Submit after delay
        }, 1500);
    });
});

// Password Visibility Toggle
function togglePassword() {
    let passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}
