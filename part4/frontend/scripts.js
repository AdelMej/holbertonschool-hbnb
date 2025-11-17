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
	detailBtn.id = place.id

	detailBtn.addEventListener("click", viewDetails);

	card.appendChild(cardName);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}

function viewDetails() {
	fetch("http://127.0.0.1:5000/api/v1/places/" + this.id)
		.then(response => response.json())
		.then(data => {
			// fetching button parent
			let card = document.getElementById(this.id).parentElement

			// creating a div for card details
			let cardDetails = document.createElement("div");
			cardDetails.className = "place-details"

			// creating paragraph representing the host
			let cardHost = document.createElement("p");

			// creating paragraph representing the description
			let cardInfo = document.createElement("p");
			cardInfo.className = "place-info";
			cardInfo.innerText = data.description

			cardDetails.appendChild(cardHost);

			card.appendChild(cardDetails);
			card.appendChild(cardInfo);
			this.remove()
		})
		.catch(err => console.error("Error:", err));
}

document.addEventListener('DOMContentLoaded', () => {
	fetch("http://127.0.0.1:5000/api/v1/places/")
		.then(response => response.json())
		.then(data => {
			const placeList = document.getElementById("places-list");
			for (const value of data) {
				let card = generateCard(value);
				placeList.appendChild(card);
			}
		})
});
