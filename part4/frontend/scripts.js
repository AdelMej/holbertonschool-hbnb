function generateCard(place) {
	let card = document.createElement("div");
	card.className = "place-card";

	let cardName = document.createElement("p");
	cardName.innerText = "name: " + place.title;

	let cardPrice = document.createElement("p");
	cardPrice.innerText = "Price per night: " + place.price;

	const detailBtn = document.createElement("a");
	detailBtn.className = "details-button";
	detailBtn.innerText = "View Details";

	card.appendChild(cardName);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}


document.addEventListener('DOMContentLoaded', () => {
	fetch("http://127.0.0.1:5000/api/v1/places/")
		.then(response => response.json())
		.then(data => {
			const placeList = document.getElementById("places-list");
			for (const value of data) {
				let card = generateCard(value);
				placeList.append(card);
			}
		})

});
