import { Cookie } from "./utils.js";

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

	// adding card metadata
	card.dataset.id = place.id;
	card.dataset.price = place.price;
	card.dataset.name = place.title;

	card.appendChild(cardName);
	card.appendChild(cardPrice);
	card.appendChild(detailBtn);

	return card;
}

async function viewDetails() {
	try {
		const response = await fetch("http://127.0.0.1:5000/api/v1/places/" + this.id)

		if (!response.ok) {
			console.error("HTTP error: ", response.status);
			return;
		}

		const data = await response.json();

		// fetching button parent
		let card = document.getElementById(this.id).parentElement

		// creating a div for card details
		let cardDetails = document.createElement("div");
		cardDetails.className = "place-details";

		// creating paragraph representing the host
		let cardHost = document.createElement("p");
		cardHost.innerText = "Host: " + data.owner.first_name + " " + data.owner.last_name;

		// creating paragraph representing the price
		let cardPrice = document.createElement("p");
		cardPrice.className = "price";
		cardPrice.innerText = "Price: " + data.price + " €";

		// creating amenities div and paragraph
		let cardAmenities = document.createElement("div");
		for (const amenity of data.amenities) {
			let cardAmenty = document.createElement("p")
			cardAmenty.innerText = amenity.name;
			cardAmenities.appendChild(cardAmenty);
		}

		// add information to the details
		cardDetails.appendChild(cardHost);
		cardDetails.appendChild(cardAmenities);

		let cardReview = document.createElement("div");
		generateReview(this.id, cardReview)

		// creating paragraph representing the description
		let cardInfo = document.createElement("p");
		cardInfo.className = "place-info";
		cardInfo.innerText = data.description

		card.appendChild(cardDetails);
		card.appendChild(cardInfo);
		if (cardReview) {
			card.appendChild(cardReview);
		}

		this.remove()

	}
	catch (err) {
		console.error("Error: ", err);
	}
};

async function generateReview(place_id, card) {
	try {
		const response = await fetch("http://127.0.0.1:5000/api/v1/places/" + place_id + "/reviews");
		if (response.status === 404) {
			if (Cookie.get("token")) {
				let reviewBtn = document.createElement("a");
				reviewBtn.href = "/add_review.html";
				reviewBtn.innerText = "add a review";

				card.appendChild(reviewBtn);
			}

			let reviews = document.createElement("p");
			reviews.innerText = "No review found";

			card.appendChild(reviews);
			return;
		}

		if (!response.ok) {
			console.error("HTTP error:", response.status);
			return;
		}

		const data = await response.json();

		if (!data) return;
		let divReview = document.createElement("div");

		if (Cookie.get("token")) {
			let reviewBtn = document.createElement("a");
			reviewBtn.href = "/add_review.html";
			reviewBtn.innerText = "add a review";
			divReview.appendChild(reviewBtn);
		}

		for (const review of data) {
			let reviewTitle = document.createElement("p");
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
	} catch (err) {
		console.error("Error: ", err);
	}
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
		if (price < value) {
			place.style.display = "none";
		}
		else {
			place.style.display = "";
		}
	}
}
