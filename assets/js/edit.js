var firstName = document.getElementById("id_first_name");
var lastName = document.getElementById("id_last_name");
var email = document.getElementById("id_email");
var password = document.getElementById("id_password");
var btn = document.getElementById("submit");

function edit_firstname(){
    firstName.removeAttribute("readonly");
    btn.removeAttribute("hidden");
}

function edit_lastname(){
    lastName.removeAttribute("readonly");
    btn.removeAttribute("hidden");
}

function edit_email(){
    email.removeAttribute("readonly");
    btn.removeAttribute("hidden");
}

function edit_password(){
    password.removeAttribute("readonly");
    btn.removeAttribute("hidden");
}