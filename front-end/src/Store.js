function allo(container) {
    

    var new_item = document.createElement('div');
    new_item.className = "card";

    var img = document.createElement('img')
    img.setAttribute("src", "./media/dannyBoy.JPEG");
    img.setAttribute("alt","produit")
    img.setAttribute("class","productCardImg")

    var new_des = document.createElement('div');
    new_des.className = "cardDescContainer";
    new_des.innerHTML = "<h4><b>Sirop d'érable</b></h4>"


    new_item.appendChild(img)
    new_item.appendChild(new_des)

    container.appendChild(new_item)

}

for (let index = 0; index < 10
    ; index++) {
    var container = document.getElementsByClassName("cardsContainer")[0]
    allo(container)
 }
 

// const cards = document.querySelectorAll(".card");

// for (let i = 0; i < cards.length; i++) {
//     cards[i].addEventListener("click", function () {
//         allo();
//     });

// }