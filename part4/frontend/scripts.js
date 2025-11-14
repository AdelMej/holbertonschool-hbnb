function generateCard(place) {
	const card = document.createElement("div");
	card.className = "place-card";

	let cardName = document.createElement("p");
	cardName.innerText = "name" + place.namek;

	let cardPrice = document.createElement("p");
	cardPrice = document.innerText = "Price per night" + place.price;

	const detailBtn = document.createElement("a");
	detailBtn.className = "details-button";

	card.appendChild(cardName);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}


document.addEventListener('DOMContentLoaded', () => {
	fetch("http://127.0.0.1:5000/api/v1/places/")
		.then(response => response.json())
		.then(data => {
			for (const value of data) {
				generateCard(value);
			}
		})

});
