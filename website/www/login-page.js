const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginMsg = document.getElementById("login-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        localStorage.setItem("isLogged", "1");
        window.location.replace("./index.html");

        

    } else {
        loginErrorMsg.style.opacity = 1;
        setTimeout(function(){ loginErrorMsg.style.opacity = 0; }, 3000);
    }
})