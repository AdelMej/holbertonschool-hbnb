import { Cookie } from "./utils.js";

function generateCard(place) {
	let card = document.createElement("div");
	card.className = "place-card";

	let cardName = document.createElement("h3");
	cardName.innerText = place.title;

	let cardPrice = document.createElement("p");
	cardPrice.innerText = "Price per night: " + place.price + "€";

	const detailBtn = document.createElement("a");
	detailBtn.className = "details-button";
	detailBtn.innerText = "View Details";
	detailBtn.id = place.id

	let detailLink = document.createElement("a");
	detailBtn.addEventListener("click", () => {
		window.location.replace("http://127.0.0.1:8000/place.html?id=" + place.id);
	});

	// adding card metadata
	card.dataset.id = place.id;
	card.dataset.price = place.price;
	card.dataset.name = place.title;

	// creating a link that redirect to place page
	detailLink.href = "http://127.0.0.1:8000/place.html?id=" + place.id;
	detailLink.appendChild(detailBtn);

	card.appendChild(cardName);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}


document.addEventListener('DOMContentLoaded', () => {
	if (Cookie.get("token")) {
		let loginBtn = document.getElementById("login-link");
		loginBtn.remove();
	}
	fetch("http://127.0.0.1:5000/api/v1/places/")
		.then(response => response.json())
		.then(data => {
			const placeList = document.getElementById("places-list");
			for (const value of data) {
				let card = generateCard(value);
				placeList.appendChild(card);
			}
		})
		.catch(err => {
			console.error("Error: ", err);
		})
	const values = ["All", 10, 50, 100];
	let filter = document.getElementById("price-filter");

	for (const value of values) {
		let option = document.createElement("option");
		option.innerText = value;
		filter.appendChild(option);
		filter.addEventListener("change", filterPlace);
	}
});

function filterPlace() {
	let value = Number(this.value);

	const places = document.querySelectorAll(".place-card")

	for (const place of places) {
		const price = Number(place.dataset.price);
		if (price > value) {
			place.classList.add("hidden");
		}
		else {
			place.classList.remove("hidden");
		}
	}
}
