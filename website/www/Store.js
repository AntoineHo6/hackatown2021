function reqListener () {
    // console.log(this.responseText);

    var obj = JSON.parse(this.responseText);
    
    console.log(obj);
    console.log(obj.result.length);

    for (let i = 0; i < obj.result.length; i++) {
        createCard(cardsContainer, obj.result[i].name, "./media/dannyBoy.JPEG", obj.result[i].description, "12$");
    }
  }

  var oReq = new XMLHttpRequest();
  oReq.addEventListener("load", reqListener);
  oReq.open("GET", "http://localhost:8393/products/list");
  oReq.send();





// fetch("http://localhost:8393/products/list").then(function (response) {
//     console.log(response.json());
// }).then(function(data) {
//     console.log(data);
// }).catch(function () {

// });















// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];


// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// create a card
function createCard(cardsContainer, name, imgSrc, description, price) {
    var new_item = document.createElement('div');
    new_item.className = "card";

    var img = document.createElement('img');
    img.setAttribute("src", imgSrc);
    img.setAttribute("alt", "produit");
    img.setAttribute("class", "productCardImg");

    var productName = document.createElement('div');
    productName.className = "cardDescContainer";
    productName.innerHTML = "<h4><b>" + name + "</b></h4>";

    new_item.appendChild(img);
    new_item.appendChild(productName);
    cardsContainer.appendChild(new_item);

    new_item.onclick = () => {
        document.getElementById("modalProductName").innerHTML = name;
        document.getElementById("modalProductImage").setAttribute("src", imgSrc);
        document.getElementById("modalProductDescription").innerHTML = description;
        document.getElementById("modalProductPrice").innerHTML = "<b>" + price + "</b>";

        modal.style.display = "block";
    };
}

var cardsContainer = document.getElementsByClassName("cardsContainer")[0];
// for (let index = 0; index < 20; index++) {
//     createCard(cardsContainer, "sirop d'érable", "./media/dannyBoy.JPEG", "description", "12$");
// }
