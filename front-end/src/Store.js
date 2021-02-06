// for (let index = 0; index < 3; index++) {
//     let clone = document.querySelector('.card').cloneNode( true );
//     document.querySelector('p').appendChild( clone );
// }

function allo() {
    document.querySelector(".cardsContainer").innerHTML += `
        <div class="card">
            < img src = "./media/dannyBoy.JPEG" alt = "produit" class="productCardImg" >
            <div class="cardDescContainer">
                <h4><b>Sirop d'érable</b></h4>
            </div>
        </div > `;
}

const cards = document.querySelectorAll(".card");

for (let i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", function () {
        allo();
    });

}