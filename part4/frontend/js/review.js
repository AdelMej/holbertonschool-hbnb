import { Cookie } from "./utils.js";

document.addEventListener('DOMContentLoaded', () => {

	let review = document.getElementById("rating");
	const params = new URLSearchParams(window.location.search);
	const placeId = params.get("place_id");

	const validRating = [1, 2, 3, 4, 5];

	for (const value of validRating) {
		let option = document.createElement("option");
		option.value = value;
		option.innerText = value;

		review.appendChild(option);
	}

	document.getElementById("review-form").addEventListener("submit", (event) => {
		event.preventDefault();
		submitReview(placeId)
	})
});

async function submitReview(placeId) {
	if (!placeId) {
		window.location.replace("index.html");
	}
	try {
		const fd = new FormData(document.getElementById("review-form"));

		const response = await fetch("http://127.0.0.1:5000/api/v1/reviews/", {
			method: "POST",
			headers: {
				'Content-Type': 'application/json',
				'Authorization': 'Bearer ' + Cookie.get("token")
			},
			body: JSON.stringify({
				'title': fd.get('review-title'),
				'text': fd.get("review"),
				'rating': fd.get("rating"),
				'place_id': placeId,
			})
		})
		if (!response.ok) {
			if (response.status === 401 || response.status === 422) {
				Cookie.delete("token");
				window.location.replace("/login.html")
			}
		}
		const data = await response.json();
		console.log(data);
	} catch (err) {
		console.error("Error: ", err);
	}
}
