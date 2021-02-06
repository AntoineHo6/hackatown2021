const cards = document.querySelectorAll(".card");

for (let i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", function () {
        alert("You clicked this div");
    });

}