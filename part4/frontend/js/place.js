import { Cookie } from "./utils.js";
import { FetchPlace } from "./models/place.js";
import { FetchPlaceReviews } from "./models/review.js";

document.addEventListener('DOMContentLoaded', () => {
	generateDetails();

	// generating reviews
	let reviews = document.getElementById("reviews");
	const params = new URLSearchParams(window.location.search);
	const placeId = params.get("id");
	generateReview(placeId, reviews);

	// show review form if user is connected
	if (!Cookie.get("token")) {
		document.getElementById("add-review").classList.add("hidden");
	}
})

async function generateDetails() {
	let details = document.getElementById("place-details");

	const params = new URLSearchParams(window.location.search);
	const placeId = params.get("id");

	if (!placeId) {
		window.location.replace("index.html");
	}

	let place = new FetchPlace(placeId);
	await place.load();
	if (place.error) {
		window.location.replace("index.html");
	}

	// generating content
	let placeTitle = document.createElement("h1");
	placeTitle.innerText = place.getTitle();

	let placePrice = document.createElement("p");
	placePrice.innerText = "Cost per night: " + place.getPrice() + "€";

	let placeOwner = document.createElement("p");
	placeOwner.innerText = "Host: " + place.getOwner().first_name + " " + place.getOwner().last_name

	let amenities = document.createElement("div");
	amenities.className = "amenities";

	for (const amenity of place.getAmenities()) {
		let amenityName = document.createElement("p");
		amenityName.innerText = amenity.name;
		amenities.appendChild(amenityName);
	}

	let description = document.createElement("p");
	description.innerText = place.getDescription();

	// adding element to the details
	details.appendChild(placeTitle);
	details.appendChild(placePrice);
	details.appendChild(placeOwner);
	if (amenities) {
		details.appendChild(amenities);
	}
	details.appendChild(description);
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
