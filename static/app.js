//show and hide password in login page
function togglePassword() {
    var passwordField = document.getElementById("password");
    var showPasswordIcon = document.getElementById("hide1");
    var hidePasswordIcon = document.getElementById("hide2");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        showPasswordIcon.style.display = "inline";
        hidePasswordIcon.style.display = "none";
    } else {
        passwordField.type = "password";
        showPasswordIcon.style.display = "none";
        hidePasswordIcon.style.display = "inline";
    }
}

// confirm password in signup page
function validateForm() {
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    
    if (password !== confirm_password) {
        alert("Passwords do not match!");
        return false;
        }
        return true;
    }