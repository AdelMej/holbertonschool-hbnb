export class FetchReview {
	constructor(reviewId) {
		this.id = reviewId;
		this.data = null;
		this.error = null;
	}

	async load() {
		try {
			if (!this.id) {
				this.error = ("where id?");
				return null;
			}
			const response = await fetch("http://127.0.0.1:5000/api/v1/reviews/" + this.id);

			if (!response.ok) {
				this.error = "HTTP " + response.status;
				return null;
			}

			this.data = await response.json();
			return this.data;

		} catch (err) {
			this.error = err;
			return null;
		}
	}

	getTitle() { return this.data?.title ?? null };
	getText() { return this.data?.text ?? null };
	getRating() { return this.data?.rating ?? null };
	getUser() { return this.data?.user_id ?? null };
}

export class FetchPlaceReviews {
	constructor(placeId) {
		this.id = placeId;
		this.data = null;
		this.error = null;
	}

	async load() {
		try {
			if (!this.id) {
				this.error = ("where id?");
				return null;
			}
			const response = await fetch("http://127.0.0.1:5000/api/v1/places/" + this.id + "/reviews");

			if (!response.ok) {
				this.error = "HTTP " + response.status;
				return null;
			}

			this.data = await response.json();

			return this.data;
		} catch (err) {
			this.error = err;
			return null;
		}
	}

	count() { return this.data?.length ?? 0 }
	getAll() { return this.data ?? [] };
	getTitle(idx) { return this.data?.[idx]?.title ?? null };
	getText(idx) { return this.data?.[idx]?.text ?? null };
	getRating(idx) { return this.data?.[idx]?.rating ?? null };
	getUser(idx) { return this.data?.[idx]?.user_id ?? null }
}

export class CreateReview {

}
