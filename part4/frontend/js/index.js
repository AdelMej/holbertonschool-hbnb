import { Cookie } from "./utils.js";
import { FetchPlaceReviews } from "./models/review.js";
import { FetchPlace } from "./models/place.js";

function generateCard(place) {
	let card = document.createElement("div");
	card.className = "place-card";

	let cardName = document.createElement("h1");
	cardName.innerText = place.title;

	let cardPrice = document.createElement("p");
	cardPrice.innerText = "Price per night: " + place.price + "€";

	const detailBtn = document.createElement("a");
	detailBtn.className = "details-button";
	detailBtn.innerText = "View Details";
	detailBtn.id = place.id

	detailBtn.addEventListener("click", viewDetails);

	// adding card metadata
	card.dataset.id = place.id;
	card.dataset.price = place.price;
	card.dataset.name = place.title;

	// creating a link that redirect to place page
	let placeLink = document.createElement("a");
	placeLink.href = "http://127.0.0.1:8000/place.html?id=" + place.id;
	placeLink.appendChild(cardName);

	card.appendChild(placeLink);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}

async function viewDetails() {
	let card = this.parentElement;

	let place = new FetchPlace(this.id);
	await place.load();

	// Create details container
	const details = document.createElement("div");
	details.className = "place-details";

	// Host
	const host = document.createElement("p");
	host.innerText = "Host: " + place.getOwner().first_name + " " + place.getOwner().last_name;

	// Amenities
	const amenities = document.createElement("div");
	for (const a of place.getAmenities()) {
		const p = document.createElement("p");
		p.innerText = a.name;
		amenities.appendChild(p);
	}

	// Description
	const desc = document.createElement("p");
	desc.className = "place-info";
	desc.innerText = place.getDescription();

	// Reviews
	const reviewSection = document.createElement("div");
	generateReview(this.id, reviewSection);

	// Append all
	details.appendChild(host);
	details.appendChild(amenities);
	details.appendChild(desc);
	details.appendChild(reviewSection);

	// Reduce button
	const reduceBtn = document.createElement("button");
	reduceBtn.innerText = "Hide details";

	reduceBtn.onclick = () => {
		details.classList.add("hidden");
		this.classList.remove("hidden");
	};

	details.appendChild(reduceBtn);

	// Insert into card
	card.appendChild(details);

	// Hide "view details" button
	this.classList.add("hidden");
}

async function generateReview(place_id, card) {

	let placeReviews = new FetchPlaceReviews(place_id);
	await placeReviews.load();

	let divReview = document.createElement("div");

	for (const review of placeReviews.getAll()) {
		let reviewTitle = document.createElement("h1");
		reviewTitle.innerText = review.title;

		let reviewText = document.createElement("p");
		reviewText.innerText = review.text;

		let reviewRating = document.createElement("p");
		reviewRating.innerText = review.rating;

		divReview.appendChild(reviewTitle);
		divReview.appendChild(reviewText);
		divReview.appendChild(reviewRating);
	}
	card.appendChild(divReview);
};


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
