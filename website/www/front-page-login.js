

function userLogin(){
    if(localStorage.getItem("isLogged") == "1"){
        document.getElementById("welcomeMsg").innerHTML = "Bienvenu.e"+localStorage.getItem(username)+"au Panier du Lys!";
        document.getElementById("btn").innerHTML = "Deconnexion";
        document.getElementById("btn").setAttribute('href','index.html');
        document.getElementById('logo').setAttribute('src','media/medium.jpg');
    }
    else{
        document.getElementById("mbloginsignupsdiv").innerHTML = "<a href='login.html' class='mbloginbtn'>Login</a>";
    }

}

